#!/usr/bin/env python3



from numpy import real


class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        # addapt code to use classes

        self.r= self.r+y.r
        self.i=self.i+y.i

    def multiply(self, y):
        
        real= self.r*y.r-self.i*y.i
        imaginary= self.r*self.i+y.i*y.r
        
        self.r=real
        self.y=imaginary
        # addapt code to use classes


    def __str__(self):
        return str(self.r) +' + '+ str(self.i)+'i'
        #adapt to one of the classes

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    print(c2)
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    
    # test multiply
    print('\n\nmultiplication')
    print(c1)
    print(c2)
      # uses the __str__ method in the class
    c2.multiply(c1)
    print(c2)  # uses the __str__ method in the class



if __name__ == '__main__':
    main()