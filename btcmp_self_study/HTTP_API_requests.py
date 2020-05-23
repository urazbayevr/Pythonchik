"""import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} came back w/ status code {response.status_code}")

help(requests)"""
from pyfiglet import figlet_format as figlet
from termcolor import colored as color
from random import choice
import requ


kirgiw = 'My DAD JOKE!!!!'
osigo = figlet(kirgiw)
c = color(osigo,color="magenta")
print(c)

url = "https://icanhazdadjoke.com/search"

koyu = str(input("Kandai Prikol Tigain:  "))

response = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term": koyu}
)

data = response.json()

form = len(data["results"])

if form == 1:
    print(data["results"]["joke"])
elif form > 1:
    choice = choice(data["results"])
    print(choice['joke'])
else:
    print("No jokes for that word")
