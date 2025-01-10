import streamlit as st
import pandas

st.set_page_config(layout = "wide")

st.markdown("<h1 style='text-align: center; color: black;'>Portfolio Website</h1>", unsafe_allow_html=True)
st.logo("images/code.png")

col1, col_empty, col2, col_last= st.columns([0.3, 0.01, 0.6, 0.3], vertical_alignment= "top")

with col1:
    st.image("images/canva_edit.png", width= 300)

with col2:
    st.text("\n")
    st.subheader("Lexure Velasco", anchor= False)
    content = """
    Hi! I am Lexure! A computer science student in his 5th semester in TUHH searching for a student job or internship. My studies have equipped me with a solid theorical knowledge and I want
    to use the opportunity to bridge the gap between theory and practice by applying my knowledge to real-world scenarios and gaining hands-on experience.
    """
    st.info(content)

st.write("\n")
description  = "Below you can find some of the apps I have built in Python."
st.write(description)
if st.button("Feel free to contact me"):
    st.switch_page("pages/Contact_Me.py")

col3, empty_col, col4 = st.columns([1.5, 0.2, 1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"], divider= True)
        st.write(row["description"])
        st.image("images/"+ row["image"], width = 200)
        st.write(f"[Source code]({row['url']})")
 
with col4:
    for index, row in df[2:].iterrows():
        st.header(row["title"], divider= True)
        st.write(row["description"])
        st.image("images/5.png", width = 200)
        st.write(f"[Source code]({row['url']})")