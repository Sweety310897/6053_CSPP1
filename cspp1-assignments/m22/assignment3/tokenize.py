'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    pass
def main():
    '''
    This is main function
    '''
    noof_lines = int(input())
    for _ in range(noof_lines):
        words_input = input()
        #temp10.append(words_input)
    words_input = words_input.split()
    temp_list = list(words_input)
    dictionary_1 = {}
    for word in temp_list:
        if word not in dictionary_1:
            dictionary_1[word] = 1
        else:
            dictionary_1[word] += 1
    print(dictionary_1)
    #print(temp)
# 1
# lorem ipsum porem lorem ipsum porem
# {'lorem': 2, 'ipsum': 2, 'porem': 2}
# 2
# James, while John had had "had", had had "had had";
# "had had" had had a better effect on the teacher.
if __name__ == '__main__':
    main()
