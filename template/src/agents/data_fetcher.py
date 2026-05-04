from src.services.market_data import fetch, MarketData
from src.utils.logger import logger


def run(ticker: str, deep: bool = False, no_macro: bool = False) -> MarketData:
    logger.step(f"Fetching data for {ticker}")
    data = fetch(ticker)
    logger.success("Data fetched")
    return data
