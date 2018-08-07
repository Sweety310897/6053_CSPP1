'''This is 2nd program'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in
#one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
def sumofdigits(numbe_r):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if numbe_r == 0:
        return 0
    if numbe_r == 1:
        return 1
    else:
        return numbe_r%10 + sumofdigits(numbe_r//10)
def main():
    '''This is main function'''
    number_1 = input()
    print(sumofdigits(int(number_1)))
if __name__ == "__main__":
    main()
