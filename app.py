import streamlit as st
import cv2
from makeup_app import MakeupApplication  # Assuming your class is in a file named MakeupApplication.py

# Initialize makeup app
makeup_app = MakeupApplication()

# Streamlit interface
st.title('Virtual Makeup Application')

# Capture the video feed
run = st.checkbox('Start Video Makeup Application')

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    while run:
        success, frame = cap.read()
        if not success:
            st.write("Ignoring empty camera frame.")
            break

        # Process the frame to apply makeup
        frame = makeup_app.process_frame(frame)

        # Convert BGR to RGB for Streamlit display
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()
