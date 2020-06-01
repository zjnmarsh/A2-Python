alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt():
    usr_text = str(input("Enter string to be encrypted: "))
    usr_text.lower()
    cipher = int(input("Enter number to shift by (up to 26): "))
    usr_list = list(usr_text)

    new_string = ''
    for i in range(len(usr_list)):
        letter = usr_list[i]
        if letter == " ":
            new_string = new_string + " "
        else:
            new_string = new_string + alphabet[alphabet.index(letter) + cipher]

    return new_string


def decrypt():
    usr_text = str(input("Enter string to be decrypted: "))
    usr_text.lower()
    cipher = int(input("Enter number to shift by: "))
    usr_list = list(usr_text)

    new_string = ''
    for i in range(len(usr_list)):
        letter = usr_list[i]
        if letter == " ":
            new_string = new_string + " "
        else:
            new_string = new_string + alphabet[alphabet.index(letter) - cipher]

    return new_string


print(encrypt())
print(decrypt())
