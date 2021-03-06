'''Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest
 that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break
and cleared your head.'''
def main():
#this is main program
    str_abc = input()
    maxlength = 0
    initialvalue = str_abc[0]
    longest = str_abc[0]
    for i in range(len(str_abc)-1):
        if str_abc[i+1] > str_abc[i]:
            initialvalue += str_abc[i+1]
            if len(initialvalue) > maxlength:
                maxlength = len(initialvalue)
                longest = initialvalue
        else:
            initialvalue = str_abc[i+1]
    print(longest)
if __name__ == "__main__":
    main()
