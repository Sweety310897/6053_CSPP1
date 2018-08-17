'''
    Document Distance - A detailed description is given in the PDF
'''
import re
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
        temp7 = element1.strip()
        temp5.append(temp7)
    for element2 in temp4:
        temp8 = element2.strip()
        temp6.append(temp8)
    for word in temp5:
        temp10.append(re.sub('[^ a-zA-Z]', '', word))
    #print(temp10)
    for word in temp6:
        temp11.append(re.sub('[^ a-zA-Z]', '', word))
    stopwords = load_stopwords('stopwords.txt')
    sdictionary1=[]
    sdictionary2=[]
    print(stopwords)

    


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
