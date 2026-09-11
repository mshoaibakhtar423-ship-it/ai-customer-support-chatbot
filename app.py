import streamlit as st

st.set_page_config(page_title="AI Customer Support Chatbot")

st.title("🤖 AI Customer Support Chatbot")
st.write("Welcome! How can I help you?")

message = st.text_input("Enter your message:")

if message:
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        response = "Hello! Welcome to our customer support. How can I help you?"
    elif "price" in msg or "cost" in msg:
        response = "Please tell me which product you are interested in, and I will help you with the price."
    elif "order" in msg:
        response = "Sure! Please provide your order number so we can help you."
    elif "delivery" in msg or "shipping" in msg:
        response = "Our team can help you with delivery information. Please provide your order number."
    elif "thank" in msg:
        response = "You're welcome! 😊 Is there anything else I can help you with?"
    else:
        response = "Thank you for your message. Our customer support team will be happy to help you."

    st.write("*Bot:*", response)
