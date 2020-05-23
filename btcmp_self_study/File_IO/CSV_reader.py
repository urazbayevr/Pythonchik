# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
#with open("fighters.csv") as file:
# data = file.read()

# Using reader
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader) #To skip the headers
#     for fighter in csv_reader:
#     	# Each row is a list
#     	# Use index to access data
#     	print(f"{fighter[0]} is from {fighter[1]}")

# Example where data is cast into a list
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)

# with open("fighters.csv",'w') as file:
#     csv = file.write("Name,Country,Height (in cm)\nRyu,Japan,175\nKen,USA,175\nChun-Li,China,165\nGuile,USA,182\nE. Honda,Japan,185\nDhalsim,India,176\nBlanka,Brazil,192\nZangief,Russia,214\n")

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row) #Use keys to access data