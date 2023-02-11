import streamlit as st
import requests
from streamlit_lottie import st_lottie
from pathlib import Path
st.set_page_config(page_title='My Website', page_icon=':tada:', layout='wide')

#Path Settings
STRIPE_CHECKOUT = "https://www.youtube.com/channel/UCtNNl-4R1_n8rI78SB11Wbw?app=desktop"
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / 'assets'
STYLES_DIR = THIS_DIR / 'style'
CSS_FILE = STYLES_DIR/ "main.css"

#Opening a CSS
def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#Loading the Lottie
def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieur1("https://assets4.lottiefiles.com/packages/lf20_6xfdtlzb.json")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieur1("https://assets10.lottiefiles.com/packages/lf20_NI497MPlTg.json")

#Description
with st.container():
    st.subheader("Hi, I am Vihaan Kamath!:wave:")
    st.title("A YouTuber From Canada")
    st.write("I am working on a Python Code this is a test. I will make this website about my YouTube channel!")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I post")
        st.write("##")
        st.write(
        """
        On my Youtube Channel I create videos on Hypixel Skyblock! 
        - I post tutorials 
        - I post cool interviews 
        - I post nice videos 
        - Funny Videos
        - Post Weekly
        - Adventures I do! 
        If this sounds nice you should really consider subscribing and watch my videos!
        """
    )
    st.write("[Youtube Channel Link >](https://www.youtube.com/channel/UCtNNl-4R1_n8rI78SB11Wbw?app=desktop)")

with right_column:
    st_lottie(lottie_coding, height=300)

