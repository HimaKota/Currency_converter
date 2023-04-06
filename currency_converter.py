import requests
api_key = "9f84508c79e549dd8fe320139de6fdaa"
#retrieve currency and exchange rate information
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
# Make the request for the exchange rate data
response = requests.get(url)
# store the response in JSON format
data = response.json()
# Save this exchange rate data
exchange_rates = data["rates"]
available_currencies = ""
for currency in exchange_rates.keys():
    available_currencies += currency + ", "

# Remove the trailing comma and space
available_currencies = available_currencies[:-2] 
print("Available currencies: " + available_currencies)
from_currency = input("Enter the from currency: ").upper()
to_currency = input("Enter the to currency: ").upper()
amount = float(input("Enter the amount to convert: "))
original_amount = amount / exchange_rates[from_currency]
converted_amount = round(original_amount * exchange_rates[to_currency],2)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")