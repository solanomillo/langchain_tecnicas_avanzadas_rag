from app.chains.query_rewriter import crear_query_rewriter
from app.loaders.pdf_loader import (
    cargar_documentos
)

from app.processing.chunking import (
    crear_chunks
)

from app.processing.embeddings import (
    cargar_embeddings
)

from app.vectorstores.faiss_store import (
    crear_vectorstore
)

from app.retrievers.retriever import (
    crear_retriever
)

from app.models.gemini import (
    cargar_llm
)

from app.models.cohere_model import (
    obtener_llm_cohere
)

from app.chains.rag_chain import (
    crear_rag_chain
)
from langchain_classic.globals import ( set_debug )

set_debug(True)


def main():

    documentos = cargar_documentos()

    chunks = crear_chunks(
        documentos
    )

    embeddings = cargar_embeddings()

    vectorstore = crear_vectorstore(
        chunks,
        embeddings
    )

    retriever = crear_retriever(
        vectorstore
    )

    llm = cargar_llm()
    llm_optimizador =  obtener_llm_cohere()

    rewriter = crear_query_rewriter(
        llm_optimizador
    )

    rag_chain = crear_rag_chain(
        rewriter,
        retriever,
        llm
    )
    pregunta = (
        "¿Cómo saco el seguro?"
    )

    respuesta = rag_chain.invoke(
        pregunta
    )

    print("\nRESPUESTA:\n")

    print(respuesta)


if __name__ == "__main__":
    main()