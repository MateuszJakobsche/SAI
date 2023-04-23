# SAI
A simple implementation of chatGPT, based on this [post](https://levelup.gitconnected.com/its-time-to-create-a-private-chatgpt-for-yourself-today-6503649e7bb6)

Installation guide
1)  install [Python](https://www.python.org/downloads/)
2)  install [Pip](https://pip.pypa.io/en/stable/installation/)
3)  install packages using Pip: [Openai](https://github.com/openai/openai-python), [Streamlit](https://docs.streamlit.io/)
4)  set values in config.py: [API key](https://platform.openai.com/account/api-keys) is required for connection to OpenAI API; USER name is Your displayed name, SAI name is Bot's name; SAI identity is the input you may provide before chatting, i.e. to modify memory or personality of SAI.
5)  deploy with command: py -m streamlit run aibot.py

Future plans:
- saving settings and chat history locally;
- tabs allowing for multiple conversations;
