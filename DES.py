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


def encodeDES():
    print("siema")

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

    print(keys_array)


test_list = ['3', '5', '7', '9', '11']


# for i in range(2):
#     test_list.append(test_list.pop(0))
# print(test_list)


key = "IEOFIT#1"
generate_keys(key)