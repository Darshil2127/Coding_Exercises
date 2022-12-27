import random


rock = ('''   
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 
 ''')
paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')
scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game_images = [rock, paper, scissor]
user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid input")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print(game_images[computer_choice])

    print(computer_choice)
    if user_choice == 2 and computer_choice == 0:
        print("Computer won")
    elif user_choice == 0 and computer_choice == 2:
        print("User won")
    elif computer_choice > user_choice:
        print("Computer won")
    elif user_choice > computer_choice:
        print("User won")
    else:
        print("The game is tie")



