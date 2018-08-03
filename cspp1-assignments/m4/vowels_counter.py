''' This is vowels coun program '''
STRING1 = input('enter the string')
COUNT = 0
for char in STRING1:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        COUNT += 1
print(COUNT)
