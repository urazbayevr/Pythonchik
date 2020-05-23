def binsearch(mylist, poisk, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if poisk == mylist[mid]:
            return mid
        elif poisk < mylist[mid]:
            return binsearch(mylist, poisk, start, mid - 1)
        else:
            return binsearch(mylist, poisk, mid + 1, stop)




mylist = [18, 20, 22, 25, 30, 32, 35, 42, 46, 58, 65, 85, 95, 100, 125, 140]

poisk = 18
start = 0
stop = len(mylist)

x = binsearch(mylist, poisk, start, stop)


if poisk == mylist[0]:
    print("item", poisk, "in", mylist[0])
elif (x == False):
    print("item", poisk, "not found")
else:
    print("item", poisk, "in", x+1)