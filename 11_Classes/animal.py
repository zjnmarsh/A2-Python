
class Animal():

    def __init__(self,s,n,a,):
        self._state = s
        self._size = n
        self._animals = a

    def feed(self):
        """You must feed the piggy to make it full"""
        self._size += 1
        print("Piggy fed")
        if self._size > 9:
            self._state = "Full"
            print("Piggy",self._state)

    def mate(self,the_mate):
        """You must mate the pig with something comptaible"""
        self._mate = the_mate
        if self._mate == "Piggy":
            self._animals += 1
            print(self._animals)
            print("Oink")
        else:
            self._state = "Not happy"
            print("Piggy", self._state)

    def speak(self):
        """Make the piggy speak"""
        self._state = "Tired"
        print("Squeal")


animal = Animal("Happy",8, 2)
animal.feed()
animal.feed()
animal.mate("Hippo")
animal.speak()

# help(animal.feed)
# help(animal.mate)
# help(animal.speak)
print("################################")

help(animal)

# JTT feedback:
# Nice, succinct docstrings.
