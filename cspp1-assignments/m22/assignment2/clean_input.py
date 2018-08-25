'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
# qu!ck brown fox jump$ over t#e l@zy dog.
# quckbrownfoxjumpovertelzydog
def clean_string(string):
    '''
    Here this leans up the word
    '''
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_range = "0123456789"
    temp_result = ""
    for each in string:
        if each in lower_case or if each in numbers:
            temp_result += each
    return temp_result
def main():
    '''
    This is main function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
