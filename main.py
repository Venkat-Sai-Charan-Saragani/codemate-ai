import streamlit as st
from streamlit import session_state

from assistant import get_response

st.set_page_config(
    page_title="AI CODING ASSISTANT",
    page_icon="💻",
    layout="wide"
)

st.title("💻 CodeMate AI")
st.caption("Your Personal AI Coding Assistant")
st.divider()
st.caption("POWERDED BY GROQ")

if "messages" not in session_state:
    st.session_state.messages = []

#Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(" Ask me anything about programming.....")


if prompt:
    st.session_state.messages.append(
        {
            "role" : "user",
            "content": prompt,
        }
    )
    with st.chat_message("user",avatar="👨"):
        st.markdown(prompt)

    with st.chat_message("assistant",avatar="🤖"):
        with st.spinner("Thinking..."):
            response = get_response(st.session_state.messages)
            st.markdown(response)
    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content": response,
        }
    )

if not st.session_state.messages:
    st.info("""
👋 Welcome!

I can help you with:

- 🐍 Python
- ☕ Java
- 💻 C++
- 🌐 JavaScript
- 🐞 Debugging
- 📖 Code Explanation
- ⚡ Optimization
""")

with st.sidebar:
    st.title("Options")

    if st.button("clear chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.write("Model")

    st.code("llama-3.3-70b-versatile")

    st.markdown("---")

    st.write("Built with")

    st.write("• Streamlit")
    st.write("• Groq API")
    st.write("• Llama 3.3 70B")