# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.


def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    if x == 0:
    	return 0
    elif x >= 1:
    	num1 = x * x
    	return num1
    elif x <=1:
        num1 = x * x
        return num1
    
# Correct

def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

