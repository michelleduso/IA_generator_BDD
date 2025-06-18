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

template_prompt = '''
Você é um analista de testes especializado em BDD.

Gere cenários de teste com base nas informações abaixo:

Funcionalidade: {funcionalidade}
Tipo de usuário: {tipo_usuario}
Objetivo: {objetivo}
Contexto adicional: {contexto}

Regras para o formato dos testes:
- Utilize palavras-chave do Gherkin em INGLÊS: Given, When, Then, And, But
- O restante da frase deve estar em PORTUGUÊS.
- Crie de 2 a 3 cenários claros e bem estruturados
- Formato de saída: puro Gherkin, sem explicações adicionais

Exemplo de como devem começar os passos:
Given que o usuário acessa a página de login  
And o usuário preenche o campo "e-mail"  
When o usuário clica em "Entrar"  
Then o sistema deve exibir...

Gere agora os cenários:
'''

prompt = PromptTemplate.from_template(template_prompt)
