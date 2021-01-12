#!/usr/bin/env python3

from binascii import hexlify

plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key = b"ICE"

def repeating_key_xor(plaintext, key):
    output = b''
    i = 0
    key_length = len(key)

    for byte in plaintext:
        output += bytes([byte ^ key[i]])
        i = (i + 1) % key_length

    return output

def main():

    ciphertext = repeating_key_xor(plaintext, key)

    print ("[+] XORed plaintext:", hexlify(ciphertext).decode("utf-8"))

    if (str(hexlify(ciphertext), "utf-8")) == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f":
        print ("[+] Results match. Success!")

    else:
        print ("[-] Results do not match.")



if __name__ == "__main__":
    main()
