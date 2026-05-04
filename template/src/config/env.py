import os
import sys


def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        print(f"Error: {key} not configured. Copy .env.example to .env and add your key.")
        sys.exit(1)
    return value


# Add your required keys here
GEMINI_API_KEY = _require("GEMINI_API_KEY")
