import streamlit as st
import re

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

# Show previous messages
for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# Chat input
message = st.chat_input(
    "Type your message..."
)

if message:
    msg = message.lower().strip()

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": message
    })

    # Greeting
    if re.search(r"\b(hello|hi|hey)\b", msg) or any(x in msg for x in [
        "salam", "assalam", "aoa", "kya haal",
        "kaise ho", "kaisay ho", "kese ho"
    ]):
        response = (
            "Hello! 👋 Welcome to our customer support. "
            "How can I help you?\n\n"
            "Assalam o Alaikum! 👋 Main aap ki kaise madad kar sakta hoon?"
        )

    # Price
    elif any(x in msg for x in [
        "price", "cost", "rate", "qeemat",
        "kitne", "kitni", "paisa", "paise", "daam"
    ]):
        response = (
            "💰 Please tell me the product name and I will help "
            "you with its price.\n\n"
            "💰 Product ka naam batayein, main aap ko us ki price "
            "ke baare mein bataunga."
        )

    # Order
    elif any(x in msg for x in [
        "order", "tracking", "mera order",
        "apna order", "order kahan", "order kidhar"
    ]):
        response = (
            "📦 Please provide your order number for order status.\n\n"
            "📦 Apna order number batayein taake hum order ka "
            "status check kar saken."
        )

    # Delivery
    elif any(x in msg for x in [
        "delivery", "shipping", "deliver",
        "delivery kab", "kab ayegi", "kab ayega",
        "kitne din", "kitnay din"
    ]):
        response = (
            "🚚 Please provide your order number or location "
            "for delivery information.\n\n"
            "🚚 Delivery ki maloomat ke liye apna order number "
            "ya location batayein."
        )

    # Return / Refund
    elif any(x in msg for x in [
        "return", "refund", "exchange",
        "wapas", "paise wapas",
        "refund chahiye", "return karna"
    ]):
        response = (
            "🔄 For a return, refund, or exchange, please provide "
            "your order number and the reason.\n\n"
            "🔄 Return, refund ya exchange ke liye apna order "
            "number aur wajah batayein."
        )

    # Support
    elif any(x in msg for x in [
        "contact", "support", "agent",
        "representative", "madad",
        "help chahiye", "customer care"
    ]):
        response = (
            "📞 Please tell me your problem and order number.\n\n"
            "📞 Apna masla aur order number batayein. "
            "Hamari support team aap ki madad karegi."
        )

    # Thank you
    elif any(x in msg for x in [
        "thank", "thanks", "shukriya",
        "bohat shukriya"
    ]):
        response = (
            "You're welcome! 😊 Is there anything else I can help you with?\n\n"
            "Khush aamdeed! 😊 Kya main aap ki mazeed koi madad kar sakta hoon?"
        )

    # Goodbye
    elif any(x in msg for x in [
        "bye", "goodbye", "allah hafiz", "khuda hafiz"
    ]):
        response = (
            "Goodbye! 👋 Have a great day!\n\n"
            "Allah Hafiz! 👋 Aap ka din acha guzray."
        )

    # Unknown
    else:
        response = (
            "Sorry, I didn't understand that. 🤔\n\n"
            "You can ask about:\n"
            "• Product Price 💰\n"
            "• Order Status 📦\n"
            "• Delivery 🚚\n"
            "• Return / Refund 🔄\n"
            "• Customer Support 📞\n\n"
            "Maazrat, main aap ka sawal samajh nahi saka."
        )

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Refresh screen
    st.rerun()

    st.write("### 🤖 Bot Response")
    st.success(response)
