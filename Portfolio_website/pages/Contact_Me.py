import streamlit as st
import time
from send_email import send_email 


st.header("Contact Me")

with st.form(key = "email_form"):
    user_email = st.text_input("Your e-mail adress: ")
    raw_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """
    if button:
        #send_email(message)
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.info("Email sent successfully!")
        st.balloons()

st.caption("You can also contact me with the following E-mail: \n"
        "vlexure14@gmail.com")

