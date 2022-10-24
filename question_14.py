'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program: Hello world!
'''

sentence = input('Type words: ')
upper = 0
lower = 0
for i in sentence:
    if 'a' <= i and i <= 'z':
        lower += 1
    elif 'A' <= i and i <= 'Z':
        upper += 1
print('UPPER CASE', upper)
print('LOWER CASE', lower)
