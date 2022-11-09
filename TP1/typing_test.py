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

def typeTest(mv, utm):
    pool = string.ascii_lowercase # Gets all lowercase letters of the alphabet
    user = getlogin() # Gets the user's username
    now = datetime.datetime.now() # Gets current date
    now = now.strftime("%B %Y") # Formats date to month and year
    number_of_hits = 0
    number_of_types = 0
    inputs = [] # Creates an array to store requested and pressed letters and hit time.
    types = namedtuple("Keypress", ["requested","received","duration"]) # Creates a named tuple to store requested and pressed letters and hit time

    print("\nTyping Test, "+ user + ", "+ now)

    test_start_date = datetime.datetime.now()
    test_start_date = test_start_date.strftime("%a %-d %b %-H:%M:%S %Y") # Stores test's start date and time

    if utm == True:
        print("Test running up to " + str(mv) + " seconds.")
        print('Press any key to start the test.')

        readkey()
        test_start_time = time.time() # Stores test's start time to count duration

        while time.time()-test_start_time < mv: # Runs loop while duration (mv) is not exceeded
            start_input_time = time.time() # Stores time at input request
            to_press = random.choice(pool) # selects a random letter to type

            print('Type letter '+ Fore.LIGHTBLUE_EX + to_press + Fore.WHITE)

            key_press = readkey()# Reads pressed key
            finishinput_time = time.time() - start_input_time # Stores time of input duration

            if ord(key_press) == 32: # If spacebar is pressed, the program stops
                break

            elif ord(key_press) == ord(to_press): # If the correct key is pressed, it will be shown in green
                print("You typed letter " + Fore.GREEN + str(key_press) + Fore.WHITE)

                number_of_hits += 1
                number_of_types += 1

                type_tuple = types(to_press,key_press,finishinput_time)
                inputs.append(type_tuple)

            else:
                print("You typed letter " + Fore.RED + str(key_press) + Fore.WHITE) # If the wrong key is pressed, it will be shown in red

                number_of_types += 1

                type_tuple = types(to_press,key_press,finishinput_time)
                inputs.append(type_tuple)

        stats(test_start_time, test_start_date, number_of_types, number_of_hits, inputs, utm, mv)

    else:
        print("Test running up to " + str(mv) + " inputs.")
        print('Press any key to start the test.')

        readkey()
        test_start_time = time.time()

        for i in range(mv):
            start_input_time = time.time()
            to_press = random.choice(pool)

            print('Type letter '+ Fore.LIGHTBLUE_EX + to_press + Fore.WHITE)

            key_press = readkey()
            finishinput_time = time.time() - start_input_time

            if ord(key_press) == 32:
                break

            elif ord(key_press) == ord(to_press):
                print("You typed letter " + Fore.GREEN + str(key_press) + Fore.WHITE)

                number_of_hits += 1
                number_of_types += 1

                type_tuple = types(to_press,key_press,finishinput_time)
                inputs.append(type_tuple)

            else:
                print("You typed letter " + Fore.RED + str(key_press) + Fore.WHITE)

                number_of_types += 1

                type_tuple = types(to_press,key_press,finishinput_time)
                inputs.append(type_tuple)

        stats(test_start_time, test_start_date, number_of_types, number_of_hits, inputs, utm, mv)

def stats(test_start_time, test_start_date, number_of_types, number_of_hits, inputs, utm, mv):
      
        test_end_time = time.time()
        test_duration = test_end_time - test_start_time
        print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.WHITE)

        if utm == True:
            print("Curernt test duration (" + str(test_duration) + " ) exceed maximum of " + str(mv) + ".")

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

        resultado = {"Accuracy" : accuracy,
                    "Number of hits" : number_of_hits,
                    "Number of types" : number_of_types,
                    "Test duration" : test_duration,
                    "Test start" : test_start_date,
                    "Test end" : test_end_date,
                    "Type average duration" : average_type,
                    "Type hit average duration" : average_hit,
                    "Type miss average duration" : average_miss,
                    "Types" : inputs}

        pprint(resultado)

def main():

    # using argparse to create UI
    parser= argparse.ArgumentParser(description='Select time mode and duration of the test')

    parser.add_argument("-utm", "--use_timed_mode", action= 'store_true', dest='utm', help= "Using time mode will end the test with a duration, in seconds, equal to the value of -mv or --max_value.")
    parser.add_argument("-mv ", "--max_value", type=int, dest='mv', help= "Defines max number of seconds for time mode or maximum number of inputs for number of inputs mode.")

    args = parser.parse_args()
    print(vars(args)) #prints selected arguments

    if args.mv != None:

        typeTest(args.mv,args.utm) #calls the test function

    else:

        print("A value for MV was not given")
        exit

if __name__ == '__main__':

    main()  
