import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

pkl_path = 'dog_breed.h5'

# loading the model
model = load_model(pkl_path)

# Name of classes
classes = ['scottish deerhound', 'maltese dog', 'afghan hound', 'entlebucher', 'bernese mountain dog', 'shih-tzu', 'great pyrenees', 'pomeranian', 'basenji', 'samoyed']


with st.sidebar:
    st.subheader('Available Dog Breeds')
    st.markdown('- scottish deerhound')
    st.markdown('- maltese dog')
    st.markdown('- afghan hound')
    st.markdown('- entlebucher')
    st.markdown('- bernese mountain dog')
    st.markdown('- shih-tzu')
    st.markdown('- great pyrenees')
    st.markdown('- pomeranian')
    st.markdown('- basenji')
    st.markdown('- samoyed')

# Setting the title of app
st.header("BreedSpotter")

st.image(
    'https://t4.ftcdn.net/jpg/01/96/97/53/360_F_196975369_W7b15V9vjRgNuSGNpJJjm93gpcdHi1h4.jpg'
)

# Uploading the dog image
dog_image = st.file_uploader("Upload image of a dog", type="jpg")
submit = st.button("Predict")

# On Clicking Predict Button
if submit:
    if dog_image is not None:
        # Convert the file to an open cv image
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # Display the image
        st.image(opencv_image, channels="BGR")

        # Resizing the image
        opencv_image = cv2.resize(opencv_image, (224, 224))

        # Convert image to 4 Dimensions
        opencv_image = image.img_to_array(opencv_image)
        opencv_image = np.expand_dims(opencv_image.copy(), axis=0)
        opencv_image = opencv_image / 255.0

        # Make Prediction
        prediction = model.predict(opencv_image)

        st.title(str("The Dog Breed is " + classes[np.argmax(prediction)]))
