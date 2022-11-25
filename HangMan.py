import random

word_list = ["baboon", "camel", "rat"]
end_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from hangman_art import logo
print(logo)
print(f"the solution is {chosen_word}")

lives = 6

display = []
for _ in range(word_length):
    display += "_"


while not end_game:

    guess = input("Please guess a letter from the list = ").lower()
    if guess in display:
        print(f"You have already guessed {guess} letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} letter,That is not in the list. You lost a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You die")



    if "_" not in display:
        end_game = True
        print("You win")
    from hangman_art import stage
    print(stage[lives])