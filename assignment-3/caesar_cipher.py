'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

def translate(message: str, key: int) -> str:
    """
    Does a rot-key of the given message.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translation = []
    for letter in message:
        
        if letter.lower() in alphabet:
            index = alphabet.find(letter.lower())
            # rotate the letter by the key, wrapping around if necessary
            translated_letter = alphabet[(index + key) % 26]
            # preserve the case from the original message
            translated_letter = translated_letter if letter.islower() else translated_letter.upper()
            translation.append(translated_letter)
        
        else:
            # non alphabetic characters are left as is
            translation.append(letter)

    return "".join(translation)


if __name__ == "__main__":
    
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt?\n").lower()
        if mode in ("e", "d"):
            break
        else:
            print("Sorry I couldn't understand you, please try again.")

    while True:
        try:
            key = int(input("Please enter the key (0 to 25) to use.\n"))
            if key in range(26):
                break
            else:
                print("Number out of bounds, please try again.")
        except ValueError:
            print("Invalid choice, please try again.")
            
    if mode == "e":
        message = input("Enter the message to encrypt.\n")
    else:
        message = input("Enter the message to decrypt.\n")

    if mode == "e":
        print(translate(message, key))
    else:
        # decoding is just using the inverse key
        print(translate(message, -key))
