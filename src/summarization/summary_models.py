from typing import List

from pydantic import BaseModel


class KeyClause(BaseModel):
    clause_name: str
    summary: str


class ImportantDate(BaseModel):
    event: str
    date: str


class RiskItem(BaseModel):
    severity: str
    issue: str


class ContractSummary(BaseModel):

    contract_type: str

    parties: List[str]

    jurisdiction: str

    executive_summary: str

    key_clauses: List[KeyClause]

    important_dates: List[ImportantDate]


class RiskAssessment(BaseModel):

    risk_score: float

    risks: List[RiskItem]


class ContractStats(BaseModel):

    pages: int

    chunks: int

    sections: int    

