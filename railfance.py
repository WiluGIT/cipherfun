def encode():
    try:
        text = input("Put text to encode: ")
        key = input("Put key for text: \n")

        # populate array with  -
        railmatrix = [["-" for i in range(len(text))] for i in range(int(key))]
        print("Empty matrix:\n")
        print_matrix(railmatrix)
        row = 0
        col = 0
        godown = False
        # go through matrix and put values
        for i in range(len(text)):
            if row == 0 or row == int(key) - 1:
                godown = not godown

            railmatrix[row][col] = text[i]
            col = col + 1

            if godown is True:
                row = row + 1
            else:
                row = row - 1

        print("Full matrix:\n")
        print_matrix(railmatrix)
        codedresult = ""
        for i in range(int(key)):
            for j in range(len(text)):
                if railmatrix[i][j] != '-':
                    codedresult += railmatrix[i][j]
        print("Encoded result")
        print(codedresult)
    except ValueError:
        print("Entered wrong value")


def decode():
    try:
        text = input("Put text to decode: ")
        key = input("Put key for text: \n")

        # populate array with  -
        railmatrix = [["-" for i in range(len(text))] for i in range(int(key))]
        print("Empty matrix:\n")
        print_matrix(railmatrix)

        # populate array with $ on place of word
        row = 0
        col = 0
        godown = None
        # go through matrix and put values
        for i in range(len(text)):
            if row == 0:
                godown = True
            if row == int(key) - 1:
                godown = False

            railmatrix[row][col] = '$'
            col = col + 1

            if godown is True:
                row = row + 1
            else:
                row = row - 1

        print("Matrix with sign:\n")
        print_matrix(railmatrix)

        index = 0
        for i in range(int(key)):
            for j in range(len(text)):
                if (railmatrix[i][j] == '$') and (index < len(text)):
                    railmatrix[i][j] = text[index]
                    index = index + 1

        print("Matrix with words:\n")
        print_matrix(railmatrix)

        result = []
        row = 0
        col = 0
        for i in range(len(text)):
            if row == 0:
                godown = True
            if row == int(key) - 1:
                godown = False

            if railmatrix[row][col] != '$':
                result.append(railmatrix[row][col])
                col = col + 1

            if godown is True:
                row = row + 1
            else:
                row = row - 1

        print("Decoded result")
        print("".join(result))
    except ValueError:
        print("Entered wrong value")


def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


choice = input("1.Encode Rail fence\n2.Decode Rail fence\n")
try:
    if int(choice) == 1:
        encode()
    elif int(choice) == 2:
        decode()
    else:
        print("Pick right choice")
except ValueError:
    print("Entered wrong value")



