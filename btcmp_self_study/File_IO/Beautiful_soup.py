from bs4 import BeautifulSoup
import requests
from csv import DictWriter,writer

url = "https://kolesa.kz/cars/almaty/?auto-car-grbody=1"
site = requests.get(url)
page = BeautifulSoup(site.text, "html.parser")
root = page.find_all(class_="row vw-item list-item blue a-elem")

article_cars = page.select(".a-el-info-title")
article_price = page.select(".price")
article_god = page.select(".a-search-description")

with open("kolesa.csv","w") as file:
    headers = ["Cars","Price","Year"]
    csv_file = DictWriter(file,fieldnames=headers)
    csv_file.writeheader()

    for i in range(len(article_cars)):
        car = article_cars[i].get_text().strip()
        god = article_god[i].get_text().strip()[0:4]
        price = article_price[i].get_text().strip()
        csv_file.writerow({"Cars": car,"Price": price,"Year": god})

with open("kolesazip.csv", "w") as file:
    headers = ["Cars", "Price", "Year"]
    csv_file = DictWriter(file, fieldnames=headers)
    csv_file.writeheader()

    listik,listik2,listik3 = [],[],[]
    for i in range(len(article_cars)):
        price = article_cars[i].get_text().strip()
        listik.append(price)
    for i in range(len(article_price)):
        price = article_price[i].get_text().strip()
        listik2.append(price)
    for i in range(len(article_god)):
        god = article_god[i].get_text().strip()
        god = god[0:4]
        listik3.append(god)
    a = zip(listik,listik2,listik3)
    for i in list(a):
        csv_file.writerow({"Cars": i[0],"Price": i[1],"Year": i[2]})
