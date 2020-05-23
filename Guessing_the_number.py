import random

computer = random.randint(1,10)

number = None

while True:
    number = int(input("poprobui\n"))
    if number > computer:
        print("Kop bop ketti")
    elif number < computer:
        print("Az goi 4etaaa")
    else:
        print("You r right!!! ", computer)
        break
