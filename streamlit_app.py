import streamlit as st
import webbrowser

url = st.text_input("URL", label_visibility="collapsed")

webbrowser.open(url)