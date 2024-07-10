import streamlit as st
import webbrowser

url = st.text_input("URL", label_visibility="collapsed")
st.write(url)
webbrowser.open(url)