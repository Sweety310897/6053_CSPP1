'''this is bisection search pgm'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr),
#that takes in two arguments a character and String and
#returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean value.
def isi_n(char, ast_r):
    '''
    input is char and aStr then the ouput is True or False
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char == ast_r[0]:
        return True
    if len(ast_r) == 1:
        return False
    return isi_n(char, ast_r[1: ])
def main():
    '''this is main function'''
    data = input()
    data = data.split()
    print(isi_n((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
