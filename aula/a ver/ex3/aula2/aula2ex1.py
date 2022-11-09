#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, Setember 2020.
# --------------------------------------------------

from multiprocessing.sharedctypes import Value


maximum_number = 100  # maximum number to test.


def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    # <Add stuff here>
    for divider in range(2, value):
        remainder = value % divider
        # print(str(x) + '/' + str(divider) + ' tem resto ' + str(remainder))

        if remainder == 0:
            print('This number is not prime. Tested dividers are ' + 
                  str(list(range(2,divider +1))))
            return False


    
    return []


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
    aux = 2^(value-1)*(2^Value-1)   
    
    return 


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()