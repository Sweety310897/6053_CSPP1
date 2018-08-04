'''This is 2nd pgm'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''this is 2nd program'''
    num = int(input())
    epsilon = 0.01
    guess = 0.0
    increment = 0.1
    while abs(guess**2-num) >= epsilon:
        guess += increment
    if abs((guess**2) - num) >= epsilon:
        print(num)
    else:
        print(guess)
if __name__ == "__main__":
    main()
