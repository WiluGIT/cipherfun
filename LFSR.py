def lfsr(seed, taps):
    state = seed
    xor = 0
    while 1:
        for t in taps:
            xor += int(state[t-1])
        if xor % 2 == 0.0:
            xor = 0
        else:
            xor = 1

        output = state[-1]
        state = str(xor) + state[:-1]

        yield state, output, xor
        xor = 0
        if state == seed:
            break


def synchronous_cipher_encode(plaintext, seed, taps):
    lfsr_xor = ""
    for state, output, xor in lfsr(seed, taps):
        lfsr_xor += str(xor)

    encoded_result = ""
    for i in range(len(plaintext)):
        result = str(int(lfsr_xor[i]) ^ int(plaintext[i]))
        encoded_result += result

    print("Encoded result:\n{}".format(encoded_result))


def synchronous_cipher_decode(ciphertext, seed, taps):
    lfsr_xor = ""
    for state, output, xor in lfsr(seed, taps):
        lfsr_xor += str(xor)

    decoded_result = ""
    for i in range(len(ciphertext)):
        result = str(int(lfsr_xor[i]) ^ int(ciphertext[i]))
        decoded_result += result

    print("Decoded result:\n{}".format(decoded_result))


plaintext ="101011111100001"
ciphertext = "110101010000101"
seed = "0010"
taps = (1,4)
synchronous_cipher_encode(plaintext,seed,taps)
synchronous_cipher_decode(ciphertext,seed,taps)
# print("state    output      xor")
# for state, output, xor in lfsr('1000', (1,4)):
#     print("{}      {}           {}".format(state, output,xor))