'''
    Tiny Search Engine - Part 2 - Search
    In this programming assingment you are given the search index and search queries as input.
    Complete the program below to search in the index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.
    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
    The second input to this program is search queries.
    Each search query has one or more words
    A search query has to be tokenized i.e., the words have to be extracted
    This word may be a key in the search index.
    If the word is a key then collect the values.
    Collect the values from the search index for all the words in the search query.
    Make a set using the doc_id present as the first item in the values tuple.
    Return the search results.

    Note: PyLint score need not be 10/10. Anything above 9.5 is good.
'''

def search(search_index, query):
    '''
        function to search through the search index and return the results
        split the query into lowercase words
        check if the word is in the search_index
        collect all the values for the words that are in the search_index
        make a set of doc_id and return
    '''
    dict1 = {}
    temp = query.lower()
    #print(temp)
    list1 = []
    #length = len()
    temp1 = temp.split()
    
   
    for everyelement in temp1:
        if everyelement in search_index:
            list1 = search_index[everyelement]
        length = len(list1)
        print(length)

        




    # print(temp1[0],"temp1")
    # print(type(search_index))
    # #print(temp1)
    # #print(query)
    # length = len(temp)
    # for i in temp1:
    #     print(temp1)
        # for temp1[i] in query:
        #     print(temp1, "this is temp1")
        #     if temp1 in search_index.keys():
        #         print(search_index.keys())
         #values.add(search_index.values())
    #temp1 = set(values)
    #return temp1


def process_queries(search_index, queries):
    '''
        function to process the search queries
        iterate through all the queries and call the search function
        print the results returned by search function
    '''
    for eachquery in queries:
        temp10 = search(search_index,eachquery)
    print(temp10)
def main():
    '''
        main function
    '''
    # This line loads the search index
    search_index = eval(input())
    print(search_index)

    # read the number of search queries
    lines = int(input())
    
    # read the search queries into a list
    queries = []
    for i in range(lines):
        queries.append(input())
        i += 1

    # call process queries
    process_queries(search_index, queries)

if __name__ == '__main__':
    main()