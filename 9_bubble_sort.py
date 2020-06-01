list = []
length_list = int(input("Enter number of objects in list you want to sort"))
for i in range(length_list):
    list.append(input())




# list = [5,2,87,2,3,4,5]

length_list = len(list)
unsorted = True

while unsorted == True:
    no_changes = 0
    for i in range(length_list-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            no_changes += 1
    print(list)
    if no_changes == 0:
        break
