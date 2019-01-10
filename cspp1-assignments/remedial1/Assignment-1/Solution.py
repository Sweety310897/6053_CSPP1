def main():
	loadq = input().split(" ")
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	print(loadq[1], "are added to the quiz")
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	i = 0
	list1 = []
	while i < int(loadq[1]):
		temp = input().split(":")
		list1.append(temp)
		i += 1

	startq = input().split(" ")
	# print(list1)
	count = 0
	for i in range(len(list1)):
		templist = list1[i][1]
		templist2 = templist.split(",")
		count += 1
		tempcount = str(count)
		# templist3 = list1[i][0]
		# print(templist3,"3")
		print(list1[i][0] +"("+ tempcount+")")
		print(templist2[0]+"\t"+templist2[1]+"\t"+templist2[2]+"\t"+templist2[3] + "\n")
		# print("")
		# print(list1[i][1])
	j = 0
	list2 = []
	while j < int(startq[1]):
		tempstartq = input().split(" ")
		list2.append(tempstartq)
		j += 1
	# print(list2)
	scorereport = input()
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	marks = []
	sum1 = 0
	for i in range(len(list2)):
		if list2[i][1] == list1[i][2]:
			print(list1[i][0])
			print(" Correct Answer! - Marks Awarded:", list1[i][3])
			sum1 += int(list1[i][3])
			# print(sum1)
		else:
			# print(list1[i][4])
			print(list1[i][0])
			print(" Wrong Answer! - Penalty:", list1[i][3])
			sum1 = sum1 + int(list1[i][4])
			# print(sum1)
	print("Total Score:",sum1)

if __name__ == '__main__':
	main()