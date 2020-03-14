
def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def encode():
    key = "3-4-1-5-2"
    d = 5
    text = "CRYPTOGRAPHYOSA"
    keyordred = "".join(key.split("-"))
    rest = len(text) % d
    col = len(keyordred)
    row = 0
    if rest == 0:
        row = int(len(text) / d)
    else:
        row = int(len(text) / d) + 1

    print("matrix size c:{0} r:{1}".format(col, row))
    # populate array with -
    matrix = [["-" for i in range(col)] for i in range(row)]

    print("Matrix with -")
    print_matrix(matrix)

    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    print("Matrix with word")
    print_matrix(matrix)

    result = []

    for i in range(row):
        for j in range(len(keyordred)):
            if matrix[i][int(keyordred[j]) - 1] != "-":
                result.append(matrix[i][int(keyordred[j]) - 1])

    print("Encoded result:")
    print("".join(result))

def decode():
    key = "3-4-1-5-2"
    d = 5
    text = "YPCTRRAOPGOSHAY"
    keyordred = "".join(key.split("-"))
    rest = len(text) % d
    col = len(keyordred)
    row = 0
    if rest == 0:
        row = int(len(text) / d)
    else:
        row = int(len(text) / d) + 1

    print("matrix size c:{0} r:{1}".format(col, row))
    # populate array with -
    matrix = [["-" for i in range(col)] for i in range(row)]
    print("Matrix with -")
    print_matrix(matrix)

    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    print("Matrix with word")
    print_matrix(matrix)

    result = []

    for i in range(row):
        element = {}
        for j in range(len(keyordred)):
            if rest == 0:
                elementkey = int(keyordred[j]) - 1
                element[elementkey] = matrix[i][j]
            else:
                if i == col - 1:
                    if int(keyordred[j]) <= rest and matrix[i][int(keyordred[j])-1] != "-":
                        elementkey = int(keyordred[j]) - 1
                        element[elementkey] = matrix[i][int(keyordred[j])-1]
                else:
                    elementkey = int(keyordred[j]) - 1
                    element[elementkey] = matrix[i][j]

        sort_dic = {}

        for i in sorted(element):
            sort_dic.update({i: element[i]})

        for value in sort_dic.values():
            result.append(value)

    print("Decoded result:")
    print("".join(result))


choice = input("1.Encode transposition cipher\n2.Decode transposition cipher\n")
try:
    if int(choice) == 1:
        encode()
    elif int(choice) == 2:
        decode()
    else:
        print("Pick right choice")
except ValueError:
    print("Entered wrong value")