# -*- coding: utf-8 -*-
"""Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19L6Jo-0yUJofnmFsWnXAsmqpWg36nktG
"""

import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image,ImageOps
import numpy as np

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('final_model.h5')
  return model
model=load_model()
st.title("Shoe Classifier")
file=st.file_uploader("Choose a photo from your computer",type=["jpg","png"])

def import_and_predict(image_data,model):
    size=(128,128)
    image = ImageOps.fit(image_data,size, Image.LANCZOS)
    image = np.asarray(image)
    image = image / 255.0
    img_reshape = np.reshape(image, (1, 128, 128, 3))
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Apple', 'Tomato']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)