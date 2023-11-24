import streamlit as st
import pandas as pd

# Dispay Title and Description
st.title("Fridge")
st.markdown("Enter the product below")


import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('sectrets.json', scope)
gc = gspread.authorize(credentials)

# Open a worksheet
sheet = gc.open('Your Google Sheet Name').sheet1  # Change 'Your Google Sheet Name' to your sheet's name

# Read data from sheet
data = sheet.get_all_records()

# Display data in Streamlit
st.write(data)
