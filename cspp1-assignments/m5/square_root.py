num1=int(input('enter square root'))
epsilon=0.001
guess=0.01
increment=0.0001
num_guesses=0
while abs(guess**2-num1)>=epsilon :
    guess+=increment
    num_guesses=1
print(num_guesses)
if abs((guess**2)-num1)>=epsilon :
    print(num1)
else :
    print(guess,'guess is close')
