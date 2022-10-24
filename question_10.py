'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
'''


sentence = input("what would you like to say: ")
lst = list(sentence.split())
x = []
for i in lst:
    if i not in x:
        x.append(i)
x = sorted(x)

print(' '.join(x))
