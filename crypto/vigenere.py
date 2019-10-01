from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    """Translate the entire string based upon the rotation given"""

    #empty variable for storing new, fully translated string
    encrypted_str = ""

    #initialize variables for key to rot conversion
    i = 0
    letter = ""
    rot = 0

    #loop over each character in the given string and add it to the new string
    for char in text:
        if char.isalpha():
            #if char is alpha -> if i is greater than the length of the key index, get the modulus 
            #this rotates through the letters
            if i > len(key) - 1:
                i = i % len(key)
            #store the letter that will be setting the rotation
            letter = key[i]
            #get the position of that letter to be used as the rotation number
            rot = alphabet_position(letter)
            #increase i to continue looping over the key
            i += 1
            
        #create new encrypted string
        encrypted_str += rotate_character(char, rot)
        
    return encrypted_str

def main():
    #get message to translate from user
    message = input("What would you like to encrypt? :" + '\n')
    #get the key for rot amount from user
    key = input("Word that will be used as your encryption key? :" + '\n')
    #print mesage so user can see
    print(encrypt(message, key))

if __name__ == "__main__":
    main()