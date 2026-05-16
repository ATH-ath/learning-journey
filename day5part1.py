try:
    num = int(input("enter a number: "))
    print(100 / num)
except ValueError:
    print("thats not a number")
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("done")


nums = [10, 20, 30]
try:
    print(nums[5])
except IndexError:
    print("no item at that index")


f = open("notes.txt", "w")
f.write("hello this is day 5\n")
f.write("learning file stuff\n")
f.close()

f = open("notes.txt", "r")
print(f.read())
f.close()

f = open("notes.txt", "a")
f.write("added this line later\n")
f.close()

f = open("notes.txt", "r")
for line in f:
    print(line.strip())
f.close()