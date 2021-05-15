import os, sys, datetime, json, requests
import pandas_datareader as pdr

print("\n")

class scrip_predict:
    def __init__(self, scrip):
        self.scrip = scrip

    #def get_data(self):
        # Gets the data for the scrip given by user
    
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
    scrip = input()
    #print(f"Scrip selected: {scrip}")

    with open('./api_credential.json', 'r') as creds:
        api_key = creds["API-KEY"]

    API = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:{scrip}&apikey={api_key}&outputsize=full"

    data = requests.get(API)
    print(data.status_code)

    print(f"Below is the data fetched for {scrip}\n")
    print(data.text)
