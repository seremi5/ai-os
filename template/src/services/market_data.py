from dataclasses import dataclass


@dataclass
class MarketData:
    ticker:          str
    price:           float | None = None
    pe_ratio:        float | None = None
    revenue_growth:  float | None = None
    # Add fields as needed


def fetch(ticker: str) -> MarketData:
    # TODO: implement data fetching (yfinance, Alpha Vantage, etc.)
    return MarketData(ticker=ticker)
