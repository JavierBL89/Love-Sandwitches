
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.auth.service account import credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = credentials.from_google_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scope(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwitches")
