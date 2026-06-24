from langchain_core.documents import Document


class HybridRetriever:

    def __init__(
        self,
        vectorstore,
        bm25_store
    ):
        self.vectorstore = vectorstore
        self.bm25_store = bm25_store

    def retrieve(
        self,
        query,
        k=10
    ):

        semantic_docs = (
            self.vectorstore.similarity_search(
                query,
                k=k
            )
        )

        keyword_docs = (
            self.bm25_store.search(
                query,
                top_k=k
            )
        )

        scores = {}

        # FAISS Results
        for rank, doc in enumerate(
            semantic_docs
        ):

            content = doc.page_content

            scores.setdefault(
                content,
                {
                    "doc": doc,
                    "score": 0
                }
            )

            scores[content]["score"] += (
                1 / (60 + rank)
            )

        # BM25 Results
        for rank, doc in enumerate(
            keyword_docs
        ):

            content = getattr(
                doc,
                "page_content",
                doc.content
            )

            scores.setdefault(
                content,
                {
                    "doc": doc,
                    "score": 0
                }
            )

            scores[content]["score"] += (
                1 / (60 + rank)
            )

        ranked = sorted(
            scores.values(),
            key=lambda x: x["score"],
            reverse=True
        )

        final_docs = []

        for item in ranked[:k]:

            doc = item["doc"]

            # FAISS Document
            if hasattr(doc, "page_content"):

                final_docs.append(doc)

            # LegalChunk -> Convert to LangChain Document
            else:

                final_docs.append(
                    Document(
                        page_content=doc.content,
                        metadata={
                            "page": doc.page,
                            "section": doc.section,
                            "document_name": doc.document_name,
                            "chunk_type": doc.chunk_type
                        }
                    )
                )

        return final_docs