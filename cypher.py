def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

power = True

while power == True:
    check = False
    while check == False:
        choice = input("would you like to \n1.encrypt \n2.decrypt\n")
        if choice == "1":
            check = True
        elif choice == "2":
            check = True
        else:
            print("Error invalid input")

        
    if choice == "1":
        text = input("What would you like to encrypt?\n")
        custom_key = input("What is the custom key?\n")
        product = encrypt(text, custom_key)
    else:
        text = input("What would you like to decrypt?\n")
        custom_key = input("What is the custom key?\n")
        product = decrypt(text, custom_key)
    print(f'\nText: {text}')
    print(f'Key: {custom_key}')
    print(f'Product: {product}')

    stay = input("\nDo you want to continue using this program? (y/n)\n")

    if stay == "y":
        power = True
    elif stay == "n":
        power = False
    else:
        print("Error invalid input")
        stay = input("\nDo you want to continue using this program? (y/n)\n")
