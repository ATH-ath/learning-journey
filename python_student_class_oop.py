class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, Grade: {self.grade}")

    def is_passing(self):
        return self.grade >= 50


s1 = Student("Lexi", 18, 85)
s2 = Student("Alex", 17, 40)

s1.introduce()
s2.introduce()

print(s1.is_passing())
print(s2.is_passing())

students = [
    Student("Lexi", 18, 85),
    Student("Alex", 17, 40),
    Student("Sam", 19, 72),
]

for s in students:
    status = "Pass" if s.is_passing() else "Fail"
    print(s.name, "-", status)
