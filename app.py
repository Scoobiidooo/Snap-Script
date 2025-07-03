import streamlit as st
from caption_generator import generate_caption
from deep_translator import GoogleTranslator
from PIL import Image
import io

st.set_page_config(page_title="AI Image Caption Generator", layout="centered")

st.title("📸 AI Image Caption Generator")
st.markdown("Upload an image and get a **cool Instagram-style caption**!")

# File uploader with drag & drop
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Language selection
language = st.selectbox("🌐 Translate caption to:", ["None", "Tamil", "Hindi", "French", "Spanish"])

# Session state for caption storage
if "caption" not in st.session_state:
    st.session_state.caption = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate_caption(uploaded_file)
            st.session_state.caption = caption
            st.success("Caption generated!")

    if st.session_state.caption:
        st.markdown(f"**📝 Caption:** {st.session_state.caption}")

        # Translate if selected
        if language != "None":
            try:
                translated = GoogleTranslator(source="auto", target=language.lower()).translate(st.session_state.caption)
                st.markdown(f"**🌍 Translated ({language}):** {translated}")
            except Exception as e:
                st.error("Translation failed. Please try again.")

        # Download option
        st.download_button(
            label="📥 Download Caption",
            data=st.session_state.caption.encode(),
            file_name="caption.txt",
            mime="text/plain"
        )
