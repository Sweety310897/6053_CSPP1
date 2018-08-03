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
STRING_1 = input()
maxlength = 0
initialvalue = STRING_1[0]
longest = STRING_1[0]
for i in range(len(STRING_1)-1):
    if STRING_1[i+1] > STRING_1[i]:
        initialvalue += STRING_1[i+1]
        if len(initialvalue) > maxlength:
                 maxlength = len(initialvalue)
                 longest = initialvalue
    else:
        initialvalue = STRING_1[i+1]
    i += 1
print(longest)
if __name__ == "__main__":
    main()
