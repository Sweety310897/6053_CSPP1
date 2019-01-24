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
		except EOFError:
			break
	
	
if __name__ == '__main__':
	main()