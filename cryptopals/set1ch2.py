#!/usr/bin/env python3

from Crypto.Util.strxor import strxor
from binascii import unhexlify

string = '1c0111001f010100061a024b53535009181c'
xor_key = '686974207468652062756c6c277320657965'
comparison_string = '746865206b696420646f6e277420706c6179'

unhexed_string = unhexlify(string)
print ("Decoded initial string: ", unhexed_string)

unhexed_xor_key = unhexlify(xor_key)
print ("Decoded XOR key: ", unhexed_xor_key)

unhexed_comparison_string = unhexlify(comparison_string)
print ("Decoded comparison string: ", unhexed_comparison_string)

result = strxor(unhexed_string, unhexed_xor_key)
print (result)
if result != unhexed_comparison_string:
    print ("Strings not equal.")
else:
    print ("XOR successful. Output matches comparison string." )
