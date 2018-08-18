'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
#filename = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    temp1=dict1.lower()
    temp2=dict2.lower()
    temp3=temp1.split()
    temp4=temp2.split()
    temp5=[]
    temp6=[]
    temp10 = []
    temp11=[]

    for element1 in temp3:
        temp5.append(element1.strip())
    for element2 in temp4: 
        temp6.append(element2.strip())
    for word in temp5:
        temp10.append(re.sub('[^ a-zA-Z]', '', word))
    #print(temp10)
    for word in temp6:
        temp11.append(re.sub('[^ a-zA-Z]', '', word))
    stopwords = load_stopwords("stopwords.txt")
    temp7 = temp10[:]
    temp8 = temp11[:]
    for word in temp7:
        if word in stopwords and len(word) > 0:
            temp10.remove(word)
    for word in temp8:
        if word in stopwords and len(word) > 0:
            temp11.remove(word)
    #print(temp10)
    #print(temp11)
    dictionary1={}
    for word in temp10:
        count=0
        if word not in dictionary1:
            dictionary1[word] = 1
        else:
            dictionary1[word] += 1
    dictionary2={}
    for word in temp11:
        count=0
        if word not in dictionary2:
            dictionary2[word] = 1
        else:
            dictionary2[word] += 1
    
    keys=list(dictionary1.keys())+list(dictionary2.keys())
    
    dictionary3 = {}
    for k in keys:
        dictionary3[k] = [0, 0]
    #print(dictionary3)

    for var in dictionary1.keys():
        dictionary3[var][0] = dictionary1[var]
    for var in dictionary2.keys():
        dictionary3[var][1] = dictionary2[var]
    

    #print(dictionary3)
    #print(dictionary3[1])
    for everykey in dictionary3.keys:
        numerator = dictionary3[everykey][0] * dictionary3[everykey][1]
        denominator = (sqrt(dictionary3[everykey][0]**2)) * (sqrt(dictionary3[everykey][1]**2))
    final = numerator/denominator
    print(final)






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
