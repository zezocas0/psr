#!/usr/bin/env python3

# usado para def keypress-------------- 
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
import time
import string
import random

import argparse
from colorama import Fore
from datetime import datetime

class outputlibrary():
    def __init__(self,inputs,hits,types,duration,start,end,avrtime,avrhit,avrmiss):
        
        self.inputs=inputs
        self.hits=hits
        self.types=types
        self.duration=duration
        self.start=start
        self.end=end
        self.avrtime=avrtime
        self.avrhit=avrhit
        self.avrmiss=avrmiss
    def tuplelist(self): # nao sei se isto está no citio certo. ainda não precebi bem isto
        
            #usar os valores do input para saber os valores pedidos
            accuracy=self.hits/self.types
            self.hits= #se o requested input(0,:) é igual ao recieved(1,:)
            self.types= len(self.inputs)#tamanho da lista
            self.duration=  #valor dado no inicio  usando "-utm"
            self.start=datetime.utcnow()  #tempo de inicio do progama no pc
            self.end=self.start+self.duration #tempo do fim do  programa; não é assim que se deve fazer
            self.avrtime=self.duration/self.hits  #tempo médio por cada input
            self.avrmiss= self.avrtime*self.hits #tempo médio *numero de vezes que foi clicado a letra certa
            
            self.avrmiss=self.avrtime*(self.types-self.hits) # tempo medio * (numero de escritas-numero de escritas certas)
            lista={"accuracy":accuracy,
            "inputs":self.hits,
            "number of hits":self.hits,
            "number of types":self.types,
            "test duration": self.duration,
            "test start":self.start,
            "type average duration":self.avrtime,
            "type hit average duration":self.avrhit,
            "type miss average duration": self.avrmiss}
            return lista
        

def keypress(max_value):
    pool=string.ascii_lowercase #uma pool com o alfabeto para o resultado 
    whatever=input("\n Iremos mostrar "+str(max_value)+ " numeros"+"\n pressione uma tecla para começar o desafio")
    
    for i in range(int(max_value)):
        
            topress=random.choice(pool) #key to press, randomized every time
            keypress=input('press the key: '+topress+"  ")#reads keypress
            
            if ord(keypress)==ord(topress): # if its correct shows the right one, if not, shows it in red
                print(" you pressed "+ keypress)
                
            else:
                print("you pressed the key "+Fore.RED+str(keypress)+Fore.WHITE+"!")
                
 










def main():
    # usar argparse para fazer o ui para o user interagir
    parser= argparse.ArgumentParser()

    parser.add_argument( "-utm" ,"--use_time_mode",type=int
        , help=Fore.WHITE+"max number of secondss for"+" time mode"+" or maximum number of imputs "+"for "+"number of inputs mode")
    parser.add_argument("-mv ","--max_value", type=int
        ,help="max number of seconds for " +"time mode"+" or maximum number of imputs "+"for "+"number of inputs mode")

    args= parser.parse_args()
    timeargs=args.use_time_mode


    if args.max_value or args.use_time_mode is None:
        print("nao foram adicionados valores para valor maximo")
    else: 
        keypress(args.max_value)
        P1=outputlibrary()

            



if __name__ == '__main__':
    main()  