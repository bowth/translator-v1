import streamlit as st
from googletrans import Translator, LANGUAGES

# Set default background color to white
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define Streamlit app layout and widgets
st.title("Language Translator")

# Sidebar
st.sidebar.header("Language Settings")

source_language = st.sidebar.selectbox("Select source language:", LANGUAGES.values())
target_language = st.sidebar.selectbox("Select target language:", LANGUAGES.values())

# Main content
input_text = st.text_area("Enter text to translate:", height=300)
translate_button = st.button("Translate")

if translate_button:
    if input_text:
        translator = Translator()
        translated_text = translator.translate(input_text, src=source_language, dest=target_language).text
        col1, col2 = st.columns(2)
        with col1:
            st.text_area("Input Text:", value=input_text, height=300)
        with col2:
            st.text_area("Translated Text:", value=translated_text, height=300)

# Hide Streamlit hamburger menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
