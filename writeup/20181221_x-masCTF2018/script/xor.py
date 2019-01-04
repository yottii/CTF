#!/usr/bin/env python3

strings = "U @L^vi>n=i>R9;9<cR9ciR9;9<cR9ciR9;9<cR9ciR9;9<cR9ciRka9;p"
xor = 0xd
flag = ''.join(chr(ord(c)^xor) for c in strings)

print(flag)
