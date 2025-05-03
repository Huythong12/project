import streamlit as st 
import pandas as pd 
import numpy as np
from PIL import Image
import streamlit_lottie as st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

# App setup
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🧡", layout="wide")
st.subheader("Group 2.1")
st.title("PYTHON 2 - BUSINESS IT 2 :orange_heart:")

st.write("We are a group of business students who are interested in the economical situation in the world. Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades.")

# Toggle box
stoggle(
    "Group information",
    """
    \n 1. Dinh Ha Tu Van - 10622045
    \n 2. Bui Cam Ha Quyen - 10622023
    \n 3. Mai Hong Hanh - 10622014
    \n 4. Tran Quang Hieu - 10622088
    \n 5. Le Thi Minh Chau - 10622073
    """,
)

# Dataset link
st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link)")

# Emoji rain effect
rain(
    emoji="🔍",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

# Header
colored_header(
    label="Group members introduction",
    description="Get to know about our group",
    color_name="light-blue-70",
)

# === Member 1 ===
col1, col2 = st.columns(2)
with col1:
    st.image(Image.open('1.jpg'))
with col2:
    st.subheader("**Full name: Dinh Ha Tu Van (Group leader)**")
    st.write("Student ID: 10622045")
    st.write("Email: 10622045@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 077 6209215")

# === Member 2 ===
col3, col4 = st.columns(2)
with col3:
    st.image(Image.open('2.jpg'))
with col4:
    st.subheader("**Full name: Bui Cam Ha Quyen**")
    st.write("Student ID: 10622023")
    st.write("Email: 10622023@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")
    st.write("Phone number: 090 8784370")

# === Member 3 ===
col5, col6 = st.columns(2)
with col5:
    st.image(Image.open('3.jpg'))
with col6:
    st.subheader("**Full name: Mai Hong Hanh**")
    st.write("Student ID: 10622014")
    st.write("Email: 10622014@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 039 2230636")

# === Member 4 ===
col7, col8 = st.columns(2)
with col7:
    st.image(Image.open('4.jpg'))
with col8:
    st.subheader("**Full name: Tran Quang Hieu**")
    st.write("Student ID: 10622088")
    st.write("Email: 10622088@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 096 1234567")

# === Member 5 ===
col9, col10 = st.columns(2)
with col9:
    st.image(Image.open('5.jpg'))
with col10:
    st.subheader("**Full name: Le Thi Minh Chau**")
    st.write("Student ID: 10622073")
    st.write("Email: 10622073@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")
    st.write("Phone number: 093 7654321")

# --- Contact form ---
st.markdown("---")
st.subheader("💬 Leave us your message!")
st.caption("Let us know if you have any recommendations")

contactform = """<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email address" required>
     <textarea name="message" placeholder="What do you think?"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(contactform, unsafe_allow_html=True)

# Custom CSS (optional)
def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Uncomment below if you have custom style.css
# local_css("style.css")
