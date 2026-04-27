import streamlit as st
import torch
from PIL import Image
import cv2
import numpy as np
import tempfile

st.title("YOLOv5 Object Detection")
st.sidebar.title("Settings")
st.sidebar.markdown("---")

model_type = st.sidebar.selectbox("Select Model", ["yolov5s", "yolov5m", "yolov5l"])
confidence = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.25)

model = torch.hub.load('.', model_type, source='local', force_reload=False)
model.conf = confidence

st.sidebar.markdown("---")
source_type = st.sidebar.selectbox("Select Source", ["Image", "Video"])

if source_type == "Image":
    uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        results = model(image)
        st.image(np.squeeze(results.render()),
                 caption="Detected Objects", use_column_width=True)
        st.write(results.pandas().xyxy[0])

elif source_type == "Video":
    uploaded = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
    if uploaded:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded.read())
        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            stframe.image(np.squeeze(results.render()),
                          channels="BGR", use_column_width=True)
        cap.release()
