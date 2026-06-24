from sentence_transformers import (
    CrossEncoder
)


class LegalReranker:

    def __init__(self):

        self.model = (
            CrossEncoder(
                "cross-encoder/ms-marco-MiniLM-L-6-v2"
            )
        )

    def rerank(
        self,
        query,
        documents,
        top_k=5
    ):

        pairs = []

        for doc in documents:

            text = getattr(
                doc,
                "page_content",
                doc.content
            )

            pairs.append(
                (
                    query,
                    text
                )
            )

        scores = (
            self.model.predict(
                pairs
            )
        )

        ranked = sorted(

            zip(
                documents,
                scores
            ),

            key=lambda x: x[1],

            reverse=True
        )

        return [

            item[0]

            for item in ranked[:top_k]
        ]