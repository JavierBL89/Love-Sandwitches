
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwitches")


#let's access the data in our sales worksheet
sales = SHEET.worksheet("sales") #we call th worksheet() method of the SHEET 
                                 # and pass it the sales worksheet

#we use the gpread method get_all_values to pull the value from the worksheet
data = sales.get_all_values()

print(data)