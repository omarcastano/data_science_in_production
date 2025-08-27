import time

import streamlit as st

# title of the app
st.title("First Streamlit Application, Email Generator")

# text data
st.text("This is a simple aplication that request name and last name from user and create a email address.")

# read input from user
name = st.text_input("Enter your name:", "Type Here...")
last_name = st.text_input("Enter your last name:", "Type Here...")

# create email address
email = f"{name.lower()}.{last_name.lower()}@gmail.com"

# add a button to generate email
if st.button("Generate Email"):
    # simulate a delay
    with st.spinner("Generating email..."):
        time.sleep(2)  # Simulate a delay of 2 seconds

    # display email address
    st.info(f"Your email address is: {email}")
