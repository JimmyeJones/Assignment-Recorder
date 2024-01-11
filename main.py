import streamlit as st
from replit import db
st.title("Assignments")
page = st.selectbox("Page", ["Add", "View"])

db["list"] = []



if page == "Add":
  x = st.text_input("Assignment")
  if st.button("Add"):
    db["list'].append(x)

for g in db["list"]:
  st.text(g)
