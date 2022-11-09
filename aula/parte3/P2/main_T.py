#!/usr/bin/env python3

class Animal():
    def __init__(self,name,age,civil_state):
        self.name=name
        self.age=age

    def congratulate(self):
        print('congratulations ',self.name+'!!!!')
        self.age+=1

        

class Dog(Animal):        
    def __init__(self,name,age):
        super.__init__(name=name,age=age)
    def __str__(self):
        text= 'i am '+self.name+' and i am '+str(self.age) +'years old'
        
    
    def congratulate(self):
        print('congratulations ',self.name+'!!!!')
        self.age+=1


class Person(Animal):
    def __init__(self,name,age,civil_state):
        super.__init__(name=name,age=age,civil_state=civil_state)
        # self.civil_state=civil_state
        # self.dog=Dog(name='bobby',age=0)#not inheritance, this is composition



    def __str__(self):
        text= 'i am '+self.name+' and i am '+str(self.age) +'years old'
        text+= 'i am'+self.civil_state
    
    
    def congratulate(self):
        print('congratulations ',self.name+'!!!!')
        self.age+=1

    def marry(self, partner):
        if self.civil_state== 'married':
            print('im not sure this is a good idea')
            return

        if partner.civil_state== 'married':
            print('are you sure you trust '+partner.name)
            return
        print(self.name +'and'+partner.name+ 'are married!!')
        
        self.spouse=partner.name
        self.civil_state='married'

        partner.spouse=self.name
        partner.civil_state='married'

def doNothing(a1,a2,a3):
    print('a1 = '+ str(a1))
    print('a2 = '+str( a2))    
    print('a3 = '+ str(a3))
    print()
    return


def main():
    # doNothing(1,2,3)

    # doNothing(a1=1,a2=2,a3=3)
    # doNothing(a2=2,a3=3,a1=1)

    # doNothing(1,a3=3,a2=2)
    
    p1=Person(name='Joao',age=33,civil_state='married')
    p2=Person(name='Maria',age=34,civil_state='Single')
    d1=Dog(name='Lassie',age=2)


    print('\n\nBefore')
    print(p1)
    print(p2)
    p1.congratulate()
    p2.marry(p1)
   
    print('\n\nBefore')
    print(p1)
    print(p2)



if __name__ == '__main__':
    main()