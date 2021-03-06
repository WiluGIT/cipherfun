import math

permutated_choice = [
57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]

permutated_choice_2 = [
14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19, 12, 4, 26, 8,
16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55,
30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32
]

initial_permutation = [
58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7
]

extend_table = [
32, 1, 2, 3, 4, 5,
4, 5, 6, 7, 8, 9,
8, 9, 10, 11, 12, 13,
12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21,
20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32, 1
]

function_permutation = [
16, 7, 20, 21,
29, 12, 28, 17,
1, 15, 23, 26,
5, 18, 31, 10,
2, 8, 24, 14,
32, 27, 3, 9,
19, 13, 30, 6,
22, 11, 4, 25
]

initial_permutation_reverse = [
40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25
]

s1 = [
[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

s2 = [
[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

s3 = [
[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

s4 = [
[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

s5 = [
[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

s6 = [
[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

s7 = [
[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

s8 = [
[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

shift_table = [
1,
1,
2,
2,
2,
2,
2,
2,
1,
2,
2,
2,
2,
2,
2,
1]


def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def split_message_into_block(message):
    message_array =[]
    text_to_append = ""
    # split message into blocks
    for p in range(len(message)):
        text_to_append += message[p]
        if p == len(message)-1:
            message_array.append(text_to_append)
            text_to_append = ""
        elif p % 8 == 7:
            message_array.append(text_to_append)
            text_to_append = ""

    return message_array


def split_array_into_block(array):
    block_array = []
    array_elem = []
    for a in range(len(array)):
        array_elem.append(array[a])
        if a == len(array) - 1:
            block_array.append(array_elem)
            array_elem = []
        elif a % 8 == 7:
            block_array.append(array_elem)
            array_elem = []

    return block_array


def decodeDES(cipher_array, plain_key):
    # generate 16 keys
    keys_array = generate_keys(plain_key)

    # check number of DES blocks
    blocks_number = math.ceil((len(cipher_array) * 8) / 64)
    # split array into blocks
    cipher_block_array = split_array_into_block(cipher_array)

    block_result = []
    ascii_result = ""
    for b in range(blocks_number):
        # concatinate hex values converted to bin
        concat_bin_string = ""
        for i in range(len(cipher_block_array[b])):
            concat_bin_string += format(int(cipher_block_array[b][i], 16), '08b')

        # initial permutation
        bit_64_string = [0] * len(initial_permutation)
        for i in range(len(initial_permutation)):
            bit_64_string[i] = concat_bin_string[initial_permutation[i] - 1]

        left_part = bit_64_string[:32]
        right_part = bit_64_string[32:]

        extended_right = [0] * len(extend_table)

        counter = 15
        for i in range(16):
            # extending right part
            for j in range(len(extend_table)):
                extended_right[j] = right_part[extend_table[j] - 1]

            current_subkey = list(keys_array[counter])
            counter -= 1

            key_right_xor = [0] * len(extended_right)

            # xor current key with right part
            for j in range(len(extended_right)):
                key_right_xor[j] = int(extended_right[j]) ^ int(current_subkey[j])

            # split 48 bits to 8 x 6 blocks
            bit_6_string = ""
            split_48_bit = []
            for j in range(len(key_right_xor)):
                bit_6_string += str(key_right_xor[j])

                if j % 6 == 5:
                    split_48_bit.append(bit_6_string)
                    bit_6_string = ""

            block_string = ""
            for j in range(len(split_48_bit)):
                current_block = split_48_bit[j]
                row = current_block[0] + current_block[5]
                column = current_block[1] + current_block[2] + current_block[3] + current_block[4]

                # convert bin to index
                row_index = int(row, 2)
                column_index = int(column, 2)

                # get values for each block from s_table
                if j == 0:
                    s_value = s1[row_index][column_index]
                elif j == 1:
                    s_value = s2[row_index][column_index]
                elif j == 2:
                    s_value = s3[row_index][column_index]
                elif j == 3:
                    s_value = s4[row_index][column_index]
                elif j == 4:
                    s_value = s5[row_index][column_index]
                elif j == 5:
                    s_value = s6[row_index][column_index]
                elif j == 6:
                    s_value = s7[row_index][column_index]
                elif j == 7:
                    s_value = s8[row_index][column_index]

                block_string += format(s_value, '04b')

            # function permutation
            bit_32_string = [0] * len(function_permutation)
            for j in range(len(function_permutation)):
                bit_32_string[j] = block_string[function_permutation[j] - 1]

            new_right = [0] * len(right_part)
            for j in range(len(right_part)):
                new_right[j] = int(left_part[j]) ^ int(bit_32_string[j])

            left_part = right_part
            right_part = new_right

        final_array = right_part + left_part

        # initial permutation reverse
        final_string = [0] * len(initial_permutation_reverse)
        for k in range(len(initial_permutation_reverse)):
            final_string[k] = final_array[initial_permutation_reverse[k] - 1]

        hex_string = ""
        hex_array = []
        ascii_string = ""
        for k in range(len(final_string)):
            hex_string += str(final_string[k])
            if k % 8 == 7:
                hex_array.append(hex(int(hex_string, 2)))
                try:
                    ascii_string += bytes.fromhex(hex(int(hex_string, 2))[2:]).decode('utf-8')
                except ValueError:
                    pass
                hex_string = ""

        ascii_result += ascii_string
        block_result += hex_array

    print("Decoded hex value:")
    print(block_result)
    print("Decoded ASCII value:")
    print(ascii_result)
    # convert hex result to ASCII


def encodeDES(plaintext_message, plain_key):
    # generate 16 keys
    keys_array = generate_keys(plain_key)

    # check number of DES blocks
    blocks_number = math.ceil((len(plaintext_message)*8) / 64)

    # split message by blocks number
    message_array = split_message_into_block(plaintext_message)

    block_result = []
    for b in range(blocks_number):
        if len(message_array[b]) >= 8:
            # concatinate 8bit converted ascii values
            concat_bin_string = ""
            for i in range(len(message_array[b])):
                concat_bin_string += format(ord(message_array[b][i]), '08b')
        elif len(message_array[b]) < 8:
            diff = (8 - len(message_array[b])) * 8
            diff_string = "0" * diff
            concat_bin_string = ""
            for i in range(len(message_array[b])):
                concat_bin_string += format(ord(message_array[b][i]), '08b')
            concat_bin_string += diff_string

        # initial permutation
        bit_64_string = [0] * len(initial_permutation)
        for i in range(len(initial_permutation)):
            bit_64_string[i] = concat_bin_string[initial_permutation[i] - 1]

        left_part = bit_64_string[:32]
        right_part = bit_64_string[32:]

        extended_right = [0] * len(extend_table)

        for i in range(16):
            # extending right part
            for j in range(len(extend_table)):
                extended_right[j] = right_part[extend_table[j] - 1]

            current_subkey = list(keys_array[i])
            key_right_xor = [0] * len(extended_right)

            # xor current key with right part
            for j in range(len(extended_right)):
                key_right_xor[j] = int(extended_right[j]) ^ int(current_subkey[j])

            # split 48 bits to 8 x 6 blocks
            bit_6_string = ""
            split_48_bit = []
            for j in range(len(key_right_xor)):
                bit_6_string += str(key_right_xor[j])

                if j % 6 == 5:
                    split_48_bit.append(bit_6_string)
                    bit_6_string = ""

            block_string = ""
            for j in range(len(split_48_bit)):
                current_block = split_48_bit[j]
                row = current_block[0] + current_block[5]
                column = current_block[1] + current_block[2] + current_block[3] + current_block[4]

                # convert bin to index
                row_index = int(row, 2)
                column_index = int(column, 2)

                # get values for each block from s_table
                if j == 0:
                    s_value = s1[row_index][column_index]
                elif j == 1:
                    s_value = s2[row_index][column_index]
                elif j == 2:
                    s_value = s3[row_index][column_index]
                elif j == 3:
                    s_value = s4[row_index][column_index]
                elif j == 4:
                    s_value = s5[row_index][column_index]
                elif j == 5:
                    s_value = s6[row_index][column_index]
                elif j == 6:
                    s_value = s7[row_index][column_index]
                elif j == 7:
                    s_value = s8[row_index][column_index]

                block_string += format(s_value, '04b')

            # function permutation
            bit_32_string = [0] * len(function_permutation)
            for j in range(len(function_permutation)):
                bit_32_string[j] = block_string[function_permutation[j] - 1]

            new_right = [0] * len(right_part)
            for j in range(len(right_part)):
                new_right[j] = int(left_part[j]) ^ int(bit_32_string[j])

            left_part = right_part
            right_part = new_right

        final_array = right_part + left_part
        # initial permutation reverse
        final_string = [0] * len(initial_permutation_reverse)
        for k in range(len(initial_permutation_reverse)):
            final_string[k] = final_array[initial_permutation_reverse[k] - 1]

        hex_string = ""
        hex_array = []
        for k in range(len(final_string)):
            hex_string += str(final_string[k])
            if k % 8 == 7:
                hex_array.append(hex(int(hex_string, 2)))
                hex_string = ""

        block_result += hex_array

    print("Encoded hex value:")
    print(" ".join(block_result))
    return block_result


def generate_keys(plain_key):
    # concatinate 8bit converted ascii values
    concat_bin_string = ""
    for i in range(len(plain_key)):
        concat_bin_string += format(ord(plain_key[i]), '08b')

    # permutated choice permutation
    bit_56_string = [0] * len(permutated_choice)
    for i in range(len(permutated_choice)):
        bit_56_string[i] = concat_bin_string[permutated_choice[i]-1]

    left_part = bit_56_string[:28]
    right_part = bit_56_string[28:]

    keys_array = [0] * 16
    subkey = [0] * len(permutated_choice_2)
    for i in range(16):
        current_shift = shift_table[i]
        # shift bits by current_shift value
        for j in range(current_shift):
            left_part.append(left_part.pop(0))
            right_part.append(right_part.pop(0))

        # join 2 arrays
        joined_parts = left_part + right_part

        # permutated choice 2 permutation
        for k in range(len(permutated_choice_2)):
            subkey[k] = joined_parts[permutated_choice_2[k]-1]

        keys_array[i] = "".join(subkey)

    return keys_array


# key = "IEOFIT#1"
# plaintext = "FAFA$#CD@G"

# read key and message form binary files
with open("message.bin", "rb") as f:
    plaintext = f.read().decode('UTF-8')

with open("key.bin", "rb") as f:
    key = f.read().decode('UTF-8')


ciphertext = encodeDES(plaintext, key)
decodeDES(ciphertext, key)

# with open("message.bin", "wb") as file:
#     file.write(plaintext.encode('ascii'))




