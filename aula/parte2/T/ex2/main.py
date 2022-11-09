#!/usr/bin/env python3

from function import isPerfect




def main():

    maximum_number = 50  # maximum number to test.

    # write the code ...
    print('Testing for perfect numbers!')

    for number in range(1, maximum_number+1):
        print('Analyzing number ' + str(number))
        if isPerfect(number):
            print(str(number) + ' is perfect!')
        else:
            print(str(number) + ' is not perfect!')



if "__name__"=='__main()__':
    main()           