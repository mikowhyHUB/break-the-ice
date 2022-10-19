'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def new_func(num):
    if num > 0:
        outcome = {}
        for n in range(1, num+1):
            outcome[n] = n*n
        print(outcome)
    else:
        print('only numbers >0')


num = int(input('What number: '))
new_func(num)
