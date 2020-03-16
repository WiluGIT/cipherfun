def nwd(a, b): return nwd(b, a % b) if b else a


def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def encode_3b():
    text = "CRYPTOGRAPHY".replace(" ", "").upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".replace(" ", "").upper()
    n = 21
    k0 = 8
    k1 = 10
    result = ""
    if nwd(k0, n) != 1 or nwd(k1, n) != 1:
        print("K0 or K1 are not GCD")
    else:
        for i in range(len(text)):
            cipher_char = (alphabet.index(text[i]) * k1 + k0) % n
            char = alphabet[cipher_char]
            result += char
        print("Encoded result:\n{}".format(result))


def decode_3b():
    text = "HKRLJBFKILPR".replace(" ", "").upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".replace(" ", "").upper()
    n = 21
    k0 = 8
    k1 = 10
    result = ""
    k1_inverse = modInverse(k1, n)

    if nwd(k0, n) != 1 or nwd(k1, n) != 1:
        print("K0 or K1 are not GCD")
    else:
        for i in range(len(text)):
            dec_char = ((alphabet.index(text[i]) + (n - k0)) * k1_inverse) % n
            char = alphabet[dec_char]
            result += char

        print("Decoded result:\n{}".format(result))


def encode_3a():
    k = 3
    text = "CRYPTOGRAPHY".replace(" ", "").upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".replace(" ", "").upper()
    n = len(alphabet)
    result = ""
    for i in range(len(text)):
        cipher_char = (alphabet.index(text[i]) + k) % n
        char = alphabet[cipher_char]
        result += char

    print("Encoded result:\n{}".format(result))


def decode_3a():
    text = "FUBSWRJUDSKB".replace(" ", "").upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".replace(" ", "").upper()
    n = len(alphabet)
    k = 3
    result = ""
    for i in range(len(text)):
        dec_char = (alphabet.index(text[i]) + (n - k)) % n
        char = alphabet[dec_char]
        result += char

    print("Decoded result:\n{}".format(result))


# encode_3a()
# decode_3a()
encode_3b()
decode_3b()