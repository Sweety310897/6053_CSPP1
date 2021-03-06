'''
This is used to check similarity between two files
'''

import re
import math


def combine_dictionaries(dictionary_one, dictionary_two):
    '''
    This function is to combine dictionaries
    '''
    dictionary = {}
    for everyword in dictionary_one:
        if everyword in dictionary_two:
            dictionary[everyword] = [dictionary_one[everyword], dictionary_two[everyword]]
    for everyword in dictionary_one:
        if everyword not in dictionary:
            dictionary[everyword] = [dictionary_one[everyword], 0]
    for everyword in dictionary_two:
        if everyword not in dictionary:
            dictionary[everyword] = [0, dictionary_two[everyword]]
    return dictionary

def calculate_similarity(dictionary_values):
    '''
    This function is to calculate similarity
    '''

    sum1 = 0
    sum2 = 0
    numerator = 0
    for everykey in dictionary_values.keys():
        numerator += (dictionary_values[everykey][0] * dictionary_values[everykey][1])
        sum1 += dictionary_values[everykey][0]**2
        sum2 += dictionary_values[everykey][1]**2
    sum3 = (numerator/(math.sqrt(sum1)*math.sqrt(sum2)))
    return sum3




def create_dictionary(words_list):
    '''
    This function is used to create dictionary
    '''
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary


def clean_text(text_input):
    '''
    This function is to remove special characters
    '''
    words = text_input.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words


def similarity(text_input_one, text_input_two):
    '''
    this function is to calculate siilarity
    '''
    dictionary_one = create_dictionary(clean_text(text_input_one))
    dictionary_two = create_dictionary(clean_text(text_input_two))
    dictionary = combine_dictionaries(dictionary_one, dictionary_two)
    return calculate_similarity(dictionary)


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
#print(load_stopwords(filename))
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
