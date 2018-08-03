'''
#Assume s is a string of lower case characters.

#Write a program that counts up the
#number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your
#program should print:
#Number of vowels: 5
'''
def main():
    ''' This is vowels coun program '''
STRING1 = input('')
COUNT = 0
for char in range(len(STRING1)):
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        COUNT += 1
print(COUNT)
if __name__ == "__main__":
    main()
