def tictactoe():
    temp3 = []
    # rowcheck = ''
    # colcheck = ''
    # diagcheck = ''
    winner = None
    for i in range(3):
        temp1 = input()
        temp2 = temp1.split()
        temp3.append(temp2)
    is_valid = is_valid_input(temp3) and is_valid_game(temp3)
    if is_valid:
        winner = rowchec_k(temp3)
        if winner == None:
            winner = colchec_k(temp3)
        if winner == None:
            winner = diag_check(temp3)
        if winner == None:
            winner = "draw"
        
        return winner
    else:
        if not is_valid_input(temp3):
            winner = "invalid input"
        if not is_valid_game(temp3):
            winner = "invalid game"
        return winner
def rowchec_k(temp3):
    '''
    This is to check for rows
    '''
    if temp3[0][0] == temp3[0][1] == temp3[0][2]:
        return temp3[0][0]
    if temp3[1][0] == temp3[1][1] == temp3[1][2]:
        return temp3[1][0]
    if temp3[2][0] == temp3[2][1] == temp3[2][2]:
        return temp3[2][0]
def colchec_k(temp3):
    '''
    This is to check cols
    '''
    if temp3[0][0] == temp3[1][0] == temp3[2][0]:
        return temp3[0][0]
    if temp3[0][1] == temp3[1][1] == temp3[2][1]:
        return temp3[0][1]
    if temp3[0][2] == temp3[1][2] == temp3[2][2]:
        return temp3[0][2]
def diag_check(temp3):
    '''
    This is to check diag
    '''
    if temp3[0][0] == temp3[1][1] == temp3[2][2]:
        return temp3[0][0]
    if temp3[0][2] == temp3[1][1] == temp3[2][0]:
        return temp3[0][2]
def is_valid_input(temp3):
    for i in temp3:
        for j in i:
            if j == "x" or j == "o" or j == ".":
                pass
            else:
                return False
    return True
def is_valid_game(temp3):
    count = 0
    sum1 = 0
    count_d = 0
    for i in temp3:
        for j in i:
            if j == "x":
                count += 1
            if j == "o":
                sum1 += 1
            if j == ".":
                count_d += 1
    if abs(count - sum1 >=2):
        return False
    elif abs(count - sum1 == 0) and count_d > 0:
        return False
    return True



def main():
    res = tictactoe()
    print(res)
if __name__ == '__main__':
    main()
