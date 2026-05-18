import math
import random
import datetime

print(math.sqrt(16))
print(math.pi)
print(math.floor(3.9))
print(math.ceil(3.1))

num = random.randint(1, 100)
print("random number:", num)

fruits = ["apple", "banana", "mango", "grapes"]
print("random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("shuffled:", fruits)

today = datetime.date.today()
print("today:", today)

now = datetime.datetime.now()
print("time:", now.strftime("%H:%M:%S"))
print("year:", now.year)
print("month:", now.month)
print("day:", now.day)