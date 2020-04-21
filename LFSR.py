# def lfsr2(seed, taps):
#     sr = seed
#     nbits = 3
#     while 1:
#         xor = 1
#         for t in taps:
#             if (sr & (1<<(t-1))) != 0:
#                 xor ^= 1
#         sr = (xor << nbits-1) + (sr >> 1)
#         yield xor, sr
#         if sr == seed:
#             break
#
# nbits = 3
# for xor, sr in lfsr2(0b001, (1,3)):
#     print(xor, bin(2**nbits+sr)[3:])
#
# print("gowno", 0b001>>1)



def lfsr(seed, taps):
    result = seed
    xor = 0
    while 1:
        for t in taps:
            xor += int(result[t-1])
        if xor % 2 == 0.0:
            xor = 0
        else:
            xor = 1

        result = str(xor) + result[:-1]

        yield result, xor
        xor = 0
        if result == seed:
            break

print("state    xor")
for state, xor in lfsr('10000', (3,5)):
    print("{}   {}".format(state, xor))