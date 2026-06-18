import streamlit as st

from app.services.rag_service import (
    inicializar_rag
)

st.set_page_config(
    page_title="RRAG Avanzado con Langchain",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def cargar_rag():

    return inicializar_rag()


rag_chain = cargar_rag()

st.title(
    "RAG Avanzado con Langchain"
)

pregunta = st.chat_input(
    "Haz una pregunta"
)

if pregunta:

    st.chat_message(
        "user"
    ).write(
        pregunta
    )

    with st.spinner(
        "Consultando documentos..."
    ):

        respuesta = (
            rag_chain.invoke(
                pregunta
            )
        )

    st.chat_message(
        "assistant"
    ).write(
        respuesta
    )