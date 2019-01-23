def addtask(temp):
	str1 = ""
	str1 = temp[1] +", " + temp[2] + ", " + temp[3] + ", "
	if temp[4] == "y":
		str1 += "Important" + ", "
	else:
		str1 += "Not Important" + ", "
	if temp[5] == "y":
		str1 += "Urgent" + ", "
	else:
		str1 += "Not Urgent" + ", "
	str1 += temp[6]
	print(str1)
def validate(temp):
	# print(temp[6]=="todo")
	if temp[1] == "":
		raise Exception("Title not provided")
	if int(temp[3]) < 0:
		raise Exception("Invalid timeToComplete " + temp[3])
	if temp[6] != "todo" and temp[6] != "done" :
		raise Exception("Invalid status dud")
	
def main():
	try :
		sum1 = 0
		while True:
			try:
				temp = input().split(",")
				# print(temp)
				if temp[0] == "add-task":
					validate(temp)
				if temp[0] == "task":
					addtask(temp)
				if temp[0] == "add-task":
					addtask(temp)
				if temp[0] == "print-todoist":
					print(temp)
				if temp[0] == "total-time":
					totaltime(temp)
					
			except EOFError:
				break
	# print(sum1)
	except Exception as e:
		print(e)
	
if __name__ == '__main__':
	main()