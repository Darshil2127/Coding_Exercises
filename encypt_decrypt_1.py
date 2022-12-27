alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


direction = input("Type 'encode' to encrypt: , type 'decode' to decrypt: \n")
text = input("Type your message: \n").upper()
shift = int(input("Type the shift number you want to do: \n"))
shift = shift % 26
if direction == "encode":
    def encypt(plain_text,shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"Your encrypt message is: {cipher_text}")

    encypt(plain_text=text, shift_amount=shift)

else:

    def decrypt(plain_text,shift_amount):
        decrypt_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            decrypt_text += new_letter
        print(f"Your decrypt message is: {decrypt_text}")
    decrypt(plain_text=text, shift_amount=shift)