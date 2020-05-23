"""def factorial(x):
    summa = 1
    for i in range(1, x+1):
        summa = summa * i
    return summa

def ademilepjazu(x):
    for i in range(1, x+1):
        print(str(i) + "! = " + str(factorial(i)))

print(ademilepjazu(4))
"""


def Factorial(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * Factorial(x - 1)


z = Factorial(3)
print(z)
