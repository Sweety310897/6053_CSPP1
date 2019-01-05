def lister(l,templen):
    output = []
    outer = []
    templi = []
    sum1 = 0
    str1 = ""
    fsum = 0
    for item in l:
        if type(item) in [list, tuple, set]:
            lister(item,templen)
        else:
            output.append(item)
            sum1 += item
            # str1 += sum1
            outer.append(sum1)
        # templi.append(sum1)
    # print(output)
    for each in output:
        fsum += float(each)
    print(fsum)
    print(templen)
    # print(output[0],"0")
def main():
    input1 = eval(input())
    temp = len(input1)
    tempvalues = lister(input1,temp)
    # print(tempvalues)
    # sum1 = 0
    # j = 1
    # i = 0
    # count = 0
    # temp = "0123456789"
    # list1 = []
    # res = []
    # for val in input1:
    #     if type(val) not in [list, set, tuple]:
    #         list1.append(val)
    #     else:
    #         list1.extend(get_values(val))
    # return res
    # for i in input1:
    #   for j in i:
    #       list1.append(j)
        
            # print(sum1)
    # print(list1)
    
    # input2 = input1.split("")
if __name__ == '__main__':
    main()