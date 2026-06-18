import streamlit as st

from app.services.rag_service import (
    inicializar_rag
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

    respuesta = rag_chain.invoke(
        pregunta
    )

    st.write(
        respuesta
    )