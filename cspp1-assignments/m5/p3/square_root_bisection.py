'''This is 3rd pgm'''
# Write a python program to find the square root of the given number
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
def main():
    ''' This is 3rd pgm'''
    num1 = int(input(''))
    low = int(input(''))
    high = int(input(''))
    epsilon = 0.001
    while True:
        mid = (low + high)/2
        if mid*mid >= (num1 - epsilon) and mid*mid <= (num1 + epsilon):
            break
            high = mid
        else:
            low = mid
    print(mid)

if __name__ == "__main__":
    main()
