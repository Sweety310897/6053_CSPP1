num=int(input('enter num'))
res=1
while(num>=1):
	rem=num%10
	res=res*rem
	num=num//10
print(res)