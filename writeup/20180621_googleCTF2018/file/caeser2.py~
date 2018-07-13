#!/usr/bin/python
# -*- Coding: utf-8 -*-

file = open('orc.txt','r')
txt = file.read()
shift = 10
zura = 0



def getConverseCodes(args):
    converseCodes = ''
    for s in args:
        s = ord(s)
        if 65 <= s and s<= 90:
            s = s + shift
            if s > 90:
               zura = s - 60
               s = 65 + zura  
        elif 97 <= s and s <= 122:
            s = s + 3
            if s > 122:
               zura  = s - 122
               s = 97 + zura
        s = chr(s)
        converseCodes += s
    return converseCodes
print getConverseCodes(txt)
