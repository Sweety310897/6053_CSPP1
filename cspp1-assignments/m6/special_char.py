str1=str(input())
temp=""
for char in str1:
	if char in "#!@%$&^*":
		temp=temp+" "
	else:
		temp=temp+char
print(temp)

