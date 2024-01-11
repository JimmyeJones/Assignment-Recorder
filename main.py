import streamlit as st
from replit import db
from os import environ
environ["REPLIT_DB_URL"] = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2OTQxNjA0NzksImlhdCI6MTY5NDA0ODg3OSwiZGF0YWJhc2VfaWQiOiJhZjQ5Y2E2NC0xMmMyLTRhN2UtYWY0Mi1hYzg0MzFmMDczZTQiLCJ1c2VyIjoiTWF0dG94LUoiLCJzbHVnIjoidGVzdC1mb3ItaGFsbC1idWRkeSJ9.WHQf0i_MdU3fDhrn5HusS0z0NvaAMe6HKpyg0pgEamJ-KQOTLwogjIpoQiM7d8P7o__ZdrK3U1Ek0x-NMCc0fg"
st.title("Assignments")
page = st.selectbox("Page", ["Add", "View"])

db["list"] = []



if page == "Add":
  x = st.text_input("Assignment")
  if st.button("Add"):
    db["list"].append(x)

for g in db["list"]:
  st.text(g)
