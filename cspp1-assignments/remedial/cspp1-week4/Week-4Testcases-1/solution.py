def food(temp):
	list1 = []
	list1.append(temp[0])
	str1 = temp[1].split(",")
	# print(str1)
	list2 = []
	list2.append("Food")
	list2.append(str1[1])
	list2.append(str1[2])
	list2.append(str1[0])
	return list2
def water(temp):
	list1 = []
	list1.append(temp[0])
	str1 = temp[1].split(",")
	# print(str1)
	list2 = []
	list2.append("Water")
	list2.append(str1[1])
	list2.append(str1[2])
	list2.append(str1[0])
	return list2
def physical(temp):
	list1 = []
	list1.append(temp[0])
	str1 = temp[1].split(",")
	# print(str1)
	list2 = []
	list2.append("PhysicalActivity")
	list2.append(str1[1])
	list2.append(str1[2])
	list2.append(str1[0])
	return list2
def weight(temp):
	# print(temp)
	list1 = []
	list1.append(temp[0])
	str1 = temp[1].split(",")
	# print(str1)
	list2 = []
	list2.append("Weight")
	list2.append(str1[1])
	list2.append(str1[2])
	list2.append(str1[0])
	return list2
def sleep(temp):
	# print(temp)
	list1 = []
	list1.append(temp[0])
	str1 = temp[1].split(",")
	# print(str1)
	list2 = []
	list2.append("Sleep")
	list2.append(str1[1])
	list2.append(str1[2])
	list2.append(str1[0])
	return list2
def main():
	num = int(input())
	templist = []
	templistwater = []
	templistphysical = []
	templistweight = []
	templistsleep = []
	i = 0
	while i < num:
		temp = input().split(" ")
		if temp[0] == "Food":
			temp = food(temp)
			for each in temp:
				templist.append(each)
			# print(tempfood)
		if temp[0] == "Foodlog":
			strfood = templist[0] + ":"
			# print(templist[0],":")
			strdate = templist[1] + ":"
			print(strfood)
			# print(templist[1],":")
			print(strdate)
			strtimequ = "-" + " " + templist[2] + ":" + " " + templist[3]
			# print("-",templist[2], ":" ,templist[3])
			print(strtimequ)
		if temp[0] == "Water":
			tempwater = water(temp)
			for each in tempwater:
				templistwater.append(each)
		if temp[0] == "Waterlog":
			strwater = templistwater[0] + ":"
			# print(templist[0],":")
			strwdate = templistwater[1] + ":"
			print(strwater)
			strwatertimequant = "-" + " " + templistwater[2] + ":" + " " + templistwater[3]
			# print(templist[1],":")
			print(strwdate)
			# print("-",templistwater[2], ":", templistwater[3])
			print(strwatertimequant)
		# print(templistwater)
		if temp[0] == "PhysicalActivity":
			tempphysical = physical(temp)
			# print(tempphysical)
			for each in tempphysical:
				templistphysical.append(each)
		if temp[0] == "PhysicalActivitylog":
			strphysical = templistphysical[0] + ":"
			# print(templist[0],":")
			strpdate = templistphysical[1] + ":"
			print(strphysical)
			strphytimequant = "-" + " " + templistphysical[2] + ":" + " " + templistphysical[3]
			# print(templist[1],":")
			print(strpdate)
			# print("-",templistwater[2], ":", templistwater[3])
			print(strphytimequant)
		if temp[0] == "Weight":
			tempweight = weight(temp)
			# print(tempweight)
			for each in tempweight:
				templistweight.append(each)
		if temp[0] == "Weightlog":
			strweight = templistweight[0] + ":"
			strweightdate = templistweight[1] + ":"
			print(strweight)
			strwttimequant = "-" + " " + templistweight[2] + ":" + " " + templistweight[3]
			print(strweightdate)
			print(strwttimequant)
		if temp[0] == "Sleep":
			tempsleep = sleep(temp)
			for each in tempsleep:
				templistsleep.append(each)
		if temp[0] == "Sleeplog":
			strsleep = templistsleep[0] + ":"
			strsleepdate = templistsleep[1] + ":"
			print(strsleep)
			strsleeptimequant = "-" + " " + templistsleep[2] + ":" + " " + templistsleep[3]
			print(strsleepdate)
			print(strsleeptimequant)
		if temp[0] == "Summary":
			print("Summary")
			# print(templist[1])
			str10 = templist[1] + ":"
			str11 = templist[0] + ":"
			str12 = "-" + " " + templist[2] + ": "  + templist[3]
			print(str10)
			print(str11)
			print(str12)

			str20 = templistwater[1] + ":"
			str21 = templistwater[0] + ":"
			str22 = "-" + " " + templistwater[2] + ": "  + templistwater[3]
			print(str20)
			print(str21)
			print(str22)

			str30 = templistphysical[1] + ":"
			str31 = templistphysical[0] + ":"
			str32 = "-" + " " + templistphysical[2] + ": "  + templistphysical[3]
			print(str30)
			print(str31)
			print(str32)

			str40 = templistweight[1] + ":"
			str41 = templistweight[0] + ":"
			str42 = "-" + " " + templistweight[2] + ": "  + templistweight[3]
			print(str40)
			print(str41)
			print(str42)

			str50 = templistsleep[1] + ":"
			str51 = templistsleep[0] + ":"
			str52 = "-" + " " + templistsleep[2] + ": "  + templistsleep[3]
			print(str50)
			print(str51)
			print(str52)

			


			# print(templist,"tl")

		i += 1 
if __name__ == '__main__':
	main()