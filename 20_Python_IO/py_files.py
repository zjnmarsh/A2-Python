filename = "file_1.txt"

with open(filename, 'w+') as file:
    file.write("testing...")

filename = "file_2.txt"

with open(filename, 'a+') as file:
    file.write("testing...")

filename = "file_2.txt"

with open(filename, 'r+') as file:
    file.write("testing...")

