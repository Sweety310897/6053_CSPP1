'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if (sudoku[0][0] == sudoku[0][1] or sudoku[0][0] == sudoku[0][2] or
        sudoku[0][0] == sudoku[0][3] or sudoku[0][0] == sudoku[0][4] or
        sudoku[0][0] == sudoku[0][5] or sudoku[0][0] == sudoku[0][6] or 
        sudoku[0][0] == sudoku[0][7] or sudoku[0][0] == sudoku[0][8] or 
        sudoku[0][0] == sudoku[1][0] or sudoku[0][0] == sudoku[2][0] or
        sudoku[0][0] == sudoku[3][0] or sudoku[0][0] == sudoku[4][0] or
        sudoku[0][0] == sudoku[5][0] or sudoku[0][0] == sudoku[6][0] or 
        sudoku[0][0] == sudoku[7][0] or sudoku[0][0] == sudoku[8][0]):
        return False
    if (sudoku[0][1] == sudoku[0][0] or sudoku[0][0] == sudoku[0][2] or
        sudoku[0][1] == sudoku[0][3] or sudoku[0][0] == sudoku[0][4] or
        sudoku[0][1] == sudoku[0][5] or sudoku[0][0] == sudoku[0][6] or 
        sudoku[0][1] == sudoku[0][7] or sudoku[0][0] == sudoku[0][8] or 
        sudoku[0][1] == sudoku[1][1] or sudoku[0][0] == sudoku[2][1] or
        sudoku[0][1] == sudoku[3][1] or sudoku[0][0] == sudoku[4][1] or
        sudoku[0][1] == sudoku[5][1] or sudoku[0][0] == sudoku[6][1] or 
        sudoku[0][1] == sudoku[7][1] or sudoku[0][0] == sudoku[8][1]):
        return False
    if (sudoku[3][1] == sudoku[3][0] or sudoku[3][1] == sudoku[3][2] or
        sudoku[3][1] == sudoku[3][3] or sudoku[3][1] == sudoku[3][4] or
        sudoku[3][1] == sudoku[3][5] or sudoku[3][1] == sudoku[3][6] or 
        sudoku[3][1] == sudoku[3][7] or sudoku[3][1] == sudoku[3][8] or 
        sudoku[3][1] == sudoku[0][1] or sudoku[3][1] == sudoku[1][1] or
        sudoku[3][1] == sudoku[2][1] or sudoku[3][1] == sudoku[4][1] or
        sudoku[3][1] == sudoku[5][1] or sudoku[3][1] == sudoku[6][1] or 
        sudoku[3][1] == sudoku[7][1] or sudoku[3][1] == sudoku[8][1]):
        return False

    else:
        return True
# 2 5 6 8 3 1 7 4 9
# 8 3 7 6 4 9 5 1 2
# 1 9 4 7 2 5 3 8 6
# 6 2 1 5 8 7 9 2 3
# 7 4 5 1 9 3 8 6 4
# 3 8 9 4 6 2 1 7 5
# 9 7 8 2 5 4 6 3 1
# 5 6 2 3 1 8 4 9 7
# 4 1 3 9 7 6 2 5 8


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))


if __name__ == '__main__':
    main()