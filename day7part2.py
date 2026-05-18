import math
import random
import datetime

score = 95.7
print(math.floor(score))
print(math.ceil(score))
print(round(score))

sides = [3, 4, 5]
area = (sides[0] * sides[1]) / 2
print("triangle area:", area)
print("hypotenuse:", math.sqrt(sides[0]**2 + sides[1]**2))

guesses = []
for i in range(5):
    guesses.append(random.randint(1, 50))
print("guesses:", guesses)
print("highest:", max(guesses))
print("lowest:", min(guesses))

colors = ["red", "blue", "green", "yellow", "purple"]
random.shuffle(colors)
picked = random.choice(colors)
print("picked color:", picked)

now = datetime.datetime.now()
birthday = datetime.date(2007, 1, 1)
today = datetime.date.today()
age_days = (today - birthday).days
print("days since birthday:", age_days)
print("current hour:", now.hour)
print("current minute:", now.minute)