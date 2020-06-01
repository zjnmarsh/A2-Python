class Yard:
    def __init__(self):
        self.siding1 = Siding()
        self.siding2 = Siding()



class Siding(Yard):
    def __init__(self):
        self.stackpointer = -1
        self.siding_array = [None] * 30

    def push(self):
        if self.stackpointer >= 29:
            print("you cannot add any more wagons")
        else:
            print("adding wagon")
            self.stackpointer += 1
            self.siding_array[self.stackpointer] = Wagon

    def pop(self):
        if self.stackpointer == -1:
            print("there are no wagons to remove")
        else:
            print("Wagon removed")
            self.stackpointer -= 1


class Wagon(Siding):
    pass


class OpenWagon(Wagon):
    pass


class ClosedWagon(Wagon):
    pass


yard = Yard()
wagon = Wagon()


#for i in range(31):
#     yard.siding1.push('wagon')

yard.siding1.push()
# print(yard.siding1.siding_array)
yard.siding1.pop()
yard.siding1.pop()

"""
Zebedee, this is very good and the code is nice and clear. The only problem is that the push() function doesn't
actually take a Wagon object as a parameter and save it to the list. Line 19,  
(self.siding_array[self.stackpointer] = Wagon) is adding the Wagon class to the list, not an instance of a Wagon.
pop() should also return the wagon that was stored at the top of the stack.
"""
