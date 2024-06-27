#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    """ validates UTF-8 encoding """

    # Step 1: turn data into binary
    bin_data = []
    for number in data:
        # step 1: convert number to binary string
        bin_str = bin(number)[2:]  # Remove '0b' prefix

        # step 2: ensure it's 8 bits long
        while len(bin_str) < 8:
            bin_str = '0' + bin_str

        bin_data.append(bin_str)

    # Step 2: Check UTF-8 encoding rules
    i = 0
    while i < len(bin_data):
        if bin_data[i].startswith('0'):
            # Single-byte character
            i += 1
        elif bin_data[i].startswith('110'):
            # Two-byte character
            if i + 1 >= len(bin_data) or not bin_data[i + 1].startswith('10'):
                return False
            i += 2
        elif bin_data[i].startswith('1110'):
            # Three-byte character
            if (i + 2 >= len(bin_data) or
                    not bin_data[i + 1].startswith('10') or
                    not bin_data[i + 2].startswith('10')):
                return False
            i += 3
        elif bin_data[i].startswith('11110'):
            # Four-byte character
            if (i + 3 >= len(bin_data) or
                    not bin_data[i + 1].startswith('10') or
                    not bin_data[i + 2].startswith('10') or
                    not bin_data[i + 3].startswith('10')):
                return False
            i += 4
        else:
            # Invalid start of UTF-8 character
            return False

    return True
