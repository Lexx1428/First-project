import streamlit as st
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
        send_email(message)
        st.info("Email sent successfully!")
