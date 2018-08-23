def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix(matrix1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    pass
    



    #print(matrix1)

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    
    # #print(matrix1_rows,matrix1_cols)
    rows = int(input('enter no of rows'))
    cols = int(input('enter no of cols'))
    matrix1 = []
    for i in range(cols):
        matrix1.append([])
    #print(matrix1,"matrix1 first for")
    for i in range(rows):
        for j in range(cols):
            matrix1[i].append(j)
            matrix1[i][j] = 0
    #print(matrix1,"matrix1 second for")
    for i in range(rows):
        for j in range(cols):
            matrix1[i][j] = int(input())
    #print(matrix1,"matrix1 third for")
    print(matrix1)

    






    # 3,3
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # 3,3
    # 1 0 0
    # 0 1 0
    # 0 0 1
if __name__ == '__main__':
    main()
