import streamlit as st
import streamlit.components.v1 as components
import webbrowser

url = st.text_input("URL", label_visibility="collapsed")

if "http" in url:
    st.markdown(
        f'<a href="{url}" target="_self">APP</a>',
        unsafe_allow_html=True
    )

    components.html(
    f"""
        <div>some hidden container</div>
        <script>
            var button = window.parent.document.querySelector("a[href]");
            button.click()
        </script>
    """,
    height=0)

components.html(
f"""
    <div>some hidden container</div>
    <p>{st.session_state.counterText}</p>
    <script>
        var input = window.parent.document.querySelectorAll("[type=text]");
        for (var i = 0; i < input.length; ++i) {{
            input[i].focus();
        }}
    </script>
""",
height=0)