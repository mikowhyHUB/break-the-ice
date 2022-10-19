# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def factorial(num):
    outcome = 1
    if num > 0:
        for n in range(1, num+1):
            outcome *= n
    else:
        print('only numbers >0')
    return outcome


print(factorial(0))
