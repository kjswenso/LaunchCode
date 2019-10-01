import string

def alphabet_position(letter):
    """Get the numerical position of a given letter in the alphabet"""

    #create index base
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #uniform to get index of any letter
    letter = letter.lower()
    return alphabet.index(letter)

def rotate_character(char, rot):
    """Return a character rotated by a given amount"""
    
    #create index base
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #empty string to store character for translation
    translated_char = "" 
    
    #grab only the alpha characters, not digits or punctuation, etc
    if char.isalpha():
        new_index = (alphabet_position(char) + rot) % 26
    
        translated_char = alphabet[new_index]
    #all other characters get replaced as themselves    
    else: 
        translated_char = char

    #if the original character is uppercase, transform it back to uppercase
    if char in string.ascii_uppercase:
        translated_char = translated_char.upper()

    return translated_char