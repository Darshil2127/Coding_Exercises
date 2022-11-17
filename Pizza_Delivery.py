print("Welcome to Pizza Delivery app")
print("Small pizza: $15, Medium Pizza: $20, Large Pizza : $25")


size = input("what size of the pizza you want? S, M, L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you want to add extra cheese? Y or N ")

bill = 0
if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "Y":
    bill = bill + 1

print("Your bill is = ", bill)