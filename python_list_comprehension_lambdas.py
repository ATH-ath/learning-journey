squares = [x ** 2 for x in range(1, 11)]
print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

words = ["hello", "world", "python", "code"]
upper = [w.upper() for w in words]
print(upper)


double = lambda x: x * 2
square = lambda x: x ** 2
add = lambda a, b: a + b

print(double(5))
print(square(4))
print(add(3, 7))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


students = [
    {"name": "lexi", "grade": 85},
    {"name": "alex", "grade": 40},
    {"name": "sam", "grade": 72},
]

students.sort(key=lambda s: s["grade"], reverse=True)
for s in students:
    print(s["name"], s["grade"])
