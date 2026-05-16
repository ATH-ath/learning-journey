try:
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age cant be negative")
    print("your age is", age)
except ValueError as e:
    print("error:", e)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cant be 0")
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("error:", e)


f = open("scores.txt", "w")
for i in range(1, 6):
    f.write("player" + str(i) + " - " + str(i * 10) + "\n")
f.close()

f = open("scores.txt", "r")
for line in f:
    print(line.strip())
f.close()