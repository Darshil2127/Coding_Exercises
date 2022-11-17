# body mass index 2.0

height = float(input("Please enter your height in m = "))
weight = float(input("Please enter your weight in KG = "))

bmi = weight/(height**2)
print("Your BMI is =", bmi)

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("They are overweight")
elif bmi < 35:
    print("They are obese")
else:
    print("They are clinically obese")