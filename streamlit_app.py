import streamlit as st
import streamlit.components.v1 as components
import webbrowser

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
        document.querySelector("a[href]").click();
    </script>
""",
height=0)