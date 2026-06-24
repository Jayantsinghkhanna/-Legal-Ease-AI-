import json

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from src.evaluation.evaluation_models import (
    EvaluationResult
)


class RAGEvaluator:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            MODEL = "gemini-2.5-flash",
            temperature=0
        )

    def evaluate(
        self,
        question,
        answer,
        retrieved_context
    ):

        prompt = f"""
You are an expert evaluator for RAG systems.

Evaluate whether the answer is supported by the retrieved context.

Question:
{question}

Answer:
{answer}

Retrieved Context:
{retrieved_context}

Return ONLY JSON.

Schema:

{{
    "faithfulness_score": 0,
    "citation_score": 0,
    "explanation": ""
}}

Scoring:

Faithfulness:
0-10

Citation Score:
0-10

10 = fully supported
0 = hallucinated
"""

        response = self.llm.invoke(
            prompt
        )

        cleaned = (
            response.content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            data = json.loads(
                cleaned
            )

            return EvaluationResult(
                **data
            )

        except Exception:

            return EvaluationResult(
                faithfulness_score=0,
                citation_score=0,
                explanation="Evaluation Failed"
            )