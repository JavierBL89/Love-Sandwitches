
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
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


def update_sales_worksheet(data):
    """
    Add new sales data into the sales worksheet
    """
    # WE USE THIS PRINT SATATEMENT TO GIVE SOME FEEDBACK TO THE USER
    # AND ALSO IN THE APP CRASHED WILL TRACK DOWN WHERE EXACTLY IT DID
    print("Updating sales worksheet...")
    #HERE WE ACCESS TO THE GOOGLE WORKSHEET APP
    #AND WE USED THE  WORKSHEET METHODS
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated")


def update_surplus_worksheet(surplus):
    """
    Update surplus worksheet with the last surplus market
    """
    print("Updating surpus worksheet...")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(surplus)
    print("Surplus worksheet updated")


print("Welcome to Love Sandwitches Automation")


def calculate_sales_surplus(sales):
    """
    ACCSESS THE STOCK WORKSHEET TO CALCULATE SURPLUS
    """
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint([int(value) for value in stock[-1]])
    stock_row = [int(value) for value in stock[-1]]
    # result = zip(stock_row, sales)
    # return list(result)
    surplus_list = []
    for stock, sales in zip(stock_row, sales):
        surplus = stock - sales
        surplus_list.append(surplus)
    return surplus_list


def main():
    data = get_data_sales_user()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    surplus_data = calculate_sales_surplus(sales_data)
    update_surplus_worksheet(surplus_data)


main()
