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
			raise Exception("Invalid Sudoku:Duplicate values")
		# elif len(tempcols) != len(dup2):
		# 	raise Exception("invalid suudokkkk")
		#print(sudoku[x+1])
		if len(tempcols) != len(dup2):
			raise Exception("Invalid Sudoku:Duplicate values")
	#print(sudoku)
	pass
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(x,sudoku):
	list1 = []
	#print(sudoku[x])
	for i in sudoku[x]:
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
	# print(sudoku[0])
	# for i in sudoku[y]:


	for i in sudoku:
	 	if i[y] != ".":
	 		list2.append(i[y])
	 # print("hi")
	#print(list2)
	return list2
	
	pass

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(subgridrow,subgridcol,sudoku):

	flag = False
	#print("hi")
	templist = []
	for i in range(0,3):
		for j in range(0,3):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:
		return templist
	templist = []
	for i in range(0,3):
		for j in range(3,6):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])	
	if flag == True:
		return templist
	templist = []
	for i in range(0,3):
		for j in range(6,9):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(3,6):
		for j in range(0,3):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(3,6):
		for j in range(3,6):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(3,6):
		for j in range(6,9):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(6,9):
		for j in range(0,3):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(6,9):
		for j in range(3,6):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist
	templist = []
	for i in range(6,9):
		for j in range(6,9):
			if i == subgridrow and j == subgridcol:
				flag = True
			templist.append(sudoku[i][j])
	if flag == True:	
		return templist

"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(temp11):
	#print(temp11)
	# str1 = ""
	for i in range(len(temp11)):
		for j in range(len(temp11)):
			if temp11[i][j] == ".":
				rowval = getRowValues(i,temp11)
				colval = getColumnValues(j,temp11)
				gridval = getGridValues(i,j,temp11)
				values = rowval + colval + gridval
				str1 = ""
				for each in range(1,10):
					if str(each) not in values:
						str1 = str1 + str(each)
				print(str1)


"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def validateinput(temp1):
	#print(temp1)
	if len(temp1) != 81:
		raise Exception("Invalid input")
	#for i in temp1:
	if '.' not in temp1:
		raise Exception("Given sudoku is solved")
	# if len(temp1) == 81:
	# 	raise Exception("Given sudoku is solved")
	

def main():
	list1 = []
	listres = []
	temp = input()
	try:
		hi = validateinput(temp)
		#print(hi)
		input1 = temp
	#i = 0
		for i in range(0,81,9):
			lst = []
			for j in range(0,9):
				lst.append(input1[i])
				i += 1 
			listres.append(lst)
		#print(listres)
		validateSudoku(listres)
		possibleValues(listres)
	except Exception as e:
	   	print(e)
	#validateSudoku(listres)
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


