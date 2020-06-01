def append_to(internal_list):
    internal_list.append(1)
    print(internal_list)

list = [0]

append_to(list)
print(list)

#Python - Passing by reference
# Within the function, you have the same variable (which could have the same name)
