def food(temp):
	list1 = []
	# print(temp)
	dic = {}
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
	i = 1
	while i <= num:
		# print(i)
		temp = input().split(" ")
		if temp[0] == "Food":
			temp = food(temp)
			for each in temp:
				templist.append(each)
			# print(tempfood)
		if temp[0] == "Foodlog":
			print("Food:")
			dic1 = {}
			for z in range(len(templist)):
				if templist[z] == "Food":
					if templist[z+1] not in dic1:
						dic1[templist[z+1]] = [templist[z+2]]
						dic1[templist[z+1]] +=  [templist[z+3]]
					else:
						dic1[templist[z+1]] += [templist[z+2]]
						dic1[templist[z+1]] += [templist[z+3]]
			for key,value in sorted(dic1.items()):
				tempkey = key + ":"
				print(tempkey)
				tempval = value
				k = 1
				for y in range(len(tempval)):
					if y%2 == 0:
						str100 = "-" + " " +  tempval[y] + ": " +  tempval[y+1]
						print(str100)
		if temp[0] == "Water":
			tempwater = water(temp)
			for each in tempwater:
				templistwater.append(each)
		if temp[0] == "Waterlog":
			print("Water:")
			dicw = {}
			# print(templistwater,"w")
			for z in range(len(templistwater)):
				if templistwater[z] == "Water":
					if templistwater[z+1] not in dicw:
						dicw[templistwater[z+1]] = [templistwater[z+2]]
						dicw[templistwater[z+1]] +=  [templistwater[z+3]]
						# print(dicw)
					else:
						dicw[templistwater[z+1]] += [templistwater[z+2]]
						dicw[templistwater[z+1]] += [templistwater[z+3]]
					# print(dicw)
			for key,value in sorted(dicw.items()):
				tempkey = key + ":"
				print(tempkey)
				tempval = value
				k = 1
				for y in range(len(tempval)):
					if y%2 == 0:
						str100 = "-" + " " +  tempval[y] + ": " +  tempval[y+1]
						print(str100)
			
		if temp[0] == "PhysicalActivity":
			tempphysical = physical(temp)
			for each in tempphysical:
				templistphysical.append(each)
		if temp[0] == "PhysicalActivitylog":
			print("PhysicalActivity:")
			dicp = {}
			# print(templistwater,"w")
			for z in range(len(templistphysical)):
				if templistphysical[z] == "PhysicalActivity":
					if templistphysical[z+1] not in dicp:
						dicp[templistphysical[z+1]] = [templistphysical[z+2]]
						dicp[templistphysical[z+1]] +=  [templistphysical[z+3]]
					else:
						dicp[templistphysical[z+1]] += [templistphysical[z+2]]
						dicp[templistphysical[z+1]] += [templistphysical[z+3]]
			for key,value in sorted(dicp.items()):
				tempkey = key + ":"
				print(tempkey)
				tempval = value
				k = 1
				for y in range(len(tempval)):
					if y%2 == 0:
						str100 = "-" + " " +  tempval[y] + ": " +  tempval[y+1]
						print(str100)
		if temp[0] == "Weight":
			tempweight = weight(temp)
			# print(tempweight)
			for each in tempweight:
				templistweight.append(each)
		if temp[0] == "Weightlog":
			print("Weight:")
			dicwt = {}
			# print(templistwater,"w")
			for z in range(len(templistweight)):
				if templistweight[z] == "Weight":
					if templistweight[z+1] not in dicwt:
						dicwt[templistweight[z+1]] = [templistweight[z+2]]
						dicwt[templistweight[z+1]] +=  [templistweight[z+3]]
					else:
						dicwt[templistweight[z+1]] += [templistweight[z+2]]
						dicwt[templistweight[z+1]] += [templistweight[z+3]]
			for key,value in sorted(dicwt.items()):
				tempkey = key + ":"
				print(tempkey)
				tempval = value
				k = 1
				for y in range(len(tempval)):
					if y%2 == 0:
						str100 = "-" + " " +  tempval[y] + ": " +  tempval[y+1]
						print(str100)
		if temp[0] == "Sleep":
			tempsleep = sleep(temp)
			for each in tempsleep:
				templistsleep.append(each)
		if temp[0] == "Sleeplog":
			print("Sleep:")
			dicsl = {}
			# print(templistwater,"w")
			for z in range(len(templistsleep)):
				if templistsleep[z] == "Sleep":
					if templistsleep[z+1] not in dicsl:
						dicsl[templistsleep[z+1]] = [templistsleep[z+2]]
						dicsl[templistsleep[z+1]] +=  [templistsleep[z+3]]
					else:
						dicsl[templistsleep[z+1]] += [templistsleep[z+2]]
						dicsl[templistsleep[z+1]] += [templistsleep[z+3]]
			for key,value in sorted(dicsl.items()):
				tempkey = key + ":"
				print(tempkey)
				tempval = value
				k = 1
				for y in range(len(tempval)):
					if y%2 == 0:
						str100 = "-" + " " +  tempval[y] + ": " +  tempval[y+1]
						print(str100)
			# strsleep = templistsleep[0] + ":"
			# strsleepdate = templistsleep[1] + ":"
			# print(strsleep)
			# strsleeptimequant = "-" + " " + templistsleep[2] + ":" + " " + templistsleep[3]
			# print(strsleepdate)
			# print(strsleeptimequant)
		if temp[0] == "Summary":
			print("Summary:")
			# print(templist[1])
			str10 = templist[1] + ":"
			str11 = templist[0] + ":"
			str12 = "-" + " " + templist[2] + ": "  + templist[3]
			print(str10)
			print(str11)
			print(str12)

			# str20 = templistwater[1] + ":"
			str21 = templistwater[0] + ":"
			str22 = "-" + " " + templistwater[2] + ": "  + templistwater[3]
			# print(str20)
			print(str21)
			print(str22)

			# str30 = templistphysical[1] + ":"
			str31 = templistphysical[0] + ":"
			str32 = "-" + " " + templistphysical[2] + ": "  + templistphysical[3]
			# print(str30)
			print(str31)
			print(str32)

			# str40 = templistweight[1] + ":"
			str41 = templistweight[0] + ":"
			str42 = "-" + " " + templistweight[2] + ": "  + templistweight[3]
			# print(str40)
			print(str41)
			print(str42)

			# str50 = templistsleep[1] + ":"
			str51 = templistsleep[0] + ":"
			str52 = "-" + " " + templistsleep[2] + ": "  + templistsleep[3]
			# print(str50)
			print(str51)
			print(str52)
			# print(templist,"tl")

		i += 1 
if __name__ == '__main__':
	main()