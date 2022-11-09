#!/usr/bin/env python3

import argparse
from colorama import Fore
import datetime
from os import getlogin
import random
from readchar import readkey
import string
import time
from pprint import pprint
from collections import namedtuple

def typetest(mv, utm):
    pool = string.ascii_lowercase #gets all lowercase letters of the alphabet
    
    user = getlogin() # gets the user's username
    
    now = datetime.datetime.now() #gets current date
    now = now.strftime("%B %Y") #formats date to month and year
    number_of_hits = 0
    number_of_types = 0
    accuracy = 0
    inputs = [] #creates an array to store requested and pressed letters and hit time.
    types = namedtuple("Keypress", ["requested","received","duration"])
    
    print("\nTyping Test, "+ user + ", "+ now)

    test_start_date = datetime.datetime.now()
    test_start_date = test_start_date.strftime("%a %-d %b %-H:%M:%S %Y")

    if utm == True:
        print("Test running up to " + str(mv) + " seconds.")
        print('Press any key to start the test.')
        readkey()
        test_start_time = time.time() #stores the start time

        while time.time()-test_start_time < mv: #runs loop while duration (mv) is not exceeded

            startinput_time = time.time() #saves time at input request
            topress = random.choice(pool) #selects a key to press
            print('Type letter '+ Fore.LIGHTBLUE_EX + topress + Fore.WHITE)
            
            keypress = readkey()#reads pressed key
            finishinput_time = time.time() - startinput_time #saves time after input
            
            if ord(keypress) == 32: #if space is pressed program stops
                break
        
            elif ord(keypress) == ord(topress): # if its correct shows the right one in green, if not, shows it in red
                print("You typed letter " + Fore.GREEN + str(keypress) + Fore.WHITE)
                number_of_hits += 1
                number_of_types += 1
                typetuple = types(topress,keypress,finishinput_time)
                inputs.append(typetuple)

            else:
                print("You typed letter " + Fore.RED + str(keypress) + Fore.WHITE)
                number_of_types += 1
                typetuple = types(topress,keypress,finishinput_time)
                inputs.append(typetuple)
        
        test_end_time = time.time()
        test_duration = test_end_time - test_start_time
        print("Curernt test duration (" + str(test_duration) + " ) exceed maximum of " + str(mv) + ".")
        print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.WHITE)

        test_end_date = datetime.datetime.now()
        test_end_date = test_end_date.strftime("%a %-d %b %-H:%M:%S %Y")
            
        if number_of_types != 0 :
            average_type = test_duration / number_of_types
            accuracy = number_of_hits / number_of_types
        else:
            average_type = 0
            accuracy = 0
            
        if number_of_hits != 0 :
            average_hit = test_duration / number_of_hits
        else:
            average_hit = 0

        if number_of_types - number_of_hits > 0 :
            average_miss = test_duration / (number_of_types - number_of_hits)
        else:
            average_miss = 0

        resultado = {"accuracy" : accuracy,
                    "number of hits" : number_of_hits,
                    "number of types" : number_of_types,
                    "test duration" : test_duration,
                    "test start" : test_start_date,
                    "test end" : test_end_date,
                    "type average duration" : average_type,
                    "type hit average duration" : average_hit,
                    "type miss average duration" : average_miss,
                    "types" : inputs}
            
        pprint(resultado)
            
    
    else:
        print("Test running up to " + str(mv) + " inputs.")
        print('Press any key to start the test.')
        readkey()
        test_start_time = time.time() #stores the start time
        for i in range(mv):
        
            startinput_time = time.time() #saves time at input request
            topress = random.choice(pool) #selects a key to press
            print('Type letter '+ Fore.LIGHTBLUE_EX + topress + Fore.WHITE)
            
            keypress = readkey()#reads pressed key
            finishinput_time = time.time() - startinput_time #saves time after input
            
            if ord(keypress) == 32: #if space is pressed program stops
                break

            elif ord(keypress) == ord(topress): # if its correct shows the right one in green, if not, shows it in red
                print("You typed letter " + Fore.GREEN + str(keypress) + Fore.WHITE)
                number_of_hits += 1
                number_of_types += 1
                typetuple = types(topress,keypress,finishinput_time)
                inputs.append(typetuple)

            else:
                print("You typed letter " + Fore.RED + str(keypress) + Fore.WHITE)
                number_of_types += 1
                typetuple = types(topress,keypress,finishinput_time)
                inputs.append(typetuple)

        test_end_time = time.time()
        test_duration = test_end_time - test_start_time
        print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.WHITE)

        test_end_date = datetime.datetime.now()
        test_end_date = test_end_date.strftime("%a %-d %b %-H:%M:%S %Y")
        
        if number_of_types != 0 :
            average_type = test_duration / number_of_types
            accuracy = number_of_hits / number_of_types
        else:
            average_type = 0
            accuracy = 0
            
        if number_of_hits != 0 :
            average_hit = test_duration / number_of_hits
        else:
            average_hit = 0

        if number_of_types - number_of_hits > 0 :
            average_miss = test_duration / (number_of_types - number_of_hits)
        else:
            average_miss = 0

        resultado = {"accuracy" : accuracy,
                    "number of hits" : number_of_hits,
                    "number of types" : number_of_types,
                    "test duration" : test_duration,
                    "test start" : test_start_date,
                    "test end" : test_end_date,
                    "type average duration" : average_type,
                    "type hit average duration" : average_hit,
                    "type miss average duration" : average_miss,
                    "types" : inputs}
            
        pprint(resultado)

def main():
    # using argparse to create UI
    
    parser= argparse.ArgumentParser(description='Select time mode and duration of the test')

    #parser.add_argument("-utm", "--use_timed_mode", action= argparse.BooleanOptionalAction, default= False, help= "Using time mode will end the test with a duration equal to the value of -mv or --max_value")
    parser.add_argument("-utm", "--use_timed_mode", action= 'store_true', dest='utm', help= "Using time mode will end the test with a duration, in seconds, equal to the value of -mv or --max_value.")
    
    parser.add_argument("-mv ", "--max_value", type=int, dest='mv', help= "Defines max number of seconds for time mode or maximum number of inputs for number of inputs mode.")

    args = parser.parse_args()
    
    print(vars(args)) #prints selected arguments

    if args.mv != None:
        typetest(args.mv,args.utm) #calls the test function
    else:
        print("A value for MV was not given")
        exit

if __name__ == '__main__':
    main()  