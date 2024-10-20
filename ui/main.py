import requests
import streamlit as st

URL = "http://127.0.0.1:8080/"

st.title("Izba AI")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        # Append user input to chat history
        st.session_state['chat_history'].append({"role": "user", "content": user_input})
        # Generate a response from the chatbot
        # orchestrator_response = requests.get(URL+f"/orchestrator/{user_input}").json()["llm_response"]
        # if orchestrator_response == "out-of-scope":
        #     st.session_state['chat_history'].append({"role": "assistant", "content": "Unfortunately, I'm not currently capable of answering this question. Do you have any other questions about UK properties?"})
        # else:
        #     tool_response = requests.get(URL+f"{orchestrator_response}").json()["llm_response"]
        #     st.session_state['chat_history'].append({"role": "assistant", "content": tool_response})

        llm_response = requests.get(URL+f"/llama_index_agent/{user_input}").json()
        st.session_state['chat_history'].append({"role": "assistant", "content": llm_response})

# Display chat history
for chat in st.session_state['chat_history']:
    if chat['role'] == 'user':
        st.write(f"You: {chat['content']}")
    else:
        st.write(f"Domovenok: {chat['content']}")