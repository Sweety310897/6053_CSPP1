'''This is to add 1 to igven list
'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
def apply_to_each(lis_t, functio_n):
    '''
    input:List
    output List is returned which is inc by 1
    '''
    i = 0
    length = len(lis_t)
    while i <= length-1:
        lis_t[i] = lis_t[i]+1
        i += 1
    return lis_t
def inc(number):
    '''This is to inc number'''
    '''
    input : number
    output: incremented number
    '''
    return number + 1
def main():
    '''This is main pgm'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))
if __name__ == "__main__":
    main()
