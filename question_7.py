'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

'''

X = int(input())
Y = int(input())
lst = []
for i in range(X):
    for j in range(Y):
        lst.append(i*j)
outcome = []
for i in range(0, len(lst), 5):
    outcome.append(lst[i:i+5])

print(outcome)
