import streamlit as st

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Chatbot")
st.write("Welcome! How can I help you today?")
st.info("You can chat in English or Roman Urdu.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# FAQ selected message
if "pending_message" not in st.session_state:
    st.session_state.pending_message = None


def get_response(message):
    msg = message.lower()

    # Greeting
    if any(word in msg for word in ["hello", "hi", "hey", "salam", "assalam"]):
        return (
            "Hello! 👋 Welcome to our customer support. "
            "How can I help you?\n\n"
            "Roman Urdu: Assalam o Alaikum! 👋 Main aapki kis tarah madad kar sakta hoon?"
        )

    # Price
    elif any(word in msg for word in ["price", "cost", "rate", "qeemat"]):
        return (
            "💰 Please tell me which product you want the price of.\n\n"
            "Roman Urdu: Bata dein aap kis product ki price maloom karna chahte hain."
        )

    # Order
    elif any(word in msg for word in ["order", "mera order", "order kahan"]):
        return (
            "📦 Please provide your order number for order status.\n\n"
            "Roman Urdu: Apna order number bhej dein, main order status check karne mein madad karunga."
        )

    # Delivery
    elif any(word in msg for word in ["delivery", "deliver", "kab ayega", "kab aayega"]):
        return (
            "🚚 Delivery usually takes 3–5 business days.\n\n"
            "Roman Urdu: Delivery aam tor par 3–5 working days leti hai."
        )

    # Refund / Return
    elif any(word in msg for word in ["refund", "return", "wapis", "wapas"]):
        return (
            "🔄 Please provide your order number to request a return or refund.\n\n"
            "Roman Urdu: Return ya refund ke liye apna order number bhej dein."
        )

    # Support
    elif any(word in msg for word in ["support", "help", "madad"]):
        return (
            "📞 Our customer support team is here to help you.\n\n"
            "Roman Urdu: Hamari customer support team aapki madad ke liye mojood hai."
        )

    # Thank you
    elif any(word in msg for word in ["thank you", "thanks", "shukriya"]):
        return (
            "You're welcome! 😊\n\n"
            "Roman Urdu: Khushi hui aapki madad karke!"
        )

    # Goodbye
    elif any(word in msg for word in ["bye", "goodbye", "allah hafiz"]):
        return (
            "Goodbye! 👋 Have a great day!\n\n"
            "Roman Urdu: Allah Hafiz! 👋 Aapka din acha guzray."
        )

    else:
        return (
            "Sorry, I don't understand your question yet. "
            "Please choose one of the FAQ options below.\n\n"
            "Roman Urdu: Maaf kijiye, mujhe aapka sawal samajh nahi aya. "
            "Neeche diye gaye FAQ options mein se koi option select karein."
        )


# FAQ Section
st.write("### ❓ Frequently Asked Questions")

col1, col2 = st.columns(2)

with col1:
    if st.button("💰 Product Price"):
        st.session_state.pending_message = "What is the product price?"
        st.rerun()

    if st.button("📦 Order Status"):
        st.session_state.pending_message = "Where is my order?"
        st.rerun()

    if st.button("🔄 Return / Refund"):
        st.session_state.pending_message = "I want a refund"
        st.rerun()

with col2:
    if st.button("🚚 Delivery"):
        st.session_state.pending_message = "When will my delivery arrive?"
        st.rerun()

    if st.button("📞 Customer Support"):
        st.session_state.pending_message = "I need customer support"
        st.rerun()


# Show old messages
for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])


# Chat input
message = st.chat_input("Type your message...")

if st.session_state.pending_message:
    message = st.session_state.pending_message
    st.session_state.pending_message = None

if message:
    st.session_state.messages.append(
        {"role": "user", "content": message}
    )

    response = get_response(message)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
