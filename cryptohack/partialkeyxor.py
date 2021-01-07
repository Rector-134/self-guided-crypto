#!/usr/bin/env python3

from pwn import *

string_hexed = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

string = unhex(string_hexed)

#print (xor(string, 'crypto{')) See below for explanation

#Running the code up to here with our partial plaintext, we receive the following:
#b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
#And right away we see "myXORke". We know we're looking for a key, so...

key = 'myXORke' + 'y'

print (xor(string, key))
