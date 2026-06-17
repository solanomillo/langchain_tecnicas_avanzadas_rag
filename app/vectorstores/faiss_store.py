from langchain_community.vectorstores import (
    FAISS
)


def crear_vectorstore(
    chunks,
    embeddings
):

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore