import os
import webbrowser
from datetime import datetime

from src.services.market_data import MarketData
from src.agents.scorer import ScoreResult
from src.agents.analyst import AnalysisResult
from src.utils.logger import logger

REPORTS_DIR = "reports"


def run(
    ticker: str,
    data: MarketData,
    score: ScoreResult,
    analysis: AnalysisResult,
    open_browser: bool = True,
) -> str:
    logger.step("Building report")
    os.makedirs(REPORTS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(REPORTS_DIR, f"{ticker}_{timestamp}.html")

    html = _build_html(ticker, data, score, analysis)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    logger.success(f"Report saved: {path}")
    if open_browser:
        webbrowser.open(f"file://{os.path.abspath(path)}")

    return path


def _build_html(
    ticker: str,
    data: MarketData,
    score: ScoreResult,
    analysis: AnalysisResult,
) -> str:
    # TODO: implement full HTML report
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{ticker} Analysis</title>
  <style>
    body {{ font-family: sans-serif; background: #08090d; color: #e5e7eb; padding: 2rem; }}
    h1   {{ color: #10b981; }}
  </style>
</head>
<body>
  <h1>{ticker}</h1>
  <p>Score: {score.total:.1f}/100</p>
  <h2>Bull Case</h2>
  <p>{analysis.bull_case}</p>
  <h2>Bear Case</h2>
  <p>{analysis.bear_case}</p>
  <h2>Verdict</h2>
  <p>{analysis.verdict}</p>
</body>
</html>"""
