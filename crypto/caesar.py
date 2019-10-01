from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    """Translate the entire string based upon the rotation given"""

    #empty variable for storing new, fully translated string
    encrypted_str = ""
    #loop over each character in the given string and add it to the new string
    for char in text:
        encrypted_str += rotate_character(char, rot)

    return encrypted_str

def main():
    #get message to translate from user
    message = input("What would you like to encrypt? :" + '\n')
    #get the rot amount from user
    rot = int(input("How many letters should we rotate your message?" + '\n'))
    #print mesage so user can see
    print(encrypt(message, rot))

if __name__ == "__main__":
    main()