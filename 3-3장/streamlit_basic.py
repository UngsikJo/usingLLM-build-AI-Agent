import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv('OPENAI_API_KEY')

    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/stramlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in Github Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot with Streamlit and OpenAI API")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API ket to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-5-nano", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)