import streamlit as st
import cv2
import numpy as np
import pickle
from utils import calc_blurriness, calc_brightness, calc_contrast, calc_noise, calc_resolution

# Load model
with open("image_quality_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Image Quality Analyzer", layout="centered")
st.title("📸 Image Quality Analyzer")
st.write("Upload an image to check its quality and see detailed metrics.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Show uploaded image
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB", caption="Uploaded Image")

    # Extract 5 metrics
    brightness = calc_brightness(img)
    contrast = calc_contrast(img)
    noise = calc_noise(img)
    resolution = calc_resolution(img)
    blur = calc_blurriness(img)

    # Prepare features for model
    feats = np.array([brightness, contrast, noise, resolution, blur]).reshape(1, -1)

    # Prediction
    pred = model.predict(feats)[0]
    label = "✅ Good Quality" if pred == 1 else "❌ Bad Quality"

    st.subheader(f"Prediction: {label}")

    # Show metrics
    st.markdown("### 📊 Quality Metrics")
    st.write(f"- **Brightness**: {brightness:.2f}")
    st.write(f"- **Contrast**: {contrast:.2f}")
    st.write(f"- **Noise**: {noise:.2f}")
    st.write(f"- **Resolution**: {resolution} pixels")
    st.write(f"- **Blurriness**: {blur:.2f} (higher = sharper)")

    # Reason for bad image
    if pred == 0:
        reasons = []
        if blur < 100:
            reasons.append("Image is blurry")
        if brightness < 50:
            reasons.append("Image is too dark")
        if resolution < 200000:
            reasons.append("Image resolution is too low")
        if contrast < 30:
            reasons.append("Low contrast")
        
        if reasons:
            st.markdown("### ❌ Possible Issues")
            for r in reasons:
                st.write(f"- {r}")
