'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    input1 = int(input())
    i = 0
    str1 = ""
    while i < input1:
        input2 = input()
        str1 += input2
        i += 1
        print(str1)
        str1 = ""



if __name__ == '__main__':
    main()
