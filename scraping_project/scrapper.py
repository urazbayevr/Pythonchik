from random import choice
import requests
from bs4 import BeautifulSoup
from termcolor import colored as color
from time import sleep
from csv import DictWriter, DictReader
url = "http://quotes.toscrape.com"


def parser():
    link = "/"
    text_list = []
    while link:
        get_url = requests.get(f"{url}{link}")
        print(f"{url}{link}..............")
        get_whole_page = BeautifulSoup(get_url.text, "html.parser")
        box = get_whole_page.select(".quote")
        for t in box:
            text_list.append({
                "text": t.select_one(".text").get_text(),
                "author": t.select_one(".author").get_text(),
                "bio-link": t.select_one("a")["href"]
            })
        next_link = get_whole_page.select_one(".next")
        link = next_link.select_one('a')['href'] if next_link else None
        sleep(1)
    return text_list


def write_csv(pars):
    with open("csv_file.csv", 'w') as file:
        headers = ["text", "author", "bio-link"]
        header = DictWriter(file, fieldnames=headers)
        header.writeheader()
        for p in pars:
            header.writerow(p)
# pars = parser()
# write_csv(pars)


def reader_csv(file):
    with open(file, 'r') as file:
        reader = DictReader(file)
        return list(reader)


def play_game(text_list):
    remaining_guess = 4
    rand_text = choice(text_list)
    print(rand_text['author'])
    print("Here's the quote: ")
    guess = ''
    c = color(rand_text['text'], color="magenta")
    print(c)
    while guess.lower() != rand_text['author'] and remaining_guess > 0:
        guess = input(f"Guess The AUTHOR:{remaining_guess}")
        if guess.lower() == rand_text['author'].lower():
            print(f"YOU GODDAMN RIGHT")
            break
        remaining_guess -= 1
        if remaining_guess == 3:
            res = requests.get(f"{url}{rand_text['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            born_date = soup.select_one(".author-born-date").get_text()
            born_location = soup.select_one(".author-born-location").get_text()
            colored_born = color(f"{born_date} {born_location}", color="blue")
            print(f"HINT: {colored_born}")
        elif remaining_guess == 2:
            first_char = color(
                f"First Name char: {rand_text['author'][0]}.",
                color="red")
            print(f"HINT: {first_char}")
        elif remaining_guess == 1:
            spl = rand_text["author"].split(" ")
            initials = color(
                f"Initials: {spl[0][0]}.{spl[1][0]}.",
                color="yellow")
            print(f"HINT: {initials}")
        elif remaining_guess == 0:
            print(f"You ran out of HINT :((")
            # if yes == "y"
        else:
            break

    again = input("Would You Like To Play Again:")
    str_again = ["yes", "y", "Yes"]
    if again.lower() in str_again:
        return play_game(text_list)
    else:
        print("OK BYEEEEE.........")


text = reader_csv("csv_file.csv")
print(play_game(text))
