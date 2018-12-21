STRING1=input('enter the string')
i=0
count=0
length=len(STRING1)
while i<=length-2:
     if (STRING1[i]=='b' and STRING1[i+1]=='o' and STRING1[i+2]=='b'):
     	 count+=1
     i+=1
print(count)
    