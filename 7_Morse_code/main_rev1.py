# JTT feedback:
# Perhaps add a command-line print() as well, to see the result of the translation immediately?
# Nice use of dictionary and subroutines, though, very clear code.

morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
                    'D': '-..', 'E': '.', 'F': '..-.',
                    'G': '--.', 'H': '....', 'I': '..',
                    'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-', 'R': '.-.',
                    'S': '...', 'T': '-', 'U': '..-',
                    'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..',

                    '0': '-----', '1': '.----', '2': '..---',
                    '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..',
                    '9': '----.', '.': '.-.-.-', ',': '--..--',
                    '?': '..--..', ' ': ' '
                    }

letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

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
                if i == (len(to_translate) - 1):
                    outloop = True

    final = ''
    for i in range(len(to_translate)):
        new_letter = morse_dictionary[to_translate[i]]
        final = final + new_letter + ' '
    return (final)

def english_to_morse():
    f = open("translation.txt", "a+")
    f.write(morse_translate())
    f.write("\n")
    f.close()
    return ()


def morse_to_english():
    f = open("to_translate.txt", "r")
    contents = f.read()
    f.close()
    rev_dict = {v: k for k, v in morse_dictionary.items()}
    new_contents = contents.split()
    final = ''
    for i in range(len(new_contents)):
        new_letter = rev_dict[new_contents[i]]
        final = final + new_letter + ' '
    f = open("translation.txt", "a+")
    f.write(final)
    f.write("\n")
    f.close()
    return ()


ask = str(input("English --> Morse (em) or Morse --> English(me)?"))
if ask == 'em':
    english_to_morse()
elif ask == 'me':
    morse_to_english()
else:
    print("Invalid input, try again")




