import random

names_list = input("Give me everybody's names , seperated by a comma\n")

names = names_list.split(", ")
print(names)

items = len(names)
random_person = random.randint(0, items -1)
print(random_person)

person = names[random_person]
print(f"{person} will pay the bill")
# import random
# names_list = input("Give me everybody's names , seperated by a comma\n")
#
# names = names_list.split(", ")
# person = random.choice(names)
#
# print(f"{person} will pay for the bill")