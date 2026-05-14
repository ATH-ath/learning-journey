def greet(name):
    print("Hello,", name)

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

greet("Lexi")
print(add(10, 5))
print(is_even(4))
print(is_even(7))

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

squared = [n ** 2 for n in numbers]
print(squared)

student = {
    "name": "Lexi",
    "age": 18,
    "course": "Computer Science"
}

print(student["name"])
print(student["course"])

for key, value in student.items():
    print(key, ":", value)