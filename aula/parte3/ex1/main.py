#!/usr/bin/env python3
from time import time,ctime
import colorama
timenow=ctime()

def main():

    print('this is'+colorama.Fore.RED+' EX1 ' +colorama.Fore.WHITE+' and today is '+ str(timenow))
    
if __name__ == '__main__':
    main()