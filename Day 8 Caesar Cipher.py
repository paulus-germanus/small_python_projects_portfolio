alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift nubmer:\n"))

shift %= 26

def encrypt(input_text, shift_value):
    encrypted_text = ""
    for x in input_text:
        if x == " ":
            encrypted_text += x
        elif x.isnumeric():
            encrypted_text += x
        else:
            encrypted_text += alphabet[alphabet.index(x)+shift_value]
    print(f"Encrypted text: {encrypted_text}")

def decrypt(input_text, shift_value):
    decrypted_text = ""
    for x in input_text:
        if x == " ":
            decrypted_text += x
        elif x.isnumeric():
            decrypted_text += x
        else:
            decrypted_text += alphabet[alphabet.index(x)+shift_value]
    print(f"Decrypted text: {decrypted_text}")

if direction == "encode":
    encrypt(input_text=text, shift_value=shift)
elif direction == "decode":
    decrypt(input_text=text, shift_value=shift)
