import time

import streamlit as st

st.title("My first website")
st.header("PIAIC student")
st.subheader("learning python")
st.info("I am learning agentic ai from PIAIC institute")
st.write(
    "PIAIC is an institute in which you can take admision if you want to become an AI developer.This is an excelent opportunity for all of us .As all of us knows that whole world is moving toward artificial "
)
st.success("Quarter 1 sussessfully ended")
st.markdown("# Large Text")
st.markdown("### small text")
st.markdown("## Medium Text")
st.write("equation")
st.latex(r"""a^2+b^2=c^2""")
st.checkbox("mark it")
st.radio("select your gender", ["male", "female", "another"])
st.selectbox("choose your programing language", ["python", "c++", "java"])
st.button("click here")
st.multiselect(
    "which languages can you speak", ["Urdu", "English", "Punjabi", "chinese"]
)
st.select_slider("Rating", ["bad", "good", "excelent"])
st.slider("enter number", 1, 100)
st.number_input("enter your number", 0, 100)
st.text_input("Enter your text here")
st.date_input("enter current date")
st.time_input("enter your time ")
st.text_area("Welcome to my my website")
st.color_picker("color")
st.progress(80)
st.sidebar.title("Hy Everyone")
st.sidebar.text_input("enter your email")
st.sidebar.text_input("enter password")
st.sidebar.button("Enter")
st.sidebar.radio("Field of study", ["computer science", "Arts"])
