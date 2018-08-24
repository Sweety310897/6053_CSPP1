


def tictactoe():
	# temp1 = []
	# for i in range(3):
	# 	temp2 = []
	# 	for j in range(3):
	# 		temp3 = input("enter input")
	# 		temp2.append(temp3)
	# temp1.append(temp2)
	# print(temp1)
	
	temp3 = []
	rowcheck = ''
	for i in range(3):
		temp1 = input()
		temp2 = temp1.split()
		temp3.append(temp2)
	rowcheck = rowcheck(temp3)
def rowcheck(temp3):
	if temp3[0][0] == temp3[0][1] == temp3[0][2]:
		return temp3[0][0]


	
	






def main():
	res = print(tictactoe())
	#print(res)
if __name__ == '__main__':
    main()
