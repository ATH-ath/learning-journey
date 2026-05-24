name = "Lexi"
age = 18
gpa = 8.5
is_student = True

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is Student:", is_student)

user_name = input("\nEnter your name: ")
print("Hello,", user_name + "!")

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nEven numbers below 10:")
num = 2
while num < 10:
    print(num)
    num += 2

fruits = ["apple", "banana", "mango"]
print("\nFruits list:")
for fruit in fruits:
    print("-", fruit)
