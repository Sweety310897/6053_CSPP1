STRING1=input('enter string')
INITIAL_ELEMENT=STRING1[0]
CURRENT_ELEMENT=STRING1[0]
MAXLENGTH=0
i=0
length=len(STRING1)
for i in range(length-1):
    if(STRING1[i+1]>STRING1[i]):
        INITIAL_ELEMENT += STRING1[i+1]
        if(len(INITIAL_ELEMENT))>(MAXLENGTH):
               MAXLENGTH=len(INITIAL_ELEMENT)
               CURRENT_ELEMENT=INITIAL_ELEMENT
    else:
         INITIAL_ELEMENT=STRING1[i+1]
    i += 1
print(CURRENT_ELEMENT)
