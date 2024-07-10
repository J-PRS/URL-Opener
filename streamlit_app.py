import streamlit as st
import webbrowser

def format_line_with_style(text, top_margin = "inherit", bottom_margin = "inherit", font_size = 24):
    style = f"text-align: center; margin-top: {top_margin}px; margin-bottom: {bottom_margin}px; font-size: {font_size}px;"
    line = f"<p style='{style}'>{text}</p>"
    st.markdown(line, unsafe_allow_html=True)

url = st.text_input("URL", label_visibility="collapsed")
st.markdown(f"[APP]({url})")

st.markdown(
    f'<a href="{url}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">APP</a>',
    unsafe_allow_html=True
)

webbrowser.open(url)