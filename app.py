import streamlit as st

st.title("Streamlit Demo App🚀")
st.markdown("Willkommen auf meiner **Website**.")

username = st.text_input("Gib deinen Namen ein:")

st.write(username.upper())