import os, sys, datetime, json, requests
import numpy as np, pandas as pd

print("\n")

class scrip_analysis:
    ''' This class is used to get the data, process it, and feed into the LSTM '''
    def __init__(self, scrip, api_key):
        self.scrip = scrip
        self.api_key = api_key

    def get_data(self):
        scrip_data_api = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={scrip}&outputsize=full&apikey={api_key}"

        scrip_data_object = requests.get(scrip_data_api)
        print(f"\nSuccessfully retrieved Data for {scrip}!") if scrip_data_object.status_code == 200 else print("Did not get data")
        
        scrip_data = json.loads(scrip_data_object.text)
        scrip_data = scrip_data["Time Series (Daily)"]

        scrip_df = pd.DataFrame.from_dict(scrip_data, orient="index")
        scrip_df.columns = ["open", "high", "low", "close", "volumne"]
        scrip_df.reset_index(inplace=True)
        scrip_df.columns = ["date", "open", "high", "low", "close", "volumne"]
        print(scrip_df.head())

        return scrip_df
        
    
    def preprocess_data(self):
        return True
    
    def predict_scrip(self):
        return True
    
    def results(self):
        return True
    
#class LSTM:
   # Build the LSTM model using tensorflow


if __name__ == "__main__":
    
    print("Input the Stock Code you want to checkout!")
    symbol = input()
    while not symbol:
        print("You did not provide a valid Stock Code. Please enter again.")
        symbol = input()

    with open('./api_credentials.json') as creds:
        data = json.load(creds)
        api_key = data["API_KEY"]

    symbol_search = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}"
    symbols_available = json.loads(requests.get(symbol_search).text)
    print("Symbols available are: ")

    scrip_checklist = []
    for i in range(len(symbols_available["bestMatches"])):
        data = symbols_available["bestMatches"][i]
        scrip_checklist.append(data["1. symbol"])
        print(" {0} | {1} | {2} | {3} ".format(data['1. symbol'],data['2. name'],data['3. type'],data['4. region']))
    
    print("\nPlease select one of the above scrips")
    scrip = input()
    while not scrip:
        print("You did not select a scrip from the above list. Please select a scrip.")
        scrip = input()

    while scrip:
        if scrip not in scrip_checklist:
            print("Please select a valid scrip from those listed above.")
            scrip = input()
        else:
            break

    stock = scrip_analysis(scrip, api_key)
    stock.get_data()