def task(temp):
	list1 = []
	# print(temp)
	list1.append(temp[1])
	list1.append(temp[2])
	list1.append(temp[3])
	if temp[4] == "y":
		list1.append("Important")
	else:
		list1.append("Not Important")
	if temp[5] == "y":
		list1.append("Urgent")
	else:
		list1.append("Not Urgent")
	list1.append(temp[6])
	return list1
def validate(temp):
	if temp[1] == "":
		raise Exception("Title not provided")
	if int(temp[3]) < 0:
		raise Exception("Invalid timeToComplete " + temp[3])
	if temp[6] != "todo" and temp[6] != "done":
		raise Exception("Invalid status dud")
# def gettime(temp):
# 	print(temp)
def main():
	list10 = []
	list11 = []
	getlist = []
	sum1 = 0
	while True:
		try:
			temp = input().split(",")
			try:
				if temp[0] == "task":
					validate(temp)
					str1 = ""
					temp1 = task(temp)
					for each in temp1:
						str1 += each + ", "
					print(str1[0:len(str1)-2])
			except Exception as e:
				print(e)
			if temp[0] == "add-task":
				temp2 = task(temp)
				list10.append(temp2)
				if temp[6] == "todo":
					list11.append(int(temp[3]))
				
				# print(temp2,"2")
			if temp[0] == "print-todoist":
				# print(list10)
				for each in list10:
					str10 = ""
					for val in each:
						str10 += val + ", "
						# print(val)
					print(str10[0:len(str10)-2])
				# print(list10)
				# gettime(temp)
			if temp[0] == "total-time":
				for each in list11:
					sum1 += each
				print(sum1)
			if temp[0] == "get-next":
				tempgetnext = list10
				# print(list10)
				for i in range(len(list10)):
					strget = ""
					# print(list10[i])
					# print(list10[i][1],"l")
					# if list10[i][1] == temp[1]:
					# 	if list10[i][5] != "todo":
					# 		print("null")
					# 		break
					if list10[i][1] == temp[1] and list10[i][3] == "Important" and list10[i][4] == "Not Urgent" and list10[i][5] == "todo":
						strget += list10[i][0] + ", " + list10[i][1] + ", " + list10[i][2] + ", " + list10[i][3] + ", " + list10[i][4] + ", "+ list10[i][5]
						# print("hi")
						print(strget)
						break
				else:
					print("null")
					
					# if len(strget) == 0:
					# 	print("null")

					# if list10[i][1] == temp[1] and list10[i][3] != "Important" or list10[i][4] != "Not Urgent" or list10[i][5] == "todo":
					# 	print(strget)
				# print(getlist,"g")
			# print(list11)
		except EOFError:
			break
	
	
if __name__ == '__main__':
	main()