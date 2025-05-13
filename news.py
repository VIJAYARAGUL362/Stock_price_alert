import os,requests
from dotenv import load_dotenv
import smtplib


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


load_dotenv()
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

parameters_news = {
    "q":COMPANY_NAME,
    "apiKey":API_KEY_NEWS,
}

response = requests.get(url="https://newsapi.org/v2/everything",params=parameters_news)
response.raise_for_status()
news = response.json()["articles"]

title = []
content = []
url = []
for i in range(3):
    title.append(news[i]['title'])
    content.append(news[i]['description'])
    url.append(news[i]["url"])




def new_sender(percentage):
    if percentage > 5:
        message = f"increased {percentage}%"
    else:
        message = f"decreased {percentage}%"
    for number in range(len(title)):
        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=USER,password=PASSWORD)
            connections.sendmail(from_addr=USER,to_addrs=USER,msg=f"SUBJECT:{title[number]}\n\n{STOCK} {message}\n\n{content[number]}\n"
                                                                  f"{url[number]}")

    os.remove("price.csv")

