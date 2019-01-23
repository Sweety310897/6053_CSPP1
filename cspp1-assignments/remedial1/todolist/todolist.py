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

def main():
	
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
	
if __name__ == '__main__':
	main()