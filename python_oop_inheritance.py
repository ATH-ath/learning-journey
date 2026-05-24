class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        print(f"{self.name} says Tweet!")

    def describe(self):
        if self.can_fly:
            print(f"{self.name} can fly")
        else:
            print(f"{self.name} cannot fly")


d = Dog("Bruno")
c = Cat("Whiskers")
b = Bird("Tweety", True)
p = Bird("Penguin", False)

d.speak()
c.speak()
b.speak()
b.describe()
p.describe()

animals = [Dog("Rex"), Cat("Luna"), Dog("Max")]
for animal in animals:
    animal.speak()
