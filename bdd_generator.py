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

