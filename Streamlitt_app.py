import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit#gid=1453155026"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1], worksheet="1585633377")
st.dataframe(data)

# Old code with streamlit-gsheets
gc = GSheetsConnection()
df = gc.read_sheet("Sheet1")

# New code with shillelagh
import shillelagh

gc = shillelagh.connect()
df = gc.read_sheet("Sheet1")


