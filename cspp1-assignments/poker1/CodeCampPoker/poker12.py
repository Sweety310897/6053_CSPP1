'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    i = 0
    temp = []
    while i < len(hand):
        if hand[i][0] == 'T':
            k = hand[i][0].replace("T", "10")
            temp.append(int(k))
        elif hand[i][0] == 'J':
            k = hand[i][0].replace("J", "11")
            temp.append(int(k))
        elif hand[i][0] == 'Q':
            k = hand[i][0].replace("Q", "12")
            temp.append(int(k))
        elif hand[i][0] == 'K':
            k = hand[i][0].replace("K", "13")
            temp.append(int(k))
        elif hand[i][0] == 'A':
            k = hand[i][0].replace("A", "14")
            temp.append(int(k))
        else:
            k = hand[i][0]
            temp.append(int(k))
        i += 1
    temp1 = sorted(temp)
    p_tr = 0
    k_tr = 1
    cout1 = 1
    while k_tr < len(temp1) and cout1 == 1:
        if temp1[k_tr]-temp1[p_tr] == 1:
            pass
        else:
            cout1 = 0
        k_tr += 1
        p_tr += 1
    return cout1 == 1


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    is_flush_1 = 1
    i = 0
    j = 1
    while j < len(hand) and is_flush_1 == 1:
        if hand[i][1] != hand[j][1]:
            is_flush_1 = 0
        else:
            is_flush_1 = 1
        i += 1
        j += 1
    return is_flush_1 == 1

def is_four_of_a_kind(hands):
    list2=[]
    temp=[]
    for card in hands:
        list2.append(card[0])
    #print(list2)
    for x in list2:
        temp.append(list2.count(x))
    if max(temp) == 4:
        return True
    else:
        return False
    
    
def is_three_of_a_kind(hands):
    list2=[]
    temp=[]
    for card in hands:
        list2.append(card[0])
    #print(list2)
    for x in list2:
        temp.append(list2.count(x))
    if max(temp) == 3:
        return True
    else:
        return False


def is_one_pair(hands):
    list2=[]
    temp=[]
    for card in hands:
        list2.append(card[0])
    # temp3 = list2
    # for x in temp3(0,5):
    #     temp1 = list2[x]
    #     for y in temp3(1,5):
    #         if temp1 == y:
    #             temp.append(temp1)
    
    for x in list2:
        temp.append(list2.count(x))
    #print(temp)
    if max(temp) == 2:
        return True
    else:
        return False

def is_full_house(hands):
    list2=[]
    temp=[]
    for card in hands:
        list2.append(card[0])
     
    #print(list2)
    temp1=sorted(list2)

    if temp1[0]==temp1[1]==temp1[2]:
        if temp1[3]==temp1[4]:
            return True
    if temp1[0]==temp1[1]:
        if temp1[2]==temp1[3]==temp1[4]:
            return True
    else:
        return False
def highcar_d(hands):
    list2 = []
    for card in hands:
        list2.append(card[0])
    return max(int(list2))/100





def is_two_pair(hands):
    list2=[]
    for card in hands:
        list2.append(card[0])
    length1 = len(list2)
    temp1 = set(list2)
    length2 = len(temp1)
    if length1 - length2 == 2:
        return True
    else:
        return False

    
    


def hand_rank(hand):
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
    is_straight_1 = is_straight(hand)
    is_flush_1 = is_flush(hand)
    if is_flush_1 and is_straight_1:
        return 9
    elif is_four_of_a_kind(hand):
        return 4
    elif is_full_house(hand):
        return 7
    elif is_three_of_a_kind(hand):
        return 3
    elif is_two_pair(hand):
        return 2
    elif is_one_pair(hand):
        return 1
    elif is_straight_1:
        return 5
    elif is_flush_1:
        return 6
    else:
        return highcar_d(hand)

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
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    
