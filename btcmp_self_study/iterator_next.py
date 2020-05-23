'''class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for i in Counter(20,30):
    print(i*10)
'''
############################
"""def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
"""
############################
"""def fib_it(num):
    lis = []
    a = 0
    b = 1
    while num >= len(lis):
        lis.append(b)
        a,b = b,a+b
    return lis
"""
#############################
'''def fib_gen(num):
    a = 0
    b = 1
    count = 0
    print("koyeee")
    while count < num:
        print("birinwi")
        yield a+b
        a,b = b,a+b
        count += 1
        print("ekinwi")

for i in fib_gen(10):
    print(i)
'''
##############################
"""
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num

for i in get_multiples():
    print(i)"""
#############################
import time
# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time()  # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time  # end time - start time

# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")

