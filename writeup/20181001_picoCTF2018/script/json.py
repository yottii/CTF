#!/usr/bin/env python3
#coding:utf-8
import json

f = open('data.json', 'r')

jsonData = json.load(f)

print(json.dumps(jsonData, sort_keys = True, indent = 4))

f.close()
    

