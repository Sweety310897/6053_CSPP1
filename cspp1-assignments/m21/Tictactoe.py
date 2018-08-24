def tictactoe():
	temp3 = []
	# rowcheck = ''
	# colcheck = ''
	# diagcheck = ''
	winner = None
	for i in range(3):
		temp1 = input()
		temp2 = temp1.split()
		temp3.append(temp2)
	is_valid = is_valid_input(temp3)
	if is_valid:
		winner = rowchec_k(temp3)
		if winner == None:
			winner = colchec_k(temp3)
		if winner == None:
			winner = diag_check(temp3)
		if winner == None:
			winner = "draw"
		return winner
	else:
		return "invalid input"
def rowchec_k(temp3):
	'''
	This is to check for rows
	'''
	if temp3[0][0] == temp3[0][1] == temp3[0][2]:
		return temp3[0][0]
	if temp3[1][0] == temp3[1][1] == temp3[1][2]:
		return temp3[1][0]
	if temp3[2][0] == temp3[2][1] == temp3[2][2]:
		return temp3[2][0]
def colchec_k(temp3):
	'''
	This is to check cols
	'''
	if temp3[0][0] == temp3[1][0] == temp3[2][0]:
		return temp3[0][0]
	if temp3[0][1] == temp3[1][1] == temp3[2][1]:
		return temp3[0][1]
	if temp3[0][2] == temp3[1][2] == temp3[2][2]:
		return temp3[0][2]
def diag_check(temp3):
	'''
	This is to check diag
	'''
	if temp3[0][0] == temp3[1][1] == temp3[2][2]:
		return temp3[0][0]
	if temp3[0][2] == temp3[1][1] == temp3[2][0]:
		return temp3[0][2]
def is_valid_input(temp3):
	for i in range(3):
		for j in range(3):
			if temp3[i][j] == "x" or temp3[i][j] == "o" or temp3[i][j]== ".":
				pass
			else:
				return False
		return True

def main():
	res = tictactoe()
	print(res)
if __name__ == '__main__':
    main()
