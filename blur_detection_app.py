import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit UI
st.title("🔍 Blur Detection App")
st.write("Upload an image to check if it is **blurred or sharp** using Variance of Laplacian.")

# File uploader
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Apply Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    variance = laplacian.var()

    # Threshold for blur detection
    threshold = 100.0
    is_blurred = variance < threshold

    # Show results
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write(f"📊 **Variance of Laplacian:** `{variance:.2f}`")

    if is_blurred:
        st.error("❌ The image is Blurred")
    else:
        st.success("✅ The image is Sharp")
