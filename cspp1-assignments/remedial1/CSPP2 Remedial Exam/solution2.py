def main():
  rangeofinputs = int(input())
  j = 0
  dic = {}
  maxcapacity = 6
  while j < rangeofinputs:
    temp = input().split(" ")
    if temp[0] == "reserve":
        if dic == {}:
            dic[1] = temp[1]
            print(temp[1],1)
        else:
            for i in range(1,maxcapacity):
                if i not in dic.keys():
                    # print(i)
                    if i >= maxcapacity:
                        print("All Rooms are reserved")
                        break
                    dic[i] = temp[1]
                    print(temp[1],i)
                    # print(hi)
                    break
    if temp[0] == "reserveN":
        # print(len(dic),"lp")
        if len(dic) >= maxcapacity:
            print("All Rooms are reserved")
        
        elif int(temp[2]) in dic.keys():
            print("Room is already reserved")
            # break
        else:    
            dic[int(temp[2])] = temp[1]
            # print(len(dic),"idc")
            print(temp[1],temp[2])
            # return
        
    if temp[0] == "print":
        for key,value in sorted(dic.items()):
            print(value,key)
    if temp[0] == "build":
        maxcapacity += int(temp[1])
        print("Added" +" "+ temp[1] +" "+ "more rooms")
    j += 1
if __name__ == '__main__':
    main()

