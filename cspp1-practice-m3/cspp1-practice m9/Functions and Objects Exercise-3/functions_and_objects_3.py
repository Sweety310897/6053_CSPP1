'''This is 3rd activity'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
def apply_to_each(lis_t, functio_n):
    '''
    List is given and square of function is performed
     and value is returned
    '''
    i = 0
    length = len(lis_t)
    while i < length:
        lis_t[i] = lis_t[i] * lis_t[i]
        i += 1
    return lis_t
def square(num):
    '''
    input number
    output square of that number
    '''
    return num * num  
def main():
    '''
    This is main function
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))
if __name__ == "__main__":
    main()
