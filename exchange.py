import bs4
import sys
import requests
import pyperclip
import json

sys.argv # ["exchange.py", <source_coin> <target_coin> <amount>] || ["exchange.py", <amount>]

API_KEY = "__" #enter here your API_KEY from rapid_api

if len(sys.argv) > 2:    
    source_coin = sys.argv[1]
    target_coin = sys.argv[2]
    amount = sys.argv[3]
    
else:
    source_coin = "ILS"
    target_coin = "USD"
    amount = sys.argv[1]


url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format":"json","from":source_coin,"to":target_coin,"amount":amount}



headers = {
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
    'x-rapidapi-key': "965b9ef643mshcd4da9cc82b8899p151ddcjsn602468997eeb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(f'Converting {amount} {source_coin} to {target_coin}')
if response.status_code != 200:
    print("error, please try again")
    print(response.body)
else:
    rate = response.json()['rates'][target_coin]['rate']
    rate_for_amount = response.json()['rates'][target_coin]['rate_for_amount']
    print(f'the current rate is: {rate}')
    print(f'{amount} of {source_coin} equal to {rate_for_amount} {target_coin}')
