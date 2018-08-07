'''This is 1st pgm'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
# number and returns the factorial of given number.
# This function takes in one number and returns one number.
def factorial(numbe_r):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if numbe_r == 1:
        return 1
    return numbe_r * factorial(numbe_r-1)
def main():
    '''This is main program'''
    num1 = input()
    print(factorial(int(num1)))
if __name__ == "__main__":
    main()
