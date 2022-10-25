
'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
'''
amount = 0
for i in range(4):

    user_income = input('Type "D ..." or "W ...": ').split(' ')
    num = int(user_income[1])
    if user_income[0] == 'D':
        amount += num
    elif user_income[0] == 'W':
        amount -= num
print('Your current deposit is: ', amount)
