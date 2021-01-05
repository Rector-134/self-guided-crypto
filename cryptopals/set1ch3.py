#!/usr/bin/env python3

from pwn import unhex

encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

string = unhex(encoded_string)

decoded_string = (''.join(chr(num ^ key) for num in string) for key in range(256))
flag = max(decoded_string, key = lambda s: s.count(' '))

print (flag)
