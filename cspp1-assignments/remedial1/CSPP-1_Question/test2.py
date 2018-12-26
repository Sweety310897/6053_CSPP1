def greet_person(sPersonName):
    """
    says hello
    """
    if sPersonName <= 81:
        raise Exception("we don't like you, Robert")
    print ("Hi there")
print(greet_person(86))