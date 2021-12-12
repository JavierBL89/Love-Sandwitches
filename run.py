
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

#WE DELETE THIS CODE AS IT IS ONLY TO CHECK THAT THE API WAS WORKING
# #let's access the data in our sales worksheet
# sales = SHEET.worksheet("sales") #we call th worksheet() method of the SHEET
#                                  # and pass it the sales worksheet
# #we use the gpread method get_all_values to pull the value from the worksheet
# data = sales.get_all_values()

# print(data)


def get_data_sales_user():
    """
    Get sales input data from users
    """
    while True:
        print("Please enter sales data from the last market")
        print("Dta shoul be six numbers separated by comma.")
        print("Example, 24,22,85,12,5,51\n")

        data_str = input("Enter data: ")
        sales_data = data_str.split(",")

        if valid_data_sales(sales_data):
            print("data is valid!")
            break
    return sales_data


def valid_data_sales(values):
    """
    Inside the try, converts all strings into integers.
    Raises an error if the strings cnnot be converted
    or there aren't exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you entered {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True


data = get_data_sales_user()
print(data)
