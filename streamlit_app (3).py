import streamlit as st
from finance_agent import get_finance_answer

st.set_page_config(page_title="Finance Chatbot", page_icon="💹")

st.title("💬 Finance Assistant")
st.write("Ask me anything about finance, stocks, or investments!")

# Chat UI
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Enter your finance question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get finance answer
    with st.spinner("Analyzing finance data..."):
        answer = get_finance_answer(user_input)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
