import re

from src.chunking.legal_chunk_model import (
    LegalChunk
)

from src.chunking.recursive_fallback import (
    split_large_clause
)


class LegalClauseChunker:

    def __init__(
        self,
        max_clause_size=3000
    ):

        self.max_clause_size = (
            max_clause_size
        )

    def chunk_sections(
    self,
    sections,
    page_number,
    document_name
    ):

        chunks = []

        for section in sections:

            section_title = (
                section["section"]
            )

            content = (
                section["content"]
            )

            if (
                len(content)
                < self.max_clause_size
            ):

                chunks.append(

                    LegalChunk(

                        content=content,

                        section=section_title,

                        page=page_number,

                        chunk_type="clause",

                        document_name=document_name
                    )
                )

            else:

                smaller_chunks = (
                    split_large_clause(
                        content
                    )
                )

                for chunk in smaller_chunks:

                    chunks.append(

                        LegalChunk(

                            content=chunk,

                            section=section_title,

                            page=page_number,

                            chunk_type="recursive",

                            document_name=document_name
                        )
                    )

        return chunks