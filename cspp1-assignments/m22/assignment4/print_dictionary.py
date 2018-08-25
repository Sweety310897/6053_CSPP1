'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    dic1 = str(dictionary)
    temp1 = sorted(dic1)
    return temp1
# {'lorem': 2, 'ipsum': 2, 'porem': 2}
# ipsum - 2
# lorem - 2
# porem - 2

# {'This': 1, 'is': 1, 'assignment': 1, '3': 1, 'in': 1, 'Week': 1, '4': 1, 'Exam': 1}
# 3 - 1
# 4 - 1
# Exam - 1
# This - 1
# Week - 1
# assignment - 1
# in - 1
# is - 1

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
