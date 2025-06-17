import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv(override=True)
OPENAI_KEY = os.getenv("API_KEY")

chat = ChatOpenAI(
    model_name="gpt-4o-mini",
    openai_api_key=OPENAI_KEY,
    temperature=0.3
)

st.set_page_config(page_title="Gerador BDD", page_icon="🧪")
st.title("🧪 Gerador de Casos de Teste BDD")

funcionalidade = st.text_input("🔧 Funcionalidade a ser testada")
tipo_usuario = st.selectbox("👤 Tipo de usuário", ["Administrador", "Usuário comum", "Visitante", "Cliente logado"])
objetivo = st.text_input("🎯 O que o teste deve validar?")
contexto = st.text_area("📄 Contexto adicional (opcional)", placeholder="Ex: O usuário deve estar logado no sistema...")


