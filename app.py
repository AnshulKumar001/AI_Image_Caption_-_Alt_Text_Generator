import streamlit as st

from model.caption_model import generate_caption

from utils.image_processing import process_image


st.set_page_config(
    page_title="Image Caption Generator",
    page_icon="🖼️"
)

st.title("🖼️ AI Image Caption & Alt Text Generator")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = process_image(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image"
    )

    if st.button("Generate Caption"):

        with st.spinner("Generating..."):

            caption = generate_caption(image)

            alt_text = (
                f"Image showing {caption}. "
                f"This description is generated for accessibility."
            )

        st.subheader("Caption")

        st.success(caption)

        st.subheader("Alt Text")

        st.info(alt_text)

        st.download_button(
            "Download Caption",
            caption,
            "caption.txt"
        )

        st.download_button(
            "Download Alt Text",
            alt_text,
            "alt_text.txt"
        )