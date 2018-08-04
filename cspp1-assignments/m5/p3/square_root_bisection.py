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
    num1 = float(input('enter num'))
    low = float(input('lower value'))
    high = float(input('higher value'))
    epsilon = 0.001
    while True:
        mid = (low+high)/2
        difference = mid**2-num1
        if abs(difference) <= epsilon:
            break
        if difference < 0:
            low = mid
        else:
            high = mid
    print(round(mid, 3))

if __name__ == "__main__":
    main()
