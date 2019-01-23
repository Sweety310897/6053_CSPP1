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
	return list1
def main():
	
	temp = input().split(",")			
	if temp[0] == "task":
		str1 = ""
		temp1 = task(temp)
		for each in temp1:
			str1 += each + ", "
		print(str1)
if __name__ == '__main__':
	main()