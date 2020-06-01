with open("scores.otl", "rb") as f:
    i = 0

    """
    while byte != b'H':
        print(byte)
        if byte != [b'O',b'T',b'L',b'F'][i]:
            print("Incorrect file signature")
        i += 1
        byte = f.read(1)
    """

    signature_bytes = f.read(4)
    signature = signature_bytes.decode("utf-8")
    assert signature == "OTLF"

    f.read(1)

    big = 'big'

    format_version = int.from_bytes(f.read(1), byteorder='big', signed=False)
    assert format_version == 1
    number_scores = int.from_bytes(f.read(1), byteorder='big', signed=False)
    # print(f'format version {format_version} and number scores {number_scores}')
    for i in range(number_scores):
        f.read(1)
        print(f'Player ID: {str(int.from_bytes(f.read(1), byteorder=big, signed=False))} Score: {str(int.from_bytes(f.read(1), byteorder=big, signed=False))}')

