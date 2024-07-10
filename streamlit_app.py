import streamlit as st
import streamlit.components.v1 as components
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

components.html(
f"""
    <div>some hidden container</div>
    <p>{st.session_state.counterText}</p>
    <script>
        var input = window.parent.document.querySelectorAll("[type=text]");
        for (var i = 0; i < input.length; ++i) {{
            input[i].setAttribute('inputmode', 'numeric');
            input[i].focus();
        }}
    </script>
""",
height=0)

webbrowser.open(url)