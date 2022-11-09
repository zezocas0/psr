#!/usr/bin/env python3

from numpy import require
from function import isPerfect

import argparse


def main():

        parser = argparse.ArgumentParser(description='definir valor maximo.')
        parser.add_argument('-mn','--max_number',type=int , required= True
                ,help='o valor maximo a verificar se é perfeito')
        parser.add_argument('valor',type=int ,required= False
                ,help=" valor maximo a ser medido")
        
        args = parser.parse_args()
        answer=isPerfect(args.valor)


        for number in range(1,args.valor+1):
                if isPerfect(number):
                        print(str(number) + ' is perfect!')
                else:
                        print(str(number) + ' is not perfect!')



# print('Testing for perfect numbers!')

# for number in range(1, args+1):
#     print('Analyzing number ' + str(number))
#     if isPerfect(number):
#         print(str(number) + ' is perfect!')
#     else:
#         print(str(number) + ' is not perfect!')





if __name__ == '__main__':
    main()


