def lister(l):
    output = []
    outer = []
    templi = []
    sum1 = 0
    fsum = 0
    for item in l:
        if type(item) in [list, tuple, set]:
            lister(item)
        else:
            output.append(item)
            sum1 += item
            outer.append(sum1)
        # templi.append(sum1)
    # for each in templi:
    #     fsum += int(each)
    # print(templi)
    print(sum1)
    print(len(l))
    # print(outer,"ou")
    # print(fsum)
def main():
    input1 = eval(input())
    print(lister(input1))
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