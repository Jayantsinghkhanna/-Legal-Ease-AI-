import time


class MetricsTracker:

    def __init__(self):

        self.retrieval_time = 0
        self.rerank_time = 0
        self.llm_time = 0
        self.total_time = 0

    def start(self):

        self.start_time = time.time()

    def stop(self):

        self.total_time = round(
            time.time() - self.start_time,
            3
        )

    def set_retrieval_time(
        self,
        value
    ):
        self.retrieval_time = round(
            value,
            3
        )

    def set_rerank_time(
        self,
        value
    ):
        self.rerank_time = round(
            value,
            3
        )

    def set_llm_time(
        self,
        value
    ):
        self.llm_time = round(
            value,
            3
        )

    def get_metrics(self):

        return {

            "retrieval_time":
                self.retrieval_time,

            "rerank_time":
                self.rerank_time,

            "llm_time":
                self.llm_time,

            "total_time":
                self.total_time
        }