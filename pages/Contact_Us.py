import streamlit as st
from send_email import send_email

st.header("Contact me")

with ((st.form(key="form"))):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = f"""Subject: Portfolio Website - {user_email}\n
        From: {user_email}
        {message}
        """
    button = st.form_submit_button("Submit")

if button:
    send_email(message)
    st.info("Email sent")
