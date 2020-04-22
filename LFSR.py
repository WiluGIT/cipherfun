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

    print("Encoded synchronous result:\n{}".format(encoded_result))


def synchronous_cipher_decode(ciphertext, seed, taps):
    lfsr_xor = ""
    for state, output, xor in lfsr(seed, taps):
        lfsr_xor += str(xor)

    decoded_result = ""
    for i in range(len(ciphertext)):
        result = str(int(lfsr_xor[i]) ^ int(ciphertext[i]))
        decoded_result += result

    print("Decoded synchronous result:\n{}".format(decoded_result))

def autokey_cipher_encode(plaintext, seed, taps):
    state = seed
    xor = 0
    counter = 0
    ciphertext_result = ""
    while 1:
        for t in taps:
            xor += int(state[t - 1])
        if xor % 2 == 0.0:
            xor = 0
        else:
            xor = 1

        z_x_xor = str(int(plaintext[counter]) ^ int(xor))
        state = z_x_xor + state[:-1]
        counter += 1
        ciphertext_result += z_x_xor
        xor = 0
        if counter >= len(plaintext):
            break
    print("Encoded autokey result:\n{}".format(ciphertext_result))


def autokey_cipher_decode(ciphertext, seed, taps):
    state = seed
    xor = 0
    counter = 0
    plaintext_result = ""
    while 1:
        for t in taps:
            xor += int(state[t - 1])
        if xor % 2 == 0.0:
            xor = 0
        else:
            xor = 1

        current_bit = ciphertext[counter]
        y_z_xor = str(int(current_bit) ^ int(xor))
        state = current_bit + state[:-1]
        plaintext_result += y_z_xor
        counter += 1
        xor = 0
        if counter >= len(ciphertext):
            break
    print("Decoded autokey result:\n{}".format(plaintext_result))



plaintext = "11101001"
ciphertext_sync = "01100110"
ciphertext_autokey = "00110011"
seed = "0011"
taps = (1,4)
synchronous_cipher_encode(plaintext, seed, taps)
synchronous_cipher_decode(ciphertext_sync, seed, taps)
autokey_cipher_encode(plaintext, seed, taps)
autokey_cipher_decode(ciphertext_autokey, seed, taps)
