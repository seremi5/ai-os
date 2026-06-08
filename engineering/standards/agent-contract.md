# Agent Contract

Rules every agent module must follow.

## Public Interface

Every agent exports exactly one public function:

```python
def run(...) -> ResultType:
```

Nothing else is public. Internal helpers are prefixed with `_`.

## Typed Signatures

All inputs and outputs are typed. Dataclasses for structured data:

```python
# Good
def run(data: MarketData, score: ScoreResult) -> AnalysisResult:
    ...

# Bad
def run(data: dict, score: dict) -> dict:
    ...
```

## No Side Effects

Agents do not:
- Write files
- Call external APIs directly (use services)
- Modify their inputs
- Store state between calls

```python
# Bad — agent calling an API directly
def run(ticker: str) -> AnalysisResult:
    raw = requests.get(f"https://api.example.com/{ticker}")  # ← belongs in a service

# Good — agent receiving pre-fetched data
def run(data: MarketData) -> AnalysisResult:
    ...
```

## Logging

Use the shared logger. Never use `print()`:

```python
from src.utils.logger import logger

def run(data: MarketData) -> AnalysisResult:
    logger.step("Analyzing with Gemini...")
    result = _call_gemini(data)
    logger.success("Analysis complete")
    return result
```

## Error Handling

- Raise specific exceptions, never bare `except:`
- User-facing errors go in the CLI entry point, not in agents
- If an agent can continue with degraded output (e.g. missing optional data), log a warning and continue
- If an agent cannot continue, raise — let the CLI handle the message and exit

```python
# Bad
try:
    result = _call_gemini(data)
except:
    return None  # silent failure

# Good
try:
    result = _call_gemini(data)
except google.api_core.exceptions.ResourceExhausted:
    logger.warn("Gemini rate limit hit, retrying in 30s...")
    time.sleep(30)
    result = _call_gemini(data)
```

## Naming

| Thing | Convention | Example |
|---|---|---|
| Agent module | `snake_case.py` | `report_builder.py` |
| Entry point | `run` | `def run(...)` |
| Internal helpers | `_verb_noun` | `_build_page_one` |
| Result dataclass | `<Agent>Result` | `ScorerResult` |
| Input dataclass | `<Domain>Data` | `MarketData` |
