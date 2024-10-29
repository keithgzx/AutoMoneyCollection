import src
import os
from dotenv import load_dotenv

"""
collection_date has to strictly follow the dd-mmm-yyyy format where mmm is:
"Jan" / "Feb" / "Mar" / "Apr" / "May" / "Jun" /
"Jul" / "Aug" / "Sep" / "Oct" / "Nov" / "Dec"
example: "01-Jan-2024" (case sensitive)

excel_filename will be the name of the file before the .xlsx extension:
example: "Week1" will give Week1.xlsx as the output excel file (avoid spaces)
"""

############### DO NOT EDIT ABOVE ###############


# Input your initial collection date and preferred filename here:
collection_date = "31-Oct-2024"
excel_filename = "Week1"


############### DO NOT EDIT BELOW ###############

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

config = {
    'username': USER,
    'password': PASSWORD,
    'search_query': ['FROM', 'ibanking.alert@dbs.com', 'SUBJECT', 'Transaction Alerts', 'SINCE', collection_date],
    'output_file_path': f'{excel_filename}.xlsx'
}

src.main(config)