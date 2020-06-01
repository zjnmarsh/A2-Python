dictionary = [[-1, ]] * 522


def print_dict():
    for i in range(len(dictionary)):
        print(dictionary[i])


def hash_function(to_hash):
    ans = 0
    for i in range(len(to_hash)):
        ans += ord(to_hash[i]) * ord(to_hash[i])
    hash = ans % 523
    return hash


def lookup():
    to_look = str(input("Enter english word to look up: "))
    hash = hash_function(to_look)
    print("Translation is: ", dictionary[hash][1])


lang_dict = [["PEN", "PLUME"], ["CAT", "CHAT"], ["NOW", "MAINTENANT"]]


def initialise():
    for word in lang_dict:
        key = word[0]
        hash = hash_function(key)
        dictionary[hash] = word


initialise()
lookup()
