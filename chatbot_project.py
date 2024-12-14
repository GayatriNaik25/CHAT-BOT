import nltk
from nltk.chat.util import Chat, reflections
import streamlit as st
import base64
from PIL import Image

# NLTK Data Download
nltk.download('punkt')

# Define the conversation pairs
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you",]
    ],
    [
        r"(.*) your name ?",
        ["My name is CleverBot, but you can just call me robot and I'm a chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Prakash created me using Python's NLTK library.", "Top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health.",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach you']
    ],
]

# Chatbot setup
chat = Chat(pairs, reflections)

# Streamlit App
st.title("Chat with CleverBot 🤖")

# Function to set a background image and sidebar color
def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        encoded_image = base64.b64encode(data).decode()

    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    section[data-testid="stSidebar"] {{
        background-color: #1e1e1e;
        color: white;
    }}
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white;
    }}
    .stButton > button {{
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }}
    .stButton > button:hover {{
        background-color: #45a049;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(r"C:\Users\new\Pictures\images (5).jpg")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input from the user
st.subheader("Chat with me!")

user_input = st.text_input("Type your message here:")

# Process the conversation
if user_input:
    if user_input.lower() == "quit":
        st.write("CleverBot: Bye for now. See you soon! 😊")
        st.stop()
    response = chat.respond(user_input)
    # Append conversation to history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("CleverBot", response))

# Display the conversation history
if st.session_state.history:
    st.write("---")
    for sender, message in st.session_state.history:
        avatar = "👤" if sender == "You" else "🤖"
        st.markdown(f"**{avatar} {sender}:** {message}")

# Footer message
st.markdown("<br><i>Type 'quit' to end the conversation.</i>", unsafe_allow_html=True)
