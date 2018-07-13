#!/usr/bin/python
# -*- Coding: utf-8 -*-

file = open('orc.txt','r')
inputStr = file.read()


def getConverseCodes(args):
    converseCodes = ''
    for s in args:
        s = ord(s)
        if 65 <= s and s<= 90:
            s = s + 3
        elif 97 <= s and s <= 122:
            s = s + 3
        s = chr(s)
        converseCodes += s
    return converseCodes

print getConverseCodes(inputStr)
