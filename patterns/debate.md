# Multi-Agent Debate Pattern

Used when a decision benefits from adversarial analysis — the goal is to surface blind spots and prevent the AI from anchoring on a single narrative.

## Agents

```
BullAgent    → builds the strongest case FOR
BearAgent    → builds the strongest case AGAINST
SkepticAgent → challenges both, surfaces hidden assumptions
JudgeAgent   → synthesizes all three into a final verdict
```

## Execution Order

```
data + score
    │
    ├─ BullAgent    ──────────────┐
    ├─ BearAgent    ──────────────┤  (can run in parallel)
    │                             │
    └─ SkepticAgent ──────────────┤
                                  ▼
                            JudgeAgent
                                  │
                                  ▼
                           AnalysisResult
```

Bull, Bear, and Skeptic can run in parallel since none depends on the others. The Judge receives all three outputs and runs last.

## Prompt Design

Each agent gets a **role constraint** that prevents hedging:

```
BullAgent system prompt:
"You are a bull analyst. Your job is to make the strongest possible case
FOR investing in this stock. Do not hedge. Do not mention risks — that is
the bear's job. Use only concrete data from the inputs provided."

BearAgent system prompt:
"You are a bear analyst. Your job is to make the strongest possible case
AGAINST investing in this stock. Do not hedge. Do not mention positives —
that is the bull's job. Use only concrete data from the inputs provided."

SkepticAgent system prompt:
"You have read the bull and bear cases. Your job is to challenge both.
What assumptions are each making? What data are they ignoring? What would
change your view on either case?"

JudgeAgent system prompt:
"You have read the bull case, the bear case, and the skeptic's challenges.
Synthesize them into a final verdict. State your conviction level (high /
medium / low) and the single most important factor driving your conclusion."
```

## Output Structure

```python
@dataclass
class DebateResult:
    bull_case: str
    bear_case: str
    skeptic_challenges: str
    verdict: str
    conviction: Literal["high", "medium", "low"]
    key_factor: str
    bear_return: float   # p10 historical or AI estimate
    base_return: float   # p50
    bull_return: float   # p90
    downside_probability: float  # P(return < -20%)
```

## When to Use

Use the debate pattern when:
- The output is a recommendation or prediction (not just analysis)
- The cost of a wrong answer is high
- You want the report to show both sides

Use a single analyst agent when:
- The task is summarization or extraction, not judgment
- Speed matters more than adversarial rigor
