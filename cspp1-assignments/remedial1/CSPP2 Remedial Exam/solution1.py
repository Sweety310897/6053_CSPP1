# # def main():
# # 	list1 = []
# # 	rangeval = int(input())
# # 	i = 0
# # 	dic = {}
# # 	count = 0
# # 	while i < rangeval:
# # 		temp = input().split(" ")
# # 		if temp[0] == "reserve":
# # 			if list1 == []:
				
# # 				count += 1
# # 				dic[count] = temp[1]
# # 				print(dic)
# # 				list1.append(count)
# # 				print(temp[1],count)
# # 			else:
# # 				count += 1
# # 				if count not in list1:
# # 					print(temp[1],count)
# # 				if count in list1:
# # 					print(temp[1],count+1)
# # 		if temp[0] == "reserveN":
# # 			list1.append(int(temp[2]))
# # 			print(temp[1],temp[2])
# # 			# print("reserveN")
# # 		if temp[0] == "print":
# # 			print("print")

# # 		# list1.append(temp)
# # 		i += 1
# # 	# print(list1)
# # if __name__ == '__main__':
# # 	main()
# def main():
# 	rangeofinputs = int(input())
# 	i = 0
# 	list1 = []
# 	temporarykeysmin = 0
# 	temporarykeysmax = 1
# 	dic = {}
# 	length = 0
# 	j = 0
# 	while i < rangeofinputs:
# 		temp = input().split(" ")
# 		if temp[0] == "reserve":
# 			if dic == {}:
# 				dic[1] = temp[1] 
# 			else:
# 				temp = sorted(dic)
# 				# print(type(temp[0]))
# 				# for key in sorted(dic):
# 					# print(key,dic)
# 			# 	sortedval = sorted(dic.keys())
# 				sortedval = list(map(int,temp))
# 				print(type(sortedval[0]))
# 				# print(len(dic))
# 		if temp[0] == "reserveN":
# 			dic[temp[2]] = temp[1]
# 			# print("hi")
		
# 		i += 1
# 	# print(dic)
# 	# print(sortedval)
# if __name__ == '__main__':
# 	main()
def main():
  rangeofinputs = int(input())
  j = 0
  # list1 = []
  # temporarykeysmin = 0
  # temporarykeysmax = 1
  dic = {}
  # length = 0
  while j < rangeofinputs:
    temp = input().split(" ")
    if temp[0] == "reserve":
      if dic == {}:
        dic[1] = temp[1]
        print(temp[1],1)
      else:
        for i in range(1,6):
          if i not in dic.keys():
          	if len(dic) > 5:
          		print("All Rooms are reserved")
          		break
            # tempval1 += 1
            # print(type(dic[tempval1]))
            dic[i] = temp[1]
            print(temp[1],i)
            break

    if temp[0] == "reserveN":
      dic[int(temp[2])] = temp[1]
      print(temp[1],temp[2])
      # print(dic)
    if temp[0] == "print":
    	# print(dic)
    	for key,value in sorted(dic.items()):
    		print(value,key)
    	# for i in range(len(dic)):
    	# 	print()
    	# print(dic.items())
    j += 1
  # print(dic)
if __name__ == '__main__':
  main()