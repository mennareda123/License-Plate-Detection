import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from datetime import datetime

# ===== Load YOLO Model =====
model = YOLO("best.pt")  # Replace with your model weights

# ===== Streamlit UI =====
st.title("🚗 License Plate Detection")
st.markdown("### Real-time detection using YOLO + Streamlit")

mode = st.radio("Choose mode:", ["📷 Camera", "🖼️ Upload Image"])

# ===== Camera Mode =====
if mode == "📷 Camera":
    run_camera = st.checkbox("Turn on Camera", value=False)

    if run_camera:
        cap = cv2.VideoCapture(0)  # 0 = default webcam
        stframe = st.empty()

        # Save Screenshot Button
        if st.button("📌 Save Screenshot"):
            ret, frame = cap.read()
            if ret:
                results = model(frame)
                annotated_frame = results[0].plot()
                filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, annotated_frame)
                st.success(f"Screenshot saved as: {filename}")

        while run_camera:
            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Camera not working")
                break

            # YOLO Detection
            results = model(frame)
            annotated_frame = results[0].plot()

            # Convert BGR to RGB
            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            # Display frame
            stframe.image(annotated_frame, channels="RGB")

# ===== Image Upload Mode =====
elif mode == "🖼️ Upload Image":
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read image
        file_bytes = uploaded_file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Detection
        results = model(img)
        annotated_img = results[0].plot()
        annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

        st.image(annotated_img, caption="Detection Result", use_column_width=True)
