#!/usr/bin/env python3
import argparse
from functions import isPerfect


def main():

    maximum_number=60


    parser = argparse.ArgumentParser(description='test for psr.')
    parser.add_argument('integers', metavar='maximum_number', type=int, nargs='+',
                    help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    print("heio")
    for number in range (1, maximum_number):
        print('analyzing number'+str(number))
        if isPerfect(number):
            print(str (number)+' isPerfect')
        else:
            print(str(number)+ ' is not perfect')
            

if __name__=='__main__':
    main()