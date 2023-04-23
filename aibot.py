import openai
import streamlit as st
from streamlit_chat import message
from config import APIkey, USERname, AIname, AIidentity

#functions
def generate_response(prompt):
    st.session_state['prompts'].append({"role": "user", "content":prompt})
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = st.session_state['prompts']
    )
    message= completion.choices[0].message.content
    return message
def send_click():
    if st.session_state['user']!= '':
        chat_input = USERname + st.session_state['user']
        chat_output= generate_response(chat_input)
        st.session_state['past'].append(chat_input)
        st.session_state['generated'].append(chat_output)
        st.session_state['prompts'].append({"role": "assistant", "content": chat_output})
        st.session_state['user'] = ""

#initialization
openai.api_key = APIkey
if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [{"role": "system", "content": AIidentity}]
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

#content
user_input=st.text_input("enter message", key="user", label_visibility="collapsed", on_change=send_click)
with st.container():
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.divider()
            st.markdown(st.session_state['past'][i])
            st.markdown(AIname + st.session_state['generated'][i])