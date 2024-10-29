import email
import sys
import os

import pandas as pd
from imapclient import IMAPClient
from imapclient.exceptions import LoginError
from bs4 import BeautifulSoup

########## DO NOT EDIT OR RUN THIS FILE DIRECTLY: RUN app.py INSTEAD ##########

def main(config: dict[str]):
    """
    Main function - Establishes email connection\n
    Calls fetch_message_data and write_to_excel for input and output info respectively
    """
    username = config.get('username')
    password = config.get('password')
    with IMAPClient('imap.gmail.com') as client:
        try:
            client.login(username, password)
        except LoginError as e:
            print("Login failed:", str(e))
            sys.exit()

        client.select_folder('INBOX')
        search_query = config.get('search_query')
        messages = client.search(search_query)  

        if messages:
            message_data: dict = fetch_message_data(messages, client)
            output_file_path = config.get('output_file_path')
            write_to_excel(message_data, output_file_path)
            client.logout()
        else:
            print(f"No messages matching the search query were found in the INBOX folder")
            client.logout()
            sys.exit()

def fetch_message_data(message_data, client: IMAPClient):
    try:
        data_dict = {}
        message_content = client.fetch(message_data, ['BODY[TEXT]'])

        for gmail_id, data in message_content.items():
            message_body = email.message_from_bytes(data[b'BODY[TEXT]'])
            content = message_body.get_payload(decode=True).decode('utf-8')

            soup = BeautifulSoup(content, 'lxml')
            extracted_content = soup.find('p', style="font: normal 16px/1.2em arial;").text # hardcoded
            content_list = extracted_content.split(" ")
            info = False

            if content_list:
                if float(content_list[8])%1 == 0:# hardcoded
                    amt = int(content_list[8].split(".")[0]) # hardcoded
                else:
                    amt = float(content_list[8]) # hardcoded
                
                date = int(content_list[10]) # hardcoded
                month = content_list[11] # hardcoded
                time = content_list[12] # hardcoded
                idx = content_list.index("to") # hardcoded
                name = " ".join(content_list[15:idx]) # hardcoded
                info = [name, amt, date, month, time]

            if info:
                data_dict[gmail_id] = info
        return data_dict
        
    except ValueError as e:
        print(str(e))
        sys.exit()

def write_to_excel(write_data: dict, file_path):
    rows = [{'Name': lst[0], 'Amount': lst[1], 'Date': lst[2], 'Month': lst[3], 'Time': lst[4]} for eid, lst in write_data.items()]
    df = pd.DataFrame(rows)

    try:
        if os.path.exists(file_path):
            df_existing = pd.read_excel(file_path)
            df_updated = pd.concat([df_existing, df], ignore_index=True)
            df_updated.to_excel(file_path, index=False)
            print("Attached new (duplicated) data to current file!\nExcel write operation successful")
        else:
            df.to_excel(file_path, index=False)
            print("Excel write operation successful")
        print("Exiting application...",end="")
    except Exception as e:
        print(str(e))
        print(f"Please make sure the file path {file_path} is correct and file has the necessary permissions.")
        sys.exit()

if __name__ == "__main__":
    print("<!>\nPlease open the main AutoMoneyCollection file and run the program from app.py instead.\nExiting application...\n<!>",end="")