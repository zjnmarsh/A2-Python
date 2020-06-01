class Cipher():
    def __init__(self, option, read_file, write_file, shift, enigma):
        self.option = option
        self.read_file = read_file
        self.write_file = write_file
        self.shift = shift
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')
        self.enigma = enigma
        if option == 'decrypt':
            self.decrypt()
        if option == 'encrypt':
            self.encrypt()

    def reading_file(self):
        """Reads the file entered, returning the data in it"""
        with open(self.read_file, 'r') as file:
            data = file.read()
            new_data = data.lower().strip('\n')
        return new_data

    def writing_file(self,new_string):
        """Writes the new encrypted or decrypted string to the file entered"""
        with open(self.write_file, 'w') as file:
            file.write(new_string)

    def encrypt(self):
        """Encrypts the data"""
        usr_text_list = list(self.reading_file())
        new_string = ''
        for letter in usr_text_list:
            if letter == ' ':
                new_string = new_string + " "
            else:
                if self.enigma:
                    self.shift = self.shift + 1
                new_string = new_string + self.alphabet[(self.alphabet.index(letter) + self.shift) % len(self.alphabet)]
        self.writing_file(new_string)

    def decrypt(self):
        usr_text_list = list(self.reading_file())
        new_string = ''
        for letter in usr_text_list:
            if letter == ' ':
                new_string = new_string + ' '
            else:
                if self.enigma:
                    self.shift = self.shift + 1
                new_string = new_string + self.alphabet[(self.alphabet.index(letter) - self.shift) % len(self.alphabet)]
        self.writing_file(new_string)




cipher = Cipher
cipher('encrypt', 'encrypt_me.txt', 'write_to_me.txt', 4, True)
cipher('decrypt', 'write_to_me.txt', 'decrypt_to_me.txt', 4, True)
