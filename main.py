import streamlit as st

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
st.write(loremIpsum)
