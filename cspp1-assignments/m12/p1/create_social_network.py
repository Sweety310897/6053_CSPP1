'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    temp = data.split('\n')
    list2 = []
    list3= []
    dict1 = {}
    print(temp)
    length = len(temp)
    print(len(temp))
    
    for i in range(length-1):

    	if temp[i] =='follows':
    		#temp[i] = ":"
    		list2.append(temp[i-1])
    		list3.append(temp[i+1])
    	#list3.append(temp[i+1])
    

    for i in range(len(temp)):
    	#list2=temp[i][0]
    	#list3=temp[i][1]
    	if list2 not in dict1.keys():
    		
    		dict1[list2] = [str(list3[0])]


    print(dict1)
    print(list2)
    print(list3)

    '''
    for i in range(len(list3)):
    	dict1[list2]=list3




    for i in range(len(temp)):
    	list2 = temp[i][0]
    	if list2[0] not in dict1.keys():
    		dict1[list2] = list3[1]
    print(dict1)
    '''




   




def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'


    print(create_social_network(string))

if __name__ == "__main__":
    main()
