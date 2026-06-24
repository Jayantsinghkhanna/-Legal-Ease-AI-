def build_metadata(
    section_name,
    page_number,
    content,
    document_name="contract.pdf",
    chunk_type="clause",
    clause_type=None
):

    return {

        "section": section_name,

        "page": page_number,

        "length": len(content),

        "document_name": document_name,

        "chunk_type": chunk_type,

        "clause_type": clause_type
    }