import os, sys, datetime, json, requests
import numpy as np, pandas as pd
import pandas_datareader as pdr

print("\n")

class scrip_analysis:
    def __init__(self, scrip):
        self.scrip = scrip

    def get_data(self):

        scrip_data_api = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={scrip}&outputsize=full&apikey={api_key}"

        scrip_data_object = requests.get(scrip_data_api)
        print(f"\nSuccessfully retrieved Data for {scrip}!") if scrip_data_object.status_code == 200 else print("Did not get data")
        
        scrip_data = json.loads(scrip_data_object.text)
        scrip_data = scrip_data["Time Series (Daily)"]

        scrip_df = pd.DataFrame.from_dict(scrip_data, orient="index")
        scrip_df.columns = ["open", "high", "low", "close", "volumne"]
        
        print(scrip_df.head())

        return True
    
    #def preprocess_data(self):
        # process the data for the lstm model
    
    #def predict_scrip(self):
        # run the model and precit on the data
    
    #def results(self):
        # Return results to the user in the form of a chart opening
        # in a window
    
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

    for i in range(len(symbols_available["bestMatches"])):
        data = symbols_available["bestMatches"][i]
        print(" {0} | {1} | {2} | {3} ".format(data['1. symbol'],data['2. name'],data['3. type'],data['4. region']))
    
    print("\nPlease select one of the above scrips")
    scrip = input()

    scrip_analysis.get_data(scrip)