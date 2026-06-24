from langchain_community.vectorstores import (
    FAISS
)


class FAISSStore:

    def __init__(
        self,
        embeddings
    ):

        self.embeddings = embeddings

    def create_index(
        self,
        chunks
    ):

        texts = [
            chunk.content
            for chunk in chunks
        ]

        metadatas = [
            {
        "section": chunk.section,
        "page": chunk.page,
        "chunk_type": chunk.chunk_type,
        "document_name": chunk.document_name
           }
            for chunk in chunks
        ]

        vectorstore = (
            FAISS.from_texts(
                texts,
                self.embeddings,
                metadatas=metadatas
            )
        )

        return vectorstore