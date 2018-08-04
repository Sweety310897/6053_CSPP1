''' this is'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''this is 4th pgm'''
    epsilon = 0.01
    y_s = int(input())
    guess1 = y_s/2.0
    numguesses = 0
    while abs(guess1*guess1-y_s) >= epsilon:
        numguesses += 1
        guess1 = guess1-(((guess1**2)-y_s)/(2*guess1))
    print(str(numguesses))
    print(str(guess1))
if __name__ == "__main__":
    main()
