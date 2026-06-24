from typing import List

from pydantic import BaseModel


class LegalFact(BaseModel):

    party: str

    obligation: str

    clause_type: str

    deadline: str | None = None


class LegalKnowledge(BaseModel):

    facts: List[LegalFact]