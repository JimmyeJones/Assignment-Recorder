import streamlit as st
st.title("Assignments")
page = st.selectbox("Page", ["Add", "View"])
Assignments = []


if page == "Add":
  x = st.text_input("Assignment")
  if st.button("Add"):
    Assignments.append(x)

st.text(Assignments)
