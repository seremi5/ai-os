# Config & Environment

## Pattern

All environment validation happens in `src/config/env.py`, which is imported at the top of `analyze.py`. If any required key is missing, the process exits before running anything else.

```python
# src/config/env.py
import os
import sys

def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        print(f"Error: {key} not set. Copy .env.example to .env and add your key.")
        sys.exit(1)
    return value

GEMINI_API_KEY    = _require("GEMINI_API_KEY")
ALPHA_VANTAGE_KEY = _require("ALPHA_VANTAGE_KEY")
```

## Constants

Non-secret configuration (weights, thresholds, labels) lives in `src/config/constants.py`:

```python
# src/config/constants.py
SCORE_WEIGHTS = {
    "valuation": 35,
    "health":    35,
    "growth":    30,
}

RATING_LABELS = {
    (80, 100): "Low Risk",
    (60, 80):  "Moderate Risk",
    (40, 60):  "Elevated Risk",
    (0,  40):  "High Risk",
}
```

## .env.example

Always ship a `.env.example` with placeholder values. Every required key must appear here with a comment explaining where to get it:

```bash
# Get yours at: https://aistudio.google.com/app/apikey
GEMINI_API_KEY=

# Get yours at: https://www.alphavantage.co/support/#api-key (free: 25 req/day)
ALPHA_VANTAGE_KEY=
```

## .gitignore Entries

Always include:

```
.env
*.sqlite
reports/*.html
reports/*.csv
reports/*.jsonl
```
