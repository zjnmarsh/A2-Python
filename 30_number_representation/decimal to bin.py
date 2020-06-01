def dec_to_bin(dec):
    bin = ''
    while dec >= 1:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

def dec_to_hex(dec):
    alphabet = list('0123456789ABCDEF')
    hex = ''
    while dec >= 1:
        hex = str(alphabet[dec % 16]) + hex
        dec = dec // 16
    return hex


# print(dec_to_bin(1000))
print(dec_to_hex(22000))

d
