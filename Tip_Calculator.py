print("Welcome to the bill calculator\n")
total = float(input("What was the total bill? $\n"))
person = int(input("How many person you want to split the bill from?\n"))
tip = int(input("What percentage tip you would like to give? 10, 12 or 15?\n"))

total_with_tip = total + (total*tip)/100
print("The split amount will be = ", total_with_tip/person)

