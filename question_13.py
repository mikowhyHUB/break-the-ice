'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123
'''
from curses.ascii import isalpha


sentence = input(': ')

dig, let = 0, 0
for i in sentence:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        let += 1

print('LETTERS', let, '\nDIGITS', dig)
