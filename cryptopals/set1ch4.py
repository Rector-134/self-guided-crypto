#!/usr/bin/env python3

def single_char_xor(byte_message, value):
    output = b''

    for b in byte_message:
        output += bytes([b ^ value])

    return output

def line_score (message):
    table = {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3,
        'e': 12.9, 'f': 2.2, 'g': 2.0, 'h': 6.1,
        'i': 7.1, 'j': 0.2, 'k': 0.8, 'l': 3.9,
        'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9,
        'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1,
        'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.2,
        'y': 2.0, 'z': 0.07, ' ': 15.0
        }

    score = 0

    for byte in message.lower():
        score += float(table.get(chr(byte), 0))

    return score

def solve(text):
    ciphertext = bytes.fromhex(text)

    possible_decryptions = []

    for i in range(32, 127):
        message = single_char_xor(ciphertext, i)

        score = line_score(message)

        possible_decryptions.append((message, i, score))

    possible_decryptions.sort(key = lambda x: x[2], reverse = True)

    return possible_decryptions[0]

def main():
    textfile = open('set1ch4.txt').read().splitlines()

    decrypted_list = []

    for l in textfile:
        decrypted_list.append(solve(l))

    decrypted_list.sort(key = lambda x: x[2], reverse = True)

    key = decrypted_list[0][0]

    print ("[+] Most probable plaintext is:", key.decode('utf-8'))

if __name__ == "__main__":
    main()
