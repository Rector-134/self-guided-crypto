#!/usr/bin/env python3

from pwn import *

key1_hexed = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_encoded = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key3_encoded = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_encoded = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1 = unhex(key1_hexed)
key2_encoded_unhexed = unhex(key2_encoded)
key3_encoded_unhexed = unhex(key3_encoded)

key2 = xor(key2_encoded_unhexed, key1)
key3 = xor(key2, key3_encoded_unhexed)
flag = xor(unhex(flag_encoded), key1, key3, key2)

print (flag)
