'''This is bob program '''
STRING1 = input('enter the string')
I = 0
COUNT = 0
LENGTH = len(STRING1)
while I <= LENGTH-3:
    if (STRING1[I] == 'b' and STRING1[I+1] == 'o' and STRING1[I+2] == 'b'):
        COUNT += 1
    I += 1
print(COUNT)
    