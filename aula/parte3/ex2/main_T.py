#!/usr/bin/env python3



def addComplex(x, y):
    # add code here ...
    sumof=[x[0]+y[0],x[1]+y[1]]
    return sumof

def multiplyComplex(x, y):
    # add code here ...
    a,b=x
    c,d=y

    real= a*c -b*d
    imaginary= a*b+d*c
    return (real,imaginary)

def printComplex(x):
    # add code here ...
    real,imaginary=x
    print(str(real)+ ' + ' +str(imaginary)+'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    print('sum is: ')    
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()