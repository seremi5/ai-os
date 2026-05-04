# Pipeline Pattern

The core pattern for all sequential AI pipelines.

## Structure

```
CLI  →  Data Layer  →  Scoring Layer  →  Agent Layer  →  Output Layer
```

Each layer receives the output of the previous one. No layer reaches back.

## Layer Responsibilities

### 1. Data Layer (`src/services/`)

- One file per external data source
- Each service returns a typed dataclass, never a raw dict
- Handles retries, rate limits, and caching internally
- If a source is unavailable, returns `None` or a partial dataclass — never raises to the agent layer unless truly fatal

```python
# src/services/market_data.py
@dataclass
class MarketData:
    ticker: str
    price: float
    pe_ratio: float | None
    revenue_growth: float | None
    # ...

def fetch(ticker: str) -> MarketData:
    ...
```

### 2. Scoring Layer (`src/agents/scorer.py`)

- Pure Python, no AI calls
- Deterministic: same inputs always produce the same score
- Weighted sub-scores that sum to 100
- Missing data reduces the relevant sub-score proportionally — never crashes

```python
def run(data: MarketData) -> ScoreResult:
    valuation = score_valuation(data)   # 0–35
    health    = score_health(data)      # 0–35
    growth    = score_growth(data)      # 0–30
    total     = valuation + health + growth
    return ScoreResult(total=total, valuation=valuation, health=health, growth=growth)
```

### 3. Agent Layer (`src/agents/`)

- Receives `MarketData` + `ScoreResult` (and any optional enrichments)
- Calls the AI model with a structured prompt
- Returns a typed result — never raw model output
- For adversarial analysis, use the [debate pattern](debate.md)

### 4. Output Layer (`src/agents/report_builder.py`)

- Receives all upstream results
- Produces a single self-contained HTML file
- No logic here — just rendering
- Opens in browser automatically unless `--no-browser`

## CLI Entry Point

```python
# analyze.py
import argparse
from src.config import env          # validates keys immediately on import
from src.agents import data_fetcher, scorer, analyst, report_builder

def main(ticker: str, deep: bool, no_macro: bool) -> None:
    data    = data_fetcher.run(ticker, deep=deep, no_macro=no_macro)
    score   = scorer.run(data)
    analysis = analyst.run(data, score)
    report_builder.run(ticker, data, score, analysis)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("--deep", action="store_true")
    parser.add_argument("--no-macro", action="store_true")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    main(args.ticker, args.deep, args.no_macro)
```
