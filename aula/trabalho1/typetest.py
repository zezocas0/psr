#!/usr/bin/env python3

import argparse
from re import T
from colorama import Fore
import datetime
import os
import random

from readchar import readkey
import string
import time
import pprint 



def typetest(mv, utm):
    pool = string.ascii_lowercase #gets all lowercase letters of the alphabet
    
    user = os.getlogin() # gets the user's username
    
    now = datetime.datetime.now() #gets current date
    now = now.strftime("%B %Y") #formats date to month and year
    number_of_hits = 0
    number_of_types = 0
    accuracy = 0
    inputs= [] #shows the letter supposed to hit, the letter the user hit + the time to hit it

    
    print("\nTyping Test, "+ user + ", "+ now)

    test_start = datetime.datetime.now()
    test_start = test_start.strftime("%a %-d %b %-H:%M:%S %Y")
    test_start_time=time.time() #tempo como um numero
    if utm == True:
        print("Test running up to " + str(mv) + " seconds.")
        print('Press any key to start the test.')
        readkey()
        start_time = time.time() #stores the start time

        while time.time()-start_time < mv: #runs loop while duration (mv) is not exceeded
            startinput_time=time.time()
            
            topress=random.choice(pool) #selects a key to press
            print('Type letter '+ Fore.LIGHTBLUE_EX + topress + Fore.WHITE)
            
            keypress = readkey()#reads pressed key
            finishinput_time=time.time()
            if ord(keypress) == 32: #if space is pressed program stops
                break
        
            elif ord(keypress) == ord(topress): # if its correct shows the right one in green, if not, shows it in red
                print("You typed letter " + Fore.GREEN + str(keypress) + Fore.WHITE)
                number_of_hits += 1
                number_of_types += 1
                inputs=inputs+["requested = "+str(topress), "recieved = "+str(keypress),"duration = "+str(finishinput_time-startinput_time)]# does a array like the teachers'
            else:
                print("You typed letter " + Fore.RED + str(keypress) + Fore.WHITE)
                number_of_types += 1
                inputs=inputs+["requested = "+str(topress), "recieved = "+str(keypress),"duration = "+str(finishinput_time-startinput_time)]# does a array like the teachers'

        
        else:
            print("Curernt test duration (" + str(time.time()-start_time) + " ) exceed maximum of " + str(mv) + ".")
            print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.WHITE)
        
        
            accuracy = number_of_hits / number_of_types
            test_end = datetime.datetime.now()
            test_end = test_end.strftime("%a %-d %b %-H:%M:%S %Y")
            test_end_time=time.time()
            test_time=test_end_time-test_start_time
            # test_time=test_end-test_start #tempo total do teste, pode ser menor q  utm
            average_type=test_time/number_of_types #tempo medio por tecla


            resultado={"accuracy":accuracy,
                "inputs":inputs,
                "number of hits": number_of_hits,
                "number of types":number_of_types,
                "test duration": test_time,
                "test start":test_start,
                "test end": test_end,
                "type average duration":average_type,
                "type hit average duration":test_time/number_of_hits,   
                "type miss average duration": test_time/(number_of_types-number_of_hits)}

            pp=pprint.PrettyPrinter(indent=1)
            pp.pprint(resultado)
                        

    
    else:
        print("Test running up to " + str(mv) + " inputs.")
        print('Press any key to start the test.')
        readkey()
        
        for i in range(mv):
            startinput_time= time.time() #see the start of each input line
           
            topress = random.choice(pool) #selects a key to press
            print('Type letter '+ Fore.LIGHTBLUE_EX + topress + Fore.WHITE)
            
            keypress = readkey()#reads pressed key
            finishinput_time=time.time() #sees the end of each input line

            if ord(keypress) == 32: #if space is pressed program stops
                break

            elif ord(keypress) == ord(topress): # if its correct shows the right one in green, if not, shows it in red
                print("You typed letter " + Fore.GREEN + str(keypress) + Fore.WHITE)
                number_of_hits += 1
                number_of_types += 1

                inputs=inputs+[("requested = "+str(topress), "recieved = "+str(keypress),"duration = "+str(finishinput_time-startinput_time))]
            
            
            
            else: #tecla errada
                print("You typed letter " + Fore.RED + str(keypress) + Fore.WHITE)
                number_of_types += 1
                print(inputs)
                inputs=inputs +(["requested = "+str(topress), "recieved = "+str(keypress),"duration = "+str(finishinput_time-startinput_time)])# does a array like the teachers' 
            

        print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.WHITE)
        
        
        accuracy = number_of_hits / number_of_types
        test_end = datetime.datetime.now()
        test_end = test_end.strftime("%a %-d %b %-H:%M:%S %Y")
        test_end_time=time.time()
        test_time=test_end_time-test_start_time
        # test_time=test_end-test_start #tempo total do teste, pode ser menor q  utm
        average_type=test_time/number_of_types #tempo medio por tecla


        resultado={"accuracy":accuracy,
            "inputs":inputs,
            "number of hits": number_of_hits,
            "number of types":number_of_types,
            "test duration": test_time,
            "test start":test_start,
            "test end": test_end,
            "type average duration":test_time/number_of_types,
            # "type hit average duration":test_time/number_of_hits,   #pode dar 0, a corrigir
            "type miss average duration": test_time/(number_of_types-number_of_hits)}

        pp=pprint.PrettyPrinter(indent=4)
        pp.pprint(resultado)

            






def main():
    # using argparse to create UI
    
    parser= argparse.ArgumentParser(description='Select time mode and duration of the test')

    #parser.add_argument("-utm", "--use_timed_mode", action= argparse.BooleanOptionalAction, default= False, help= "Using time mode will end the test with a duration equal to the value of -mv or --max_value")
    parser.add_argument("-utm", "--use_timed_mode", action= 'store_true', dest='utm', help= "Using time mode will end the test with a duration, in seconds, equal to the value of -mv or --max_value.")
    
    parser.add_argument("-mv ", "--max_value", type=int, dest='mv', help= "Defines max number of seconds for time mode or maximum number of inputs for number of inputs mode.")

    args = parser.parse_args()
    
    print(vars(args)) #prints selected arguments

    if args.mv or args.utm is None:
        typetest(args.mv,args.utm) #calls the test function
    else: 
        print("nao foram adicionados valores para valor maximo, por favor adicione valores")
        


if __name__ == '__main__':
    main()  