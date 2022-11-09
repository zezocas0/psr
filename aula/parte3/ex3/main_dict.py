#!/usr/bin/env python3

from collections import namedtuple

complex= namedtuple('complex',['r','i'])


def addComplex(x, y):
    # add code here ...
    # sumof=[x[0]+y[0],x[1]+y[1]]
    
    a=x['r']
    b=x['i']
    c=y['r']
    d=y['i']
    real= a+c
    imaginary=b+d
    return {'r':real,'i':imaginary}

def multiplyComplex(x, y):
    # add code here ...
    # a,b=x
    # c,d=y

    a=x['r']
    b=x['i']
    c=y['r']
    d=y['i']

    real= a*c -b*d
    imaginary= a*b+d*c
    return {'r':real,'i':imaginary}

def printComplex(x):
    # add code here ...
    real,imaginary=x
    real=x.r
    imaginary=x.i

    print(str(real)+ ' + ' +str(imaginary)+'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = {'r':5,'i':7}
    c2 = {'r':-2,'i':1}
    print(c1)
    print(c2)


    # Test add
    c3 = addComplex(c1, c2)
    print('sum is: ')    
    print(c3)

    # test multiply
    print(multiplyComplex(c1, c2))




if __name__ == '__main__':
    main()