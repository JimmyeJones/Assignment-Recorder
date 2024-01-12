import streamlit as st

conn = st.connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)
