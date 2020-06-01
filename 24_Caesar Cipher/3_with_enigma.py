alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def read_file():
    filename = str(input("Enter file name to read: "))
    with open(filename, 'r') as file:
        data = file.read()
        new_data = data.lower()
        new_data = data.strip('\n')
    return new_data


def write_file(new_string):
    filename = str(input("Enter file name to write to: "))
    with open(filename, 'w') as file:
        file.write(new_string)


def encrypt():
    usr_text = read_file()
    cipher = int(input("Enter number to shift by (up to 26): "))
    usr_list = list(usr_text)

    new_string = ''
    for i in range(len(usr_list)):
        letter = usr_list[i]
        if letter == " ":
            new_string = new_string + " "
        else:
            cipher = cipher + 1
            new_string = new_string + alphabet[(alphabet.index(letter) + cipher) % len(alphabet)]

    write_file(new_string)


def decrypt():
    usr_text = read_file()
    cipher = int(input("Enter number to shift by: "))
    usr_list = list(usr_text)

    new_string = ''
    for i in range(len(usr_list)):
        letter = usr_list[i]
        if letter == " ":
            new_string = new_string + " "
        else:
            cipher = cipher + 1
            new_string = new_string + alphabet[(alphabet.index(letter) - cipher) % len(alphabet)]

    write_file(new_string)


# print(encrypt())
print(decrypt())
