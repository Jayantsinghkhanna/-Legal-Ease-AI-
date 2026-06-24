from pydantic import BaseModel


class EvaluationResult(BaseModel):

    faithfulness_score: float

    citation_score: float

    explanation: str