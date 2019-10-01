#Have user type a sentence
message = input("Type a sentence. :" +'\n')

#create an empty dict to add counts to
char_count = {}

#loop over each character in the sentence
for cur_char in message:
    if cur_char in char_count:
        char_count[cur_char] += 1
    #if cur_char doesn't exist, add one
    else:
        char_count[cur_char] = 1


#print each key, value pair        
for char in sorted(char_count):
    print(char, char_count[char])
