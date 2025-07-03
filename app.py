import streamlit as st
from caption_generator import generate_caption
from deep_translator import GoogleTranslator
import tempfile
import os

st.set_page_config(page_title="CaptionCrafter", page_icon="📸", layout="centered")
st.title("📸 CaptionCrafter")
st.write("Turn your images into Instagram-worthy captions ✨")

# Upload area
uploaded_file = st.file_uploader("Drag and drop an image or click to upload", type=["jpg", "jpeg", "png"])

# Session state for caption history
if "captions" not in st.session_state:
    st.session_state["captions"] = []

# Language selector
lang = st.selectbox("🌍 Translate caption to", ["None", "Tamil", "Hindi", "French", "German", "Spanish", "Japanese"])

# Generate button
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    if st.button("✨ Generate Caption"):
        caption = generate_caption(image_path)
        st.session_state["captions"].append(caption)

    if st.session_state["captions"]:
        latest_caption = st.session_state["captions"][-1]

        if lang != "None":
            try:
                translated = GoogleTranslator(source='auto', target=lang.lower()).translate(latest_caption)
                st.success(f"**Translated Caption ({lang})**: {translated}")
            except Exception as e:
                st.error("Translation failed. Try another language.")
        else:
            st.success(f"**Caption**: {latest_caption}")
