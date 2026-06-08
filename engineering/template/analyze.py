import argparse
import sys

from src.config import env  # validates all required env vars on import
from src.agents import data_fetcher, scorer, analyst, report_builder
from src.utils.logger import logger


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a stock ticker")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol (e.g. ORCL)")
    parser.add_argument("--deep", action="store_true", help="Include SEC filings and insider activity")
    parser.add_argument("--no-macro", action="store_true", help="Skip macro and peer context")
    parser.add_argument("--no-browser", action="store_true", help="Don't open the report in browser")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    logger.step(f"Starting analysis for {ticker}")

    data     = data_fetcher.run(ticker, deep=args.deep, no_macro=args.no_macro)
    score    = scorer.run(data)
    analysis = analyst.run(data, score)
    report_builder.run(ticker, data, score, analysis, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
