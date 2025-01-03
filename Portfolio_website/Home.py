import streamlit as st
import pandas

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width= 400)

with col2:
    st.title("Lexure Velasco")
    content = """
    Hi! I am Lexure! A computer science student in TUHH looking for a job.
    """
    st.info(content)


description  = "Below you can find some of the apps I have built in Python. Feel free to contact me."
st.write(description)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width = 200)
        st.write(f"[Source code]({row['url']})")
 
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"],width = 200)
        st.write(f"[Source code]({row['url']})")