from app.models.gemini import cargar_llm


def main():

    llm = cargar_llm()

    respuesta = llm.invoke(
        "Explica qué es Retrieval Augmented Generation en una frase."
    )

    print(respuesta.content)


if __name__ == "__main__":
    main()