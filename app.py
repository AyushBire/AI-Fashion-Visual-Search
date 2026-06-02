import streamlit as st
from PIL import Image
from search import find_similar_images

st.set_page_config(page_title="Fashion Visual Search")

st.title("👕 Fashion Visual Search")
st.write("Upload a clothing image and find similar products.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    query_path = "query_image.jpg"

    with open(query_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.subheader("Uploaded Image")
    st.image(query_path, width=250)

    if st.button("Find Similar Products"):

        results = find_similar_images(query_path, k=5)

        st.subheader("Similar Products")

        cols = st.columns(5)

        for col, result in zip(cols, results):

            img = Image.open(result["image_path"])

            with col:
                st.image(img, use_container_width=True)
                st.write(
                    f"Distance: {result['distance']:.2f}"
                )