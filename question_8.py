'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

'''

x = input('words: ').split(',')
x = sorted(x)
x = ','.join(x)

print(x)
