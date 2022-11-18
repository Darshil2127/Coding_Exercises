print("Welcome to the Love calculator")

name1 = input("Please enter his name = ").lower()
name2 = input("Please enter her name = ").lower()

combined_string = name1+name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_string = str(true) + str(love)
print(love_string)

int_love_string = int(love_string)
print(type(int_love_string))

if (int_love_string < 10) or (int_love_string > 90):
    print(f"Your score is {int_love_string}. you go together like coke and mentos")


elif (int_love_string >= 40) and (int_love_string <= 50):
    print(f"Your score is {int_love_string}. you are alright together.")

else:
    print(f"Your score is {int_love_string}")

