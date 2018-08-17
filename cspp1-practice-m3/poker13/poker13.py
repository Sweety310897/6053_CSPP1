'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def face_values(han_d):
    """
    returns only face values of a hand in a sorted desc order
    """
    return sorted(['--23456789TJQKA'.index(face) for face, suite in han_d], reverse=True)

def is_straight(han_d):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    temp = face_values(han_d)
    if temp == [14, 5, 4, 3, 2]:
        temp = [5, 4, 3, 2, 1]
    set_face_values = set(temp)
    return len(set_face_values) == 5 and max(set_face_values) - min(set_face_values) == 4

def is_flush(han_d):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    return len(set([suit for face, suit in han_d])) == 1

def is_kind_off(f_values, number):
    """
    determines which kind the hand is
    """
    for face in f_values:
        if f_values.count(face) == number:
            return face

def hand_rank(han_d):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    temp = face_values(han_d)
    if is_straight(han_d) and is_flush(han_d):
        return (8, temp)
    if is_kind_off(temp, 4):
        return(7, is_kind_off(temp, 4), temp)
    if is_kind_off(temp, 3) and is_kind_off(temp, 2):
        return (6, (is_kind_off(temp, 3), is_kind_off(temp, 2), temp))
    if is_flush(han_d):
        return (5, temp)
    if is_straight(han_d):
        return(4, temp)
    if is_kind_off(temp, 3):
        return (3, is_kind_off(temp, 3), temp)
    if is_kind_off(temp, 2) and is_kind_off(sorted(temp), 2):
        return (2, (is_kind_off(temp, 2), is_kind_off(sorted(temp), 2)), temp)
    if is_kind_off(temp, 2):
        return(1, is_kind_off(temp, 2), temp)
    return (0, temp)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split()
        # print(face_values(ha))
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
