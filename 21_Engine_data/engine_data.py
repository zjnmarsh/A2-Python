class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def display_engine(self):
        print(f"Engine name: {self.name}, weight: {self.weight}, colour: {self.colour}")


def engines_list = []:
    engines_list.append(Engine('Thomas', 600, 'blue'))
    engines_list.append(Engine('James', 650, 'red'))
    engines_list.append(Engine('Edward', 1000, 'blue'))
    engines_list.append(Engine('Gordon', 2500, 'blue'))
    engines_list.append(Engine('Henry', 2100, 'green'))
return engines_list

# ----------------------------------------

# Add engines to CSV
filename = "trains.csv"
with open(filename, 'w') as file:
    file.write("Engine_name, Weight, Colour\n")
    for e in engines_list:
        file.write(e.name + ", " + str(e.weight) + ", " + e.colour + "\n")


# Add additional engine to CSV
def add_engine():
    with open('trains.csv', 'a') as file:
        name = str(input("Enter name"))
        weight = str(input("Enter weight"))
        colour = str(input("Enter colour"))
        file.write(name + ", " + str(weight) + ", " + colour + "\n")


add_engine()

# ----------------------------------------

# Read a CSV file and create appropriate objects

filename = 'trains.csv'

engines2_list = []

with open(filename, 'r') as file:
    for line in file:
        info = line.replace(",", "").split()
        engines2_list.append(Engine(info[0], info[1], info[2]))


for e in engines2_list:
    e.display_engine()

