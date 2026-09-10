
import streamlit as st

st.title("🤖 AI Customer Support Chatbot")

st.write("Welcome! How can I help you?")

message = st.text_input("Enter your message:")

if message:
    st.write("Bot: Thank you for your message. How can I help you?")
