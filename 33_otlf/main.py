# with open("scores_v2.otl", "rb") as f:
# with open("scores.otl", "rb") as f:
with open("test.bin", "rb") as f:

    def read_next_bit(x):
        return int.from_bytes(f.read(x), byteorder='big', signed=False)

    signature_bytes = f.read(4)
    signature = signature_bytes.decode("utf-8")
    # print(signature)
    assert signature == "OTLF"
    f.read(1)

    format_version = read_next_bit(1)
    number_of_scores = read_next_bit(1)
    print(f'There are {number_of_scores} scores')

    for i in range(number_of_scores):
        f.read(1)
        if format_version == 1:
            print(f'Player ID: {str(read_next_bit(1))}, Score: {str(read_next_bit(1))}')
        elif format_version == 2:
            name_length = read_next_bit(1)
            # print(name_length)
            player_name = ''
            for letter in range(name_length):
                player_name += (f.read(1)).decode('utf8')
            player_score = read_next_bit(4)
            print(f'Player name: {player_name}, Score: {player_score}')
