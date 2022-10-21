'''
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
'''

# q = pierwiastek z wyniku
# c = 50
# h = 30
# d = 100,150,180
# output = 18,22,24

from math import sqrt

C = 50
H = 30

# wzró pierwiastka


def calculate(D):
    return sqrt((2*C*D)/H)


# imput i rozdzielamy ,
D = [int(i) for i in input('numbers: ').split(',')]
# stringi zamieniamy na inty w liście
D = [int(i) for i in D]
# obliczamy pierwiastek kadej podanej liczby
D = [calculate(i) for i in D]
# zaokrąglamy by nie było float
D = [round(i) for i in D]
# zamieniamy w stringa eby mozna było je wyprintowac
D = [str(i) for i in D]
print(','.join(D))
