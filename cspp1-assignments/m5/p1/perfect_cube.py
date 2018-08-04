'''this is'''
# Write a python program to find
#if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
def main():
    '''this is program'''
#this is program for perfect cube using guess
    num = int(input())
    guess = 0
    while guess**3 < num:
        guess += 1
    if guess**3 == num:
        print(num, 'is a perfect cube')
    else:
        print(num, 'is not a perfect cube')
if __name__ == "__main__":
    main()
