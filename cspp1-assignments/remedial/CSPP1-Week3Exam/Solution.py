def validate(temp):
	if temp[4] not in "0123456789":
		raise Exception("Invalid input")

def main():
	noofinputs = int(input())
	list1 = []
	list3 = []
	dic = {}
	i = 0
	while i < noofinputs:
		# try :
		temp = input().split("|")
		# 	validate(temp)
		# except Exception as e:
	 #   		print(e)

		list3.append(temp[0])		
		# dic[temp[0]] = 0
		list1.append(temp)
		i += 1
	templist = list(set(list3))
	# print(list1)
	# print(templist)
	list5 = []
	list6 = []
	j = 0
	dic6 = {}
	dic9 = {}
	for i in range(len(list1)):
		if list1[i][0] in templist:
			if list1[i][2] == list1[i][3]:
				dic6[list1[i][0]] = list1[i][4]
			else:
				dic6[list1[i][0]] = list1[i][4]
	for i in range(len(list1)):
		for each in templist:
			if list1[i][0] == each:
				# if list1[i][0] not in dic9:
				sum5 = 0
				if list1[i][2] == list1[i][3]:
					sum5 += int(list1[i][4])
					# dic9[each] = list1[i][4]
					list5.append(list1[i][4])
				else:
					sum5 -= int(list1[i][4])
					# dic6[each] = list1[i][4]
					list5.append(list1[i][4])
				list6.append(each)
				dic9[each] = sum5
				list6.append(sum5)

	list7 = []
	dic19 = {}
	# print(list6[0])
	k = 1
	# print(list6,"6")
	
	# while k < len(list6):
	# 	if list6[k] not in dic19.keys():
	# 		if k%2 == 0:
	# 			dic19[list6[k]] = list6[k+1]
	# 	else:
	# 		temp = list6[k]
	# 		dic19[temp].append(list6[k+1])
	# 	k += 1
	# print(dic19)

	# print(dic9,"9")

		
	# print(dic6)

if __name__ == '__main__':
	main()