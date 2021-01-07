#!/usr/bin/env python3

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

a = 209
m = 991
print (mod_inverse(a, m))
