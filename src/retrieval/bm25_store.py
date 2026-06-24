from rank_bm25 import BM25Okapi


class BM25Store:

    def __init__(
        self,
        chunks
    ):

        self.chunks = chunks

        tokenized_docs = [

            chunk.content.split()

            for chunk in chunks
        ]

        self.bm25 = (
            BM25Okapi(
                tokenized_docs
            )
        )

    def search(
        self,
        query,
        top_k=5
    ):

        tokenized_query = (
            query.split()
        )

        scores = (
            self.bm25.get_scores(
                tokenized_query
            )
        )

        ranked = sorted(

            zip(
                self.chunks,
                scores
            ),

            key=lambda x: x[1],

            reverse=True
        )

        return [

            item[0]

            for item in ranked[:top_k]
        ]