import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class LegalLLM:

    def __init__(
        self,
        temperature=0.2
    ):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=temperature
        )

    def get_llm(self):
        return self.llm