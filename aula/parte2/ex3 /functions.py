




maximum_number=60

def getDividers(number):
    """ Args:
        number(int): a number

    """


    dividers=[]
    for i in range(1,number):
        #   '%' returns the remainder of the integer division.
        if number%i ==0:
            # print(str(i) +' is a interger divider or '+str(number)) 
            dividers.append(i)

    # print(str(number) +' is a interger divider or '+str(dividers))
    return(dividers)

def isPerfect(number):

    
    dividers=getDividers(number)
    
    total=sum(dividers)
    if total==number:
        return True
    else:
        return False

