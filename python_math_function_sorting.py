def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cant divide by zero"
    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))


def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(is_even(4))
print(is_positive(-3))
print(factorial(5))


numbers = [5, 2, 8, 1, 9, 3]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

words = ["banana", "apple", "mango"]
print(sorted(words))
