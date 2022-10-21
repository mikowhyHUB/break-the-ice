'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''


class InputAndOutput:
    def getString(self):
        self.x = input('What would you like to say: ')

    def printString(self):
        print(self.x.upper())


xx = InputAndOutput()
xx.getString()
xx.printString()
