alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
should_countinue = True
while should_countinue:

    direction = input("Type 'encode' to encrypt: , type 'decode' to decrypt: \n")
    text = input("Type your message: \n").upper()
    shift = int(input("Type the shift number you want to do: \n"))
    shift = shift % 26

    def cypher_text(plain_text, shift_amount, cypher_direction):
        if cypher_direction == "decode":
            shift_amount = shift_amount * -1
        cypher_message = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cypher_message += new_letter
            else:
                cypher_message += char
        print(f"Your {direction}d message is: {cypher_message}")

    cypher_text(plain_text=text, shift_amount=shift, cypher_direction=direction)

    result = input("Type 'Yes' for go again, Type 'No' for exit \n").lower()
    if result == "no":
        should_countinue = False
        print("Good Bye")