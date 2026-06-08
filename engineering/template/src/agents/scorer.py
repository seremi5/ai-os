from dataclasses import dataclass
from src.services.market_data import MarketData
from src.config.constants import SCORE_WEIGHTS
from src.utils.logger import logger


@dataclass
class ScoreResult:
    total:      float
    valuation:  float
    health:     float
    growth:     float


def run(data: MarketData) -> ScoreResult:
    logger.step("Scoring")
    valuation = _score_valuation(data)
    health    = _score_health(data)
    growth    = _score_growth(data)
    total     = valuation + health + growth
    logger.success(f"Score: {total:.1f}/100")
    return ScoreResult(total=total, valuation=valuation, health=health, growth=growth)


def _score_valuation(data: MarketData) -> float:
    # TODO: implement valuation scoring (max SCORE_WEIGHTS["valuation"])
    return 0.0


def _score_health(data: MarketData) -> float:
    # TODO: implement financial health scoring (max SCORE_WEIGHTS["health"])
    return 0.0


def _score_growth(data: MarketData) -> float:
    # TODO: implement growth scoring (max SCORE_WEIGHTS["growth"])
    return 0.0
