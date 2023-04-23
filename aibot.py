import openai
import streamlit as st
from config import APIkey, USERname, SAIname, SAIidentity

st.set_page_config(
        page_title="SAI",
        page_icon=":trident:",
        menu_items={
         'About': 'Github repo: https://github.com/MateuszJakobsche/SAI'
     }
    )

#functions
def initialize_session():
    if 'prompts' not in st.session_state:
        st.session_state['prompts'] = [{"role": "system", "content": saiIdentity}]
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

def restore_session():
    del st.session_state['prompts']
    del st.session_state['generated']
    del st.session_state['past']
    initialize_session()

def generate_response(prompt):
    st.session_state['prompts'].append({"role": "user", "content":prompt})
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = st.session_state['prompts']
    )
    message = completion.choices[0].message.content
    return message

def send_click():
    if st.session_state['user']!= '':
        chat_input = st.session_state['user']
        chat_output= generate_response(chat_input)
        st.session_state['past'].append(chat_input)
        st.session_state['generated'].append(chat_output)
        st.session_state['prompts'].append({"role": "assistant", "content": chat_output})
        st.session_state['user'] = ""

#configuration menu
with st.sidebar:
    openai.api_key = st.text_input("Your API key*", value=APIkey, type="password")
    st.divider()
    userName = st.text_input("Your name", value=USERname) + ": "
    saiName = st.text_input("SAI's name", value=SAIname) + ": "
    st.divider()
    saiIdentity = st.text_area("SAI's identity", value=SAIidentity)
    st.button("restore identity", on_click=restore_session)

initialize_session()

#chat content
user_input=st.text_input("enter message", key="user", label_visibility="collapsed", on_change=send_click)
with st.container():
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            query = st.session_state['past'][i]
            if len(query) > 50:
                query = query[:50] + "(...)"

            with st.expander(userName + query, expanded=1):
                st.divider()
                st.markdown(saiName + st.session_state['generated'][i])