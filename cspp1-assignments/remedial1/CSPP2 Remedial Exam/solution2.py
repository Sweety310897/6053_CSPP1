# def countfunction(tempval):
#     if tempval >= 5:
#         print("All Rooms are reserved")
    
def main():
  rangeofinputs = int(input())
  j = 0
  dic = {}
  count = 0
  maxcapacity = 6
  while j < rangeofinputs:
    temp = input().split(" ")
    
    # count += 1
    # if count > 5:
    #     print("All Rooms are reserved")
    if temp[0] == "reserve":
        if count == maxcapacity-1:
            print("All Rooms are reserved")
        else:
            if dic == {}:
                count += 1
                dic[1] = temp[1]
                print(temp[1],1)
            else:
                for i in range(1,maxcapacity):
                    if i not in dic.keys():
                        # print(i)
                        # if i >= maxcapacity:
                        #     print("All Rooms ")
                        #     break
                        dic[i] = temp[1]
                        count += 1
                        print(temp[1],i)
                        # print(hi)
                        break
            
        
            # return
    if temp[0] == "reserveN":
        if count == maxcapacity-1:
            print("All Rooms are reserved")
        elif int(temp[2]) in dic.keys():
            print("Room is already reserved")
            # break
        else:    
            dic[int(temp[2])] = temp[1]
            # print(len(dic),"idc")
            count += 1
            print(temp[1],temp[2])
            # return
        
    if temp[0] == "print":
        for key,value in sorted(dic.items()):
            print(value,key)
    if temp[0] == "build":
        maxcapacity += int(temp[1])
        print("Added" +" "+ temp[1] +" "+ "more rooms")
    # print(count)
    # countfunction(count)
        # break
    j += 1
    
    
if __name__ == '__main__':
    main()

