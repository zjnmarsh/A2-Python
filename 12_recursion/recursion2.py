# def vertical(n):
#     if n < 10:
#         print(n)
#     else:
#         vertical(n//10)
#         print(n%10)

# def vertical(n):
#     """Reverses the function"""
#     if n < 10:
#         print(n)
#     else:
#         print(n % 10)
#         vertical(n//10)
#         print(n)
#
# vertical(43579)

# def cheers(n):
#     if n == 0:
#         print('Hurray!!')
#     else:
#         print('Hip')
#         cheers(n - 1)



to_print = ''

def cheers(n):
    if n == 0:
        to_print = to_print + 'Hurray!!'

    else:
        to_print = to_print + 'Hip'
        cheers(n - 1)




cheers(5)

