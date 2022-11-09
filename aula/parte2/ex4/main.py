#!/usr/bin/env python3


from readchar import config, readkey, key 



#EX4.a
def printAllCharsUpTo(stop_char):

    while True:
        print("enter a key")
        ukey=readkey()
        
        print(' you pressed '+ukey)

        if key == stop_char:
            break


#ex 4.b
def printAllPreviousChars():
    print("enter a key")

    ukey=readkey() #le a tecla
    thekey=ord(ukey)#transforma em ascii
    print('printing all chards up to '+ukey)

    characters=[]
    for number in range(32,thekey):
        character=chr(number)
        characters.append(character)

    print (characters)



#EX4.c
#processo 1. ler inputs todos e po-los numa lista
def countNumbersUpTo(stop_char):
    keys=[]
 
    while True:
        print('enter a key ')
        key=readkey()
        print ('you pressed '+ key)

        if key ==stop_char:                     
            break

        keys.append(key)

    print('user pressed'+str(keys))


    #processo 2./5.a processar a lista de keytaps and figure out 
    # which are numbers
    keys_numbers=[]
    keys_others=[]
    for key in keys:
        if key.isnumeric():
            keys_numbers.append(key)
        else:
            keys_others.append(key)


   

    print('key numbers'+ str(keys_numbers) )
    print('key others ' + str(keys_others)) 
    
    #EX5.c
    keys_dict={}
    counter=0
    for key in keys:
        keys_dict[counter]= key

        counter+=1
    print(keys)


def main():
   #EX4.a
#    print( printAllCharsUpTo('X'))
   
   
    #EX4.b
#    print (AllPreviousChars())
   
   
   #EX4c /EX5.a)
   print (countNumbersUpTo('X'))


if __name__=='__main__':
    main()