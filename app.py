import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

pdf_viewer("RussellWhealdon_CVApr24.pdf")

st.set_page_config(page_title= f"Russell Whealdon Data Science Portfolio",page_icon="🧑‍🚀",layout="wide")
st.markdown(f"<h1 style='text-align: center; color: white;'>Russell Whealdon Resume</h1>", unsafe_allow_html=True)

#Set background image for page
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Page navigation
st.sidebar.markdown(f"<h4 style='text-align: center; color: white;'>Navigation</h4>", unsafe_allow_html=True)
url_home = "https://russellwhealdonportfolio.streamlit.app/"
url_resume = "https://russellwhealdonportfolio.streamlit.app/"
url_hobbies = "https://russellwhealdonportfolio.streamlit.app/"
st.sidebar.markdown(f"<h4><a href='{url_home}' target='_blank'>Home</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_resume}' target='_blank'>Resume</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_hobbies}' target='_blank'>Hobbies</a></h4>", unsafe_allow_html=True)
