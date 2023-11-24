import streamlit as st
import pandas as pd

# Dispay Title and Description
st.title("Fridge")
st.markdown("Enter the product below")

# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/1ipfG6cDGUQjfhl6DjAWXfFaPfs05URC_tM64Dfz7Wts"

# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
