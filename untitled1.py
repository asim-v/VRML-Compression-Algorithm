# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:08:49 2019

@author: personal
"""
import re

#vrml realizator
R2 = []
R = []
l = []
new = []

def splitter(t):
    l = ''.join(str(x) for x in t)
    res = []
    for x in str(l):
        if x not in ["'","]"]:
            res.append(x)
    return res

def converter(R):
    new = []
    for m in R:               
        try:
            if m in ['0','1']: new.append(int(m))
            else: new.append(float(m[:4]))
        except:
            if m != '':
                new.append(m)
    return new

file = open('Alpha2.wrl')
for x in ''.join(file):
    l.append(x)   
file.close()


for x in range(len(l)):
    if x+4 == len(l):break
    if l[x] + l[x+1] + l[x+2]+ l[x+3]+ l[x+4] in ['point','coordIndex']:
        local = []
        for z in l[x+7:]:
            if z == ']': 
                R = (''.join(local))
                break  
            elif z != '':
                local.append(z)
        ender = R[::]
        R  = re.split(r'(;|,|\s)\s*', R)
        R2 = converter(R)
        counter = 0 
        
        #l[len(splitter(ender))+7+x] = 'LEONARDO'
        l[x+7:len(splitter(ender))+7+x] = splitter(R2)
        
        counter += 1
        

EXPORT = open('result.wrl','w+')
EXPORT.write(''.join(l))
EXPORT.close()