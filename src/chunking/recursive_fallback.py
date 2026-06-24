from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def split_large_clause(
    text,
    chunk_size=1200,
    overlap=200
):

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )
    )

    return splitter.split_text(text)