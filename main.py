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

    print(
        f"VectorStore creado con {len(chunks)} chunks"
    )

    resultados = vectorstore.similarity_search(
    "¿Cómo solicitar el seguro?",
    k=3
    )

    for i, doc in enumerate(resultados, start=1):

        print("\n")
        print("=" * 50)
        print(f"Resultado {i}")
        print("=" * 50)

        print(
            doc.page_content[:400]
        )

if __name__ == "__main__":
    main()