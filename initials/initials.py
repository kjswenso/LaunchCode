def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    
    name_array = fullname.upper().split()

    initials = ""

    for name in name_array:
       initials += name[0]
       
    print(initials)

def main():

    get_initials(input("What is your name?" + '\n'))

if __name__ == "__main__":
    main()

