'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
'''

num = input(':').split(',')
num = [int(i) for i in num]
out = [i for i in num if i % 2 != 0]
out = [str(i * i) for i in out]
print(' '.join(out))
