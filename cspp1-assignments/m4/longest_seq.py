STRING1 = input('enter string')
maxlength = 0
initialvalue = STRING1[0]
longest = STRING1[0]
for i in range(len(STRING1)-1):
    if STRING1[i+1] > STRING1[i]:
        initialvalue += STRING1[i+1]
        if len(initialvalue) > maxlength:
                 maxlength = len(initialvalue)
                 longest = initialvalue
    else:
        initialvalue = STRING1[i+1]
    i += 1
print(longest)