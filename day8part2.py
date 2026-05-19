phrase = "the quick brown fox jumps over the lazy dog"

print(phrase.count("the"))
print(phrase.find("fox"))
print(phrase.index("jump"))

words = phrase.split()
print(len(words))
print(words[0])
print(words[-1])

new = phrase.replace("lazy", "happy")
print(new)

print(phrase.title())
print(phrase.capitalize())

code = "py-thon-is-fun"
parts = code.split("-")
print(parts)
joined = " ".join(parts)
print(joined)

username = "   lexi123   "
username = username.strip()
print(username.isalpha())
print(username.isalnum())
print(username[0].isupper())