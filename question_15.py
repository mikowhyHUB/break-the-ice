'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program: 9
'''


digit = input()
string = ''
sum = 0
for i in range(1, 5):
    string += digit
    sum += int(string)
print(sum)
