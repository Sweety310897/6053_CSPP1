def imagelinks(fh):
	templist1 = []
	temp1 = fh.split("img src=")
	head = "src=\""
	tail = "\""
	# print(temp1)
	count = 0
	for each in temp1:
		templist1.append(each)
	# temp2 = temp.split("<img")
	# print(temp2)
	# print("hi")
	for j in templist1:
		if head in j:
			valu = j.index(head)
			# print(valu)
			j = j[valu + len(head):]
			temppp = j.index(tail)
			print(j[:temppp])
			count += 1
	print(count)
	
	# print(templist1[0])
	# print("hello")
	# print(templist1[1])

	
	#print(templist1)
def listlinks(h):
	#print("hello")
	# print(h)
	temp = h.split("<li>")
	#print(temp)
	head = ">"
	tail = "</a"
	list1= []
	list2 = []
	count = 0
	for each in temp:
		list1.append(each)
	for j in list1:
		if head in j:
			#print(list1)
			# print(list1.split("">""))
			val = j.index(head)
			j = j[val + len(head):]
			temporart = j.index(tail)
			#print(j.index(tail))
			# print(j[:])
			# list2.append(j[:temporart])
			print(j[:temporart])
			count += 1
	print(count)
	#print(list2)

def backlinks(fh):
	#temp1 = fh.split("}")
	temp = fh.split("{")
	list1 = []
	list2 = []
	count = 0
	head = "background-color:"
	tail = ";"
	for each in temp:
		list1.append(each)
	# print(list1)
	# print("hi")
	end = "@"
	for j in list1:
		if head in j:
			valu = j.index(head)
			#print(valu)
			j = j[valu + len(head):]

			temppp = j.index(tail)
			print(j[:temppp])
			count += 1
	print(count)
	# print(temp1)
	# list1 = []
	# list2 = []
	# for each in temp1:
	# 	list1.append(each)
	# 	print(list1)
	# 	print("\n")
	# for j in list1:
	# 	if j == "background-color":
	# 		list2.append(temp1[j])
	# print(list2)
	# for each in range(len(fh)):






def main():
	fh = open("webpage5.html",encoding = "utf8").read()
	input1 = input()
	if input1 == "image":
		imagelinks(fh)
	if input1 == "background":
		backlinks(fh)
	#print("hi")
	if input1 == "list":
		listlinks(fh)
if __name__ == '__main__':
	main()