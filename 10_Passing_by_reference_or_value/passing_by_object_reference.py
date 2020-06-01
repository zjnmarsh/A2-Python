def change_list(internal_list1, internal_list2):
    internal_list1.append(1)
    internal_list2 = [3,2,1]
    print("internal_list1 = ", internal_list1)
    print("internal_list2 = ", internal_list2)

list1 = [0]
list2 = [5]
change_list(list1, list2)
print("list1 = ", list1)
print("list2 = ", list2)

