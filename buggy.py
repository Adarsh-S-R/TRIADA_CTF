###################################TRIADA_CTF_2024###################################

def xor_flag(encoded_flag, key):
    decoded_chars = []
    for i in range(len(encoded_flag)):
        decoded_char = chr(encoded_flag[i] ^ ord(key[i % len(key)]))
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)


encoded_flag = [39, 51, 61, 52, 54, 47, 8, 25, 68, 7, 45, 10, 64, 3, 1, 18, 21, 95, 29, 6, 43, 64, 7, 13, 16, 82, 7, 64, 15]

key = 'saturn'


flag = xor_flag(encoded_flag)
print("Flag:", flag)


###################################TRIADA_CTF_2024###################################
