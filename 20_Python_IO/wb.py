# filename = "test.txt"
# file = open(filename, 'wb')
# print(bytes([3]))
# file.write(bytes([3]))
# file.close()


# filename = "Squidward.txt"
# filename = "stormtrooper.txt"
#
# with open(filename, 'r') as file:
#     text = file.read()
#     print(text)

# with open(filename, 'r') as file:
#     for line in file:
#         # print(line)
#         #print(line, end='')
#         print(line.rstrip())

filename = "sampledata.csv"
# with open(filename, 'r') as file:
#     for line in file:
#         print(line)

with open(filename, 'r') as csv_file:
    for line in csv_file:
        print(line.rstrip().split(','))
        # print(line.split(','))
