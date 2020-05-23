def BubbleSort(mylist):
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for j in range(0, last_item - i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

    return mylist

oldlist = [1, 23, 13, 42, -3, 18]

print("Oldlist: ", oldlist)
final = BubbleSort(oldlist).copy()
print("Sorted List: ", final)
