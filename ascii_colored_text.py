from pyfiglet import figlet_format as figlet
from termcolor import colored as color

cvetter = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]


kirgiw = str(input("Ne jazgin keled:"))
colored = str(input("Kandai tus tandaisin: "))

if colored not in cvetter:
    colored = "magenta"

osigo = figlet(kirgiw)
c = color(osigo,color=colored)
print(c)

