'''This is odd strings pgm'''
#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers
# in the tuple as input and returns a tuple in which contains odd index values in the input tuple
def oddtuple_s(atu_p):
    '''
    aTup: a tuple
    input : aTup
    output: odd range of aTup
    returns: tuple, every other element of aTup.
    '''
    return atu_p[::2]
def main():
    '''this is main function'''
    data = input()
    data = data.split()
    atu_p = ()
    for j in range(len(data)):
        atu_p += ((data[j]),)
    print(oddtuple_s(atu_p))
if __name__ == "__main__":
    main()
