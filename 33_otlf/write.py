def version2():
    file.write(bytes([0x02]))
    player_list = [['Ruben', 2205745408], ['Bosch', 2138898432], ['Steve', 2908291072]]
    file.write(bytes([len(player_list)]))
    for record in player_list:
        file.write(bytes('S', 'utf8'))
        file.write(bytes([len(record[0])]) + bytes(record[0], 'utf8'))

        file.write((record[1]).to_bytes(4, byteorder='big', signed=False))

with open('test.bin', 'wb') as file:
    file.write(bytes("OTLFH", 'utf8'))
    version2()
