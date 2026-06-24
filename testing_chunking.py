from src.ingestion.pdf_loader import load_pdf
from src.ingestion.legal_parser import extract_sections

from src.chunking.clause_chunker import (
    LegalClauseChunker
)

pages = load_pdf(
    "sample.pdf"
)

chunker = LegalClauseChunker()

for page in pages:

    sections = extract_sections(
        page["text"]
    )

    chunks = chunker.chunk_sections(
        sections,
        page["page_number"]
    )

    print(chunks)