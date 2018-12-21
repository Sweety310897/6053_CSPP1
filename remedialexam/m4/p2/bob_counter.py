'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
    '''This is bob program '''
STRING1 = input('')
I = 0
COUNT = 0
LENGTH = len(STRING1)
while I <= LENGTH-3:
    if (STRING1[I] == 'b' and STRING1[I+1] == 'o' and STRING1[I+2] == 'b'):
        COUNT += 1
    I += 1
print(COUNT)
if __name__ == "__main__":
    main()
