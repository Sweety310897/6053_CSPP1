# #s = "726493815315728946489651237852147693673985124941362758194836572567214389238579461"
# # list1 = []
# # for i in range(len(s)):
# # 	temp = s[0:9]
# # 	list1.append(temp)
# # 	print(list1)
# inp = input()
# inp = list(inp)
# print(inp)
# print("hi")
# lis = []
# i = 0
# temp = []
# for i in range(len(inp)):
# 	print(i)
# 	if i%9==0 and i!=0:
# 		lis.append(temp)		
# 		print(lis)
# 		temp = []
# 	temp.append(inp[i])
# lis.append(temp)
# print(lis)
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + count)
    iteration += 1 