'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def translate(message: str, key: int) -> str:
    """
    Does a rot-key of the given message.
    """
    translation = []
    for letter in message:
        if letter.lower() in ALPHABET:
            index = ALPHABET.find(letter.lower())
            translated_letter = ALPHABET[(index + key) % 26]
            # keep the original letter case
            if letter.islower():
                translation.append(translated_letter)
            else:
                translation.append(translated_letter.upper())
        else:
            translation.append(letter)

    return "".join(translation)


if __name__ == "__main__":
    message = input("Enter the message to decrypt.\n")
    key = 1
    while key <= 26:
        print(f"Attempting decryption with key {key}:")
        # as a convention, using the opposite key to decode 
        # so that `key` is the one used for encryption
        print(translate(message, -key))
        decoded = input("Was the message decrypted? y/[n]\n").lower() 
        if decoded == "y":
            break
        key += 1
