import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv(override=True)
OPENAI_KEY = os.getenv("API_KEY")

