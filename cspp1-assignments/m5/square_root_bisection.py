num1=abs(float(input('enter num')))
low=abs(float(input('lower value')))
high=abs(float(input('higher value')))
epsilon=0.001
while True:
    mid=(low+high)/2
    difference=mid**2-num1
    if abs(difference)<=epsilon:
        break
    if difference<0:
        low=mid
    else:
        high=mid
print(round(mid,3))