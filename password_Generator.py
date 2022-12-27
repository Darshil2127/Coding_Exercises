import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
           'R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>']

print("Welcome to Password Generator")
nr_letter = int(input("How many letters you want to add? "))
nr_number = int(input("How many numbers you want to add? "))
nr_symbol = int(input("How many symbols you want to add? "))

password = []

for char in range(1, nr_letter+1):
    password += random.choice(letters)

for char in range(1, nr_number+1):
    password += random.choice(numbers)

for char in range(1, nr_symbol+1):
    password += random.choice(symbols)

print(password)
random.shuffle(password)
print(password)

strong_password = ""
for i in password:
    strong_password += i

print(f"your password is {strong_password}")





