morse_dictionary = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  '.': '.-.-.-', ',': '--..--',
        '?': '..--..'
        }

letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

new_letter = ""



def morse_translate():
    outloop = False
    while outloop == False:
        to_translate = str(input("What would you like to translate? "))
        to_translate = to_translate.upper()
        for i in range(len(to_translate)):
            if to_translate[i] not in morse_dictionary:
                print("You've inputted an illegal character. Please try again")
            else:
                if i == (len(to_translate)-1):
                    outloop = True

    final = ''
    for i in range(len(to_translate)):
        new_letter = morse_dictionary[to_translate[i]]
        final = final + new_letter + ' '
    return(final)




ask = str(input("English --> Morse (em) or Morse --> English(me)?"))

def english_to_morse():
    f = open("translation.txt","a+")
    f.write(morse_translate())
    f.write("\n")
    f.close()
    return()

def morse_to_english():
    f = open("to_translate.txt","r")
    contents = f.read()
    rev_dict = {v: k for k, v in morse_dictionary.items()}
    new_contents = contents.split()




