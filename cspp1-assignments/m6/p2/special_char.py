'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str1 = str(input())
    temp = ""
    for char in str1:
        if char in "#!@%$&^*":
            temp = temp + " "
        else:
            temp = temp + char
    print(temp)
if __name__ == "__main__":
    main()
