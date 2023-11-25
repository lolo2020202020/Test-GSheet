# Create a virtual environment (Python 3.9 used here as an example)
python3.9 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate  # For Linux/Mac

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use your own credentials JSON file obtained from Google Cloud Platform
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secrets.json', scope)
client = gspread.authorize(creds)

# Access a specific Google Sheet by its URL or name
sheet = client.open('https://docs.google.com/spreadsheets/d/1ipfG6cDGUQjfhl6DjAWXfFaPfs05URC_tM64Dfz7Wts/edit?usp=sharing').sheet1

# Read data from the sheet
data = sheet.get_all_records()
