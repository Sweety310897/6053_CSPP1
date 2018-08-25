'''
Given a  number int_input, find the product of all the digits
example:
input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num = int(input())
    res = 1
    if num == 0:
        res = 0
        print(res)
    if num > 0:
        while num >= 1:
            rem = num % 10
            res = res * rem
            num = num // 10
        temp1 = res
        print(temp1)
    if num < 0:
        while num < 0:
            num = abs(num)
            while num >= 1:
                rem = num % 10
                res = res * rem
                num = num // 10
        temp2 = res
        temp2 = -(res)
        print(temp2)
if __name__ == "__main__":
    main()
