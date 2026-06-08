from dataclasses import dataclass
import google.generativeai as genai

from src.config.env import GEMINI_API_KEY
from src.services.market_data import MarketData
from src.agents.scorer import ScoreResult
from src.utils.logger import logger

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")


@dataclass
class AnalysisResult:
    bull_case:   str
    bear_case:   str
    verdict:     str
    conviction:  str   # "high" | "medium" | "low"


def run(data: MarketData, score: ScoreResult) -> AnalysisResult:
    logger.step("Running AI analysis")
    bull   = _run_bull(data, score)
    bear   = _run_bear(data, score)
    verdict = _run_judge(data, score, bull, bear)
    logger.success("Analysis complete")
    return AnalysisResult(bull_case=bull, bear_case=bear, verdict=verdict, conviction="medium")


def _run_bull(data: MarketData, score: ScoreResult) -> str:
    prompt = f"""You are a bull analyst. Make the strongest case FOR this stock.
Use concrete data. Do not mention risks.

Ticker: {data.ticker}
Score: {score.total:.1f}/100
"""
    return _model.generate_content(prompt).text


def _run_bear(data: MarketData, score: ScoreResult) -> str:
    prompt = f"""You are a bear analyst. Make the strongest case AGAINST this stock.
Use concrete data. Do not mention positives.

Ticker: {data.ticker}
Score: {score.total:.1f}/100
"""
    return _model.generate_content(prompt).text


def _run_judge(data: MarketData, score: ScoreResult, bull: str, bear: str) -> str:
    prompt = f"""You have read the bull and bear cases. Synthesize them into a verdict.
State conviction level (high/medium/low) and the single most important factor.

Bull case: {bull}
Bear case: {bear}
Score: {score.total:.1f}/100
"""
    return _model.generate_content(prompt).text
