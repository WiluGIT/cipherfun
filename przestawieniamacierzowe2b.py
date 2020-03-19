import math


def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def find_char(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def get_column(matrix,col,row_length):
    result = []
    for i in range(row_length):
        if matrix[i][col] != "-":
            result.append(matrix[i][col])
    return "".join(result)


def populate_column(matrix, col, col_list, col_elem):
    for i in range(len(col_list[col_elem])):
        matrix[i][col] = col_list[col][i]


# def decode():
#     text = "BAEUKIOCBPWCOUEJHYLZC".replace(" ", "").upper()
#     key = "CONVENIENCE".upper()
#
#     # get number of occurance in key to dictionary
#     _dic = {}
#     for i in range(len(key)):
#         counter = 1
#         for j in range(i + 1, len(key)):
#             if key[i] == key[j]:
#                 counter += 1
#         if _dic.get(key[i]) == None:
#             _dic[key[i]] = counter
#
#     # sort dic
#     sort_dic = {}
#     for i in sorted(_dic):
#         sort_dic.update({i: _dic[i]})
#
#     print(sort_dic)
#
#
#     col = len(key)
#     row = int(math.ceil(len(text) / col))
#     rest = len(text) % col
#
#     # populate matrix with -
#     matrix = [["-" for i in range(col)] for i in range(row)]
#     print_matrix(matrix)
#     col_list = []
#     elem = []
#     index = 0
#     counter = 0
#
#     for i in range(len(text)):
#         counter += 1
#         if index < rest:
#             if counter < row:
#                 elem.append(text[i])
#             elif counter == row:
#                 elem.append(text[i])
#                 index += 1
#                 counter = 0
#                 col_list.append(elem)
#                 elem = []
#         else:
#             if counter < row - 1:
#                 elem.append(text[i])
#             elif counter == row - 1:
#                 elem.append(text[i])
#                 counter = 0
#                 col_list.append(elem)
#                 elem = []
#
#
#     counter = 0
#     for i in sort_dic:
#         col_array = find_char(key, i)
#         for j in range(len(col_array)):
#             for k in range(len(col_list[counter])):
#                 matrix[k][col_array[j]] = col_list[counter][k]
#
#             counter += 1
#
#     print("Populated final matrix: ")
#     print_matrix(matrix)
#
#     decoded_result = []
#     index = 0
#     for i in range(row):
#         for j in range(col):
#             if index < len(text):
#                 decoded_result.append(matrix[i][j])
#                 index += 1
#
#     print("Decoded result: \n{}".format("".join(decoded_result)))
#

def encode(text, key):
    # get number of occurance in key to dictionary
    _dic = {}
    for i in range(len(key)):
        counter = 1
        for j in range(i + 1, len(key)):
            if key[i] == key[j]:
                counter += 1
        if _dic.get(key[i]) == None:
            _dic[key[i]] = counter

    # sort dic
    sort_dic = {}
    for i in sorted(_dic):
        sort_dic.update({i: _dic[i]})

    print(sort_dic)

    # create matrix
    col = len(key)
    text_len = float(len(text))
    row = int(math.ceil(text_len / col))

    # populate matrix with -
    matrix = [["-" for i in range(col)] for i in range(row)]

    # populate matrix with word

    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1
    print_matrix(matrix)

    # get columns according to dic

    result = []
    for i in sort_dic:
        col_array = find_char(key, i)
        for j in range(len(col_array)):
            result.append(get_column(matrix, col_array[j], row))
    print("Encoded result:")
    print("".join(result))


def decode2(text, key):
    # algorithm works even if we have situation like:
    # a c d ....
    # b - b

    # get number of occurance in key to dictionary
    _dic = {}
    for i in range(len(key)):
        counter = 1
        for j in range(i + 1, len(key)):
            if key[i] == key[j]:
                counter += 1
        if _dic.get(key[i]) == None:
            _dic[key[i]] = counter

    # sort dic
    sort_dic = {}
    for i in sorted(_dic):
        sort_dic.update({i: _dic[i]})

    print(sort_dic)


    col = len(key)
    row = int(math.ceil(len(text) / col))
    rest = len(text) % col

    # populate matrix with -
    matrix = [["-" for i in range(col)] for i in range(row)]
    col_list = []
    elem = []
    index = 0
    counter = 0

    for i in range(len(text)):
        counter += 1
        if index < rest:
            if counter < row:
                elem.append(text[i])
            elif counter == row:
                elem.append(text[i])
                index += 1
                counter = 0
                col_list.append(elem)
                elem = []
        else:
            if counter < row - 1:
                elem.append(text[i])
            elif counter == row - 1:
                elem.append(text[i])
                counter = 0
                col_list.append(elem)
                elem = []


    if rest != 0:
        # code to insert - to places that needs it
        counter = 0
        merge_flag = 0
        for i in sort_dic:
            col_array = find_char(key, i)
            for j in range(len(col_array)):

                if col_array[j] >= rest:
                    tmp = "-"
                    if len(col_list[counter]) == row - 1:
                        col_list[counter].append(tmp)
                    else:
                        if merge_flag:
                            indexOf = col_list[counter].index(col_list[counter][row - 1])
                            col_list[counter].insert(indexOf - 1, tmp)
                            merge_flag = 0
                        else:
                            indexOf = col_list[counter].index(col_list[counter][row - 1])
                            col_list[counter].insert(indexOf, tmp)
                            merge_flag = 1

                counter += 1

    counter = 0
    # join 2d array
    # li2 = sum(col_list, [])
    # full_text = ''.join(li2)
    # col_list = []
    # elem = []
    # index = 0

    # for i in range(len(full_text)):
    #     counter += 1
    #     if counter < row:
    #         elem.append(full_text[i])
    #     elif counter == row:
    #         elem.append(full_text[i])
    #         index += 1
    #         counter = 0
    #         col_list.append(elem)
    #         elem = []
    # counter = 0

    for i in sort_dic:
        col_array = find_char(key, i)
        for j in range(len(col_array)):
            for k in range(len(col_list[counter])):
                matrix[k][col_array[j]] = col_list[counter][k]

            counter += 1

    print("Populated final matrix: ")
    print_matrix(matrix)

    decoded_result = []
    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                decoded_result.append(matrix[i][j])
                index += 1

    print("Decoded result: \n{}".format("".join(decoded_result)))


key = "CONVENIENCE".upper()
plaintext = "HERE IS A SECRET MESSAGE ENCIPHERED BY TRANSPOSITION".replace(" ", "").upper()
ciphertext = "HECRNCEYIISEPSGDIRNTOAAESRMPNSSROEEBTETIAEEHS".replace(" ", "").upper()

encode(plaintext, key)
decode2(ciphertext, key)
#decode()