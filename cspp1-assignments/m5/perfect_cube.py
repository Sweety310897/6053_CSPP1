num1=int(input('enter a cube number'))
guess=0
while guess**3<num1:
    guess+=1
print(guess)