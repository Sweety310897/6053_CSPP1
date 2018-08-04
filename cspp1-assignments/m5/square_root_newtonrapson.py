epsilon = 0.01
y=24
guess=y/2.0
numguesses=0
while abs(guess*guess-y)>=epsilon:
 numguesses+=1
 guess=guess-(((guess**2)-y)/(2*guess))
print(str(numguesses))
print(str(guess))