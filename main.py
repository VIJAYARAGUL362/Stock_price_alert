import os
import requests

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY_PRICE = os.getenv("API_KEY_PRICE")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


parameter_price = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":API_KEY_PRICE,
    "datatype":"csv",
}
response1 = requests.get(url="https://www.alphavantage.co/query",params=parameter_price)
response1.raise_for_status()

try:
    with open(file="price.csv",mode="r") as file:
        content = file.read()
except FileNotFoundError:
    with open(file="price.csv",mode="w") as file:
        file.write(f"{response1.text}")
finally:
    csv_file = pd.read_csv("price.csv")
    dataframe = pd.DataFrame(csv_file)

needed_dataframe = dataframe.iloc[0:2,:]["close"]

change = (needed_dataframe.pct_change())[1]
change = int(change*100)


if change > 5 or change < -5:
    import news
    news.new_sender(change)


