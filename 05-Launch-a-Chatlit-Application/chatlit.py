import os
import sys
import datetime
import openai
import dotenv
import streamlit as st
from pathlib import Path
import requests
import json

# import API key from secrets.env file
env_path = Path('.') / 'secrets.env'
dotenv.load_dotenv(dotenv_path=env_path)
openai.api_key =  os.environ.get("AZURE_OPENAI_API_KEY")
openai.api_base =  os.environ.get("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2023-11-01"
chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
 
if "openai_model" not in st.session_state:
   #Hint: This line of code is used in st.session_state Streamlit applications for maintaining session states.
 
if "messages" not in st.session_state:
   #Hint: This line of code is initializing st.session_state.messages to an empty list
 
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
       st.markdown(message["content"])
 
if prompt := st.chat_input("What is up?"):
   #Hint: This line of code appends a new message to the 'messages' list in the session state. A message is a dictionary with two keys: 'role' and 'content'
   with st.chat_message("user"):
       st.markdown(prompt)
 
   with st.chat_message("assistant"):
       message_placeholder = st.empty()
       full_response = ""
       for response in openai.ChatCompletion.create(
           deployment_id=st.session_state["openai_model"],
           messages=[
              #Hint: This is a list comprehension in Python that generates a new list of dictionaries from st.session_state.messages. # Each dictionary in the new list has two keys: role and content.
           ],
           stream=True,
       ):
           if len(response.choices)>0:
 
               full_response += response.choices[0].delta.get("content", "")
               message_placeholder.markdown(full_response + "▌")
       message_placeholder.markdown(full_response)
   st.session_state.messages.append({"role": "assistant", "content": full_response})
