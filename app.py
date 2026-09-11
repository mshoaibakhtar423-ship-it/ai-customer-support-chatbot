import streamlit as st

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Chatbot")
st.write("Welcome! How can I help you today?")

message = st.text_input("Enter your message:")

if message:
    msg = message.lower().strip()

    # Greeting
    if any(word in msg for word in ["hello", "hi", "hey"]):
        response = (
            "Hello! 👋 Welcome to our customer support. "
            "How can I help you?"
        )

    # Product Price
    elif any(word in msg for word in ["price", "cost", "rate"]):
        response = (
            "💰 Please tell me the product name, "
            "and I will help you with its price."
        )

    # Order
    elif any(word in msg for word in ["order", "tracking", "order status"]):
        response = (
            "📦 Please provide your order number "
            "so we can help you with your order status."
        )

    # Delivery
    elif any(word in msg for word in ["delivery", "shipping", "deliver"]):
        response = (
            "🚚 Please provide your order number or location "
            "for delivery information."
        )

    # Return / Refund
    elif any(word in msg for word in ["return", "refund", "exchange"]):
        response = (
            "🔄 For a return, refund, or exchange, "
            "please provide your order number and the reason."
        )

    # Contact Support
    elif any(word in msg for word in [
        "contact", "support", "agent", "representative"
    ]):
        response = (
            "📞 Please tell me your problem and order number. "
            "Our support team will help you."
        )

    # Thank You
    elif any(word in msg for word in ["thank", "thanks"]):
        response = (
            "You're welcome! 😊 "
            "Is there anything else I can help you with?"
        )

    # Goodbye
    elif any(word in msg for word in ["bye", "goodbye"]):
        response = (
            "Goodbye! 👋 Have a great day!"
        )

    # Unknown Question
    else:
        response = (
            "I can help you with:\n\n"
            "• Product Price 💰\n"
            "• Order Status 📦\n"
            "• Delivery 🚚\n"
            "• Return / Refund 🔄\n"
            "• Customer Support 📞"
        )

    st.write("### 🤖 Bot Response")
    st.write(response)
