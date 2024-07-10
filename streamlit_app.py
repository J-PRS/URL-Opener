import streamlit as st
import streamlit.components.v1 as components
import webbrowser

url = st.text_input("URL", label_visibility="collapsed")

if "http" in url:
    # st.markdown(f"[APP]({url})")
    # st.write(url)
    # st.markdown()
    st.markdown(
        f'<a href="{url}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">APP</a>',
        unsafe_allow_html=True
    )

    components.html(
    f"""
        <div>
        <p>
        <a href="https://copilot.microsoft.com/" target="_self" rel="noopener noreferrer">APP</a>
        </p>
        </div>
    """,
    height=0)

    components.html(
    f"""
        <div>some hidden container</div>
        <script>
            window.parent.document.querySelector("a[href]").click();
        </script>
    """,
    height=0)