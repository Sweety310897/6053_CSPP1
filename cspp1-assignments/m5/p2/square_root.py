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
    num = int(input('enter square root'))
    epsilon = 0.001
    guess = 0.01
    increment = 0.0001
    num_guesses = 0
    while abs(guess**2-num) >= epsilon:
        guess += increment
        num_guesses = 1
    print(num_guesses)
    if abs((guess**2) - num) >= epsilon:
        print(num)
    else:
        print(guess)
if __name__ == "__main__":
    main()