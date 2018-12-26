"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
 	raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
	raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
	raise an exception
"""
def validateSudoku(sudoku):
	#print(sudoku)
	for x in range(9):
		temprow = getRowValues(x,sudoku)
		tempcols = getColumnValues(x,sudoku)
		dup1 = set(temprow)
		dup2 = set(tempcols)
		if len(temprow) != len(dup1):
			raise Exception("invalid suudok")
		# elif len(tempcols) != len(dup2):
		# 	raise Exception("invalid suudokkkk")
		print(sudoku[x+1])
		if sudoku[x] == sudoku[x + 1]:
			raise Exception("invalid sudooooookkkkk")
	#print(temp)
	pass
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(y,sudoku):
	list1 = []

	for i in sudoku[y]:
		if i != ".":
			list1.append(i)
	# print("hi")
	#print(list1)
	return list1
	pass
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(y,sudoku):
	list2 = []

	for i in sudoku[y]:
		if i != ".":
			list2.append(i)
	# print("hi")
	#print(list2)
	return list2
	
	pass

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues():
	pass
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues():
	pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def validateinput(temp1):
	#print(temp1)
	if len(temp1) < 81:
		raise Exception("invalid input")
	for i in temp1:
		if i not in "123456789.":
			raise Exception("invalid expressions")
	# if len(temp1) == 81:
	# 	raise Exception("given sudok solved")
	

def main():
	list1 = []
	listres = []
	temp = input()
	try:
		hi = validateinput(temp)
		#print(hi)
		input1 = list(temp)
	#i = 0
		for i in range(0,81,9):
			lst = []
			for j in range(0,9):
				lst.append(input1[i])
				i += 1 
			listres.append(lst)
		#print(listres)
		# validateSudoku(listres)
		pass
	except Exception as e:
		print(e)
	validateSudoku(listres)
	# i=0
	# while(i < 81):
	# 	lst =[]
	# 	for k in range(0,9):
	# 		lst.append(input1[i])
	# 		i=i+1
	# 	listres.append(lst)
	# print(listres)
	# if len(input1)
	# 	for each in input1:

	# temp1 = list(input1)
	# lis = []
	# temp = []
	# #print(temp1[0])
	# for i in range(len(temp1)):
	# 	print(i)
	# 	if i%9==0 and i!=0:
	# 		lis.append(temp)		
	# 		print(lis)
	# 		temp = []
	# 	temp.append(temp1[i])
if __name__ == '__main__':
    main()

