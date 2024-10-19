import streamlit as st

st.title("Chatbot Demo")

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
        # chatbot_response = generate_response(user_input)
        st.session_state['chat_history'].append({"role": "assistant", "content": user_input})

# Display chat history
for chat in st.session_state['chat_history']:
    if chat['role'] == 'user':
        st.write(f"You: {chat['content']}")
    else:
        st.write(f"Bot: {chat['content']}")
