#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
	
    rt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    c =  lambda x,y: rt[x]+rt[y] if (rt[x]>rt[y]) else rt[y]-rt[x]
    sum = 0
    obtained_values = list(map(c, roman_string)) 
	for n in obtained_values:
        sum += n
    return sum
