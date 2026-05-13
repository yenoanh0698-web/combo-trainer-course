import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config to use full width
st.set_page_config(
    page_title="VMP Academy - Combo Trainer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI elements (header, footer, menu)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}
iframe {
    width: 100%;
    height: 100vh;
    border: none;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read and render the local HTML file
html_path = os.path.join(os.path.dirname(__file__), "index.html")

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # Render HTML in a full-screen iframe
    components.html(html_data, height=30000, scrolling=True)
    
except FileNotFoundError:
    st.error("Không tìm thấy tệp index.html. Vui lòng đảm bảo tệp nằm cùng thư mục với app.py.")
