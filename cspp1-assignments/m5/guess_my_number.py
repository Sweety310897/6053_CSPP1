print('please think of a number between 0 and 100!')
print('Is ur num 50?')
string1=input('enter char')
low=0
high=100
mid=((low+high)//2)
while(string1!='c'):
    if(string1=='h'):
        high=mid
        mid=(mid+low)//2
    elif(string1=='l'):
        low=mid
        mid=(mid+high)//2
    else:
        print('invalid input')
    print('is ur num ',mid)
    string1=input('enter char')
if(string1=='c'):
    print(mid)

