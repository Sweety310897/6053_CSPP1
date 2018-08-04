str1=input('enter sring')
i=0
temp=''
length=len(str1)
while i<length:
	if str1[i] == "#":
		temp=str1+"@"
	else:
		temp=str1[i]
	i += 1
print(temp)

