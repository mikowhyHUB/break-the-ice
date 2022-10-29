'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
'''


user_input = input('Enter passwords separeted with coma: ').split(',')
check_len = [pasw for pasw in user_input if 6 < len(pasw) < 12]
check_special = [pasw for pasw in check_len if not pasw.isalnum()]
check_letters = [pasw for pasw in check_special if 'a' <= pasw <= 'z']
for pasw in user_input:
    if pasw.islower():
        print(pasw)
print(check_letters)
print('\n')
