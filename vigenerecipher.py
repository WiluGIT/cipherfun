def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def encode(plaintext, k, matrix):
    # straight key extend
    counter = 0
    key = ""
    # if key is longer than plaintext cut key
    if len(k) > len(plaintext):
        key = k[0:len(plaintext)]
    # else extend key
    else:
        for i in range(len(plaintext)):
            if counter < len(k):
                key += k[counter]
                counter += 1
            else:
                counter = 0
                key += k[counter]
                counter += 1


    print("Plaintext: {}".format(plaintext))
    print("Key: {}".format(key))

    result = ""
    for i in range(len(plaintext)):
        index_pt = alphabet.index(plaintext[i])
        index_k = alphabet.index(key[i])
        result += matrix[index_k][index_pt]

    print("Encoded result:\n{}".format(result))


def decode(ciphertext, k, matrix):
    # straight key extend
    counter = 0
    key = ""
    # if key is longer than plaintext cut key
    if len(k) > len(plaintext):
        key = k[0:len(plaintext)]
    # else extend key
    else:
        for i in range(len(plaintext)):
            if counter < len(k):
                key += k[counter]
                counter += 1
            else:
                counter = 0
                key += k[counter]
                counter += 1

    print("Ciphertext: {}".format(ciphertext))
    print("Key: {}".format(key))

    result = ""
    for i in range(len(ciphertext)):
        # get column
        index_k = alphabet.index(key[i])
        # go down through column
        for j in range(len(alphabet)):
            if matrix[j][index_k] == ciphertext[i]:
                result += alphabet[j]

    print("Decoded result:\n{}".format(result))


alphabet = "abcdefghijklmnopqrstuvwxyz".replace(" ", "").upper()


# create vigenere matrix
size = len(alphabet)
matrix = [["-" for i in range(size)] for i in range(size)]

# populate matrix with alphabet
for i in range(size):
    for j in range(size):
        elem = (j + i) % size
        matrix[i][j] = alphabet[elem]

print_matrix(matrix)
k = "BREAK".replace(" ", "").upper()
plaintext = "cryptography".replace(" ", "").upper()
ciphertext = "DICPDPXVAZIP".replace(" ", "").upper()

encode(plaintext, k, matrix)
decode(ciphertext, k, matrix)