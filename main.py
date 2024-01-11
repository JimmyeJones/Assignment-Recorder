import streamlit as st
st.title("Assignments")
page = st.selectbox("Page", ["Add", "View"])
list = []


if page == "Add":
  x = st.text_input("Assignment")
  if st.button("Add"):
    list.append(x)

for g in list:
  st.text(g)
