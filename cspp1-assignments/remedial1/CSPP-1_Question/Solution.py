#python sudoku pgm.
def main():
    inpu_t = input()
    #temp = 0123456789"
    coun_t = 0
    #print(len(inpu_t))
    for each in inpu_t:
        if int(each) >= 1 and int(each) <= 9:
            coun_t = coun_t + 1
    #print(count)
    if coun_t == 81:
        print("Given sudoku is solved")
if __name__ == '__main__':
    main()