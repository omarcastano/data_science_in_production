"""This module provides a simple example of how to deploy a FastAPI application with Streamlit."""

import requests
import streamlit as st
from PIL import Image

# define url
URL = "http://127.0.1:8000/post_fraction"
HEADER = {"Content-Type": "application/json"}


st.title("FastAPI with Streamlit Example")
st.write("This is a simple example of how to deploy a FastAPI application with Streamlit.")

# load image
path_image = "content/images/fastapi_plus_streamlit.png"
image = Image.open(path_image)
st.image(image, caption="FastAPI with Streamlit Example", use_container_width=True, width=200)

a = st.number_input("Enter value for 'a':", value=5.0)
b = st.number_input("Enter value for 'b':", value=5.0)

if st.button("Calculate Fraction"):
    respone = requests.post(url=URL, json={"a": a, "b": b}, headers=HEADER, timeout=10)
    result = respone.json()["result"]
    st.info(f"The result of {a:.2f} / {b:.2f} is: {result:.2f}")
