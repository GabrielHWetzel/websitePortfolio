import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

# Todo - remove later
with open("loremIpsum.txt", 'r') as lp:
    loremIpsum = lp.read()

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Gabriel Henrique Wetzel")
    content = """Image is temporary. I'm not that guy."""
    st.info(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
