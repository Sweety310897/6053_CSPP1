varA= input("enter A value")
varB= input("enter B value")
newvarA=type(varA)
newvarB=type(varB)
if newvarA==str or newvarB==str:
 print('string involved')
elif varA > varB :
 print('varA is bigger')
elif varA == varB:
 print('equal')
elif varA < varB:
 print('varA is smaller')
else:
 print('invalid input')