'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''

x = list(input('Binary numbers: ').split(','))
x = ['1' + i for i in x]
x = [int(i) for i in x]
# x = [i.pop(0) for i in x]
outcome = []
for i in x:
    if i[1:] % 5 == 0:
        outcome.append(i)
print(outcome)
