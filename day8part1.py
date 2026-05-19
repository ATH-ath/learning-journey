name = "  hello world  "
print(name.strip())
print(name.upper())
print(name.lower())
print(name.replace("world", "python"))

sentence = "my name is lexi"
words = sentence.split()
print(words)
print(len(words))

print(sentence.startswith("my"))
print(sentence.endswith("lexi"))
print("lexi" in sentence)

email = "lexi@gmail.com"
print(email.split("@")[0])
print(email.split("@")[1])

name = "lexi"
age = 18
print(f"my name is {name} and i am {age} years old")
print("my name is {} and i am {} years old".format(name, age))

password = "python123"
print(len(password))
print(password[0:6])
print(password[::-1])