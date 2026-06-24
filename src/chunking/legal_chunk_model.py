from pydantic import BaseModel


class LegalChunk(BaseModel):

    content: str

    section: str

    page: int

    chunk_type: str

    document_name: str

    clause_type: str | None = None

    importance_score: float = 0.0