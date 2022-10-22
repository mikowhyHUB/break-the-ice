'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
'''


def unique_list(l):
    lst = []
    [lst.append(i) for i in l if i not in lst]
    print(lst)


a = input("what sentence: ")
a = ' '.join(unique_list(a.split()))
