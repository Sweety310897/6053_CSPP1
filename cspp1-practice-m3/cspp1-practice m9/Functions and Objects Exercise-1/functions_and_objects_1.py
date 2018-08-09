'''This pgm is to perform abs value in given list'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9]
#into [1, 4, 8, 9]
def apply_to_each(lis_t, functio_n):
    #List is passed and absolute is performed
    '''
    input-List is given
    output is abs value
    '''
    i = 0
    length = len(lis_t)
    while i < length:
        lis_t[i] = functio_n(lis_t[i])
        i += 1
    return lis_t
def main():
    '''This is amin function where data is taken as input to
    list1
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()
