


def tictactoe():
	temp3 = []
	rowcheck = ''
	colcheck = ''
	diagcheck = ''
	for i in range(3):
		temp1 = input()
		temp2 = temp1.split()
		temp3.append(temp2)
	rowcheck = rowchec_k(temp3)
	colcheck = colchec_k(temp3)
	diagcheck = diag_check(temp3)
def rowchec_k(temp3):
	if temp3[0][0] == temp3[0][1] == temp3[0][2]:
		return temp3[0][0]
	if temp3[1][0] == temp3[1][1] == temp3[1][2]:
		return temp3[1][0]
	if temp3[2][0] == temp3[2][1] == temp3[2][2]:
		return temp3[2][0]
def colchec_k(temp3):
	if temp3[0][0] == temp3[1][0] == temp3[2][0]:
		return temp3[0][0]
	if temp3[0][1] == temp3[1][1] == temp3[2][1]:
		return temp3[0][1]
	if temp3[0][2] == temp3[1][2] == temp3[2][2]:
		return temp3[0][2]
def diag_check(temp3):
	if temp3[0][0] == temp3[1][1] == temp3[2][2]:
		return temp3[0][0]
	if temp3[0][2] == temp3[1][1] == temp3[2][0]:
		return temp3[0][2]


def main():
	res = print(tictactoe())
	#print(res)
if __name__ == '__main__':
    main()
