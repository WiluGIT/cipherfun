import math


def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def find_char(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def get_column(matrix,col,row_length):
    result = []
    for i in range(row_length):
        try:
            if matrix[i][col] != "-":
                result.append(matrix[i][col])
        except IndexError:
            i += 1

    return "".join(result)


def encode():
    text = "CHUJUZAJEBANYBEKAZCIEBIEBECZUNIA".replace(" ", "").upper()
    key = "CHUJOSTWO".upper()

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

    row_values = []
    counter = 0
    txt_pointer = 0

    # take rows and move through text with txt_pointer and append text within position of key chars
    for i in sort_dic:
        col_array = find_char(key, i)
        print(col_array)
        for j in range(len(col_array)):
            if txt_pointer < len(text):
                if col_array[j] == 0:
                    row_values.append(text[txt_pointer:1])
                    txt_pointer += 1
                else:
                    row_values.append(text[txt_pointer:txt_pointer + col_array[j] + 1])
                    txt_pointer += col_array[j] + 1

    row_count = len(row_values)

    # create matrix and populate while we know how many rows it has
    matrix = [["-" for i in range(col)] for i in range(row_count)]
    print_matrix(matrix)
    print(row_values)
    for i in range(row_count):
        for j in range(col):
            matrix[i] = row_values[i]



    print_matrix(matrix)
    result = []
    for i in sort_dic:
        col_array = find_char(key, i)
        for j in range(len(col_array)):
            result.append(get_column(matrix, col_array[j], row_count))
    print("Encoded result:")
    print("".join(result))

encode()