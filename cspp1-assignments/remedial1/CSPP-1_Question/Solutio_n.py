from collections import Counter
'''this is main
    pgm'''
#main function.
def main():
    """
    { item_description }
    """
    inpu_t = input()
    list1 = []
    temp1 = 0
    #print(list1)
    #temp = 0123456789"
    coun_t = 0
    #print(len(inpu_t))
    for each in inpu_t:
        if int(each) >= 1 and int(each) <= 9:
            coun_t = coun_t + 1
        if len(inpu_t) < 81:
            print("Invalid input")
    #print(count)
    if coun_t == 81:
        print("Given sudoku is solved")
    # sudoku = []
    # for _ in range(9):
    #     row = input().split("\n")
    #     print(row)
    #     sudoku.append(row)
     #   print(sudoku)
    #print(check_sudoku(row))

if __name__ == '__main__':
    main()
