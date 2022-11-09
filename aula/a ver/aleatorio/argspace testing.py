#!/usr/bin/env python3
import argparse

from cv2 import perspectiveTransform



# # sends the square of the interger that is put in front of prog.py : 
# # ./prog.py 4 = 16 
# parser= argparse.ArgumentParser()
# parser.add_argument("square", help="echo the string you use here",
#         type=int)
# args= parser.parse_args()
# print(args.square**2)


parser= argparse.ArgumentParser()

# argumento para os quadrado do int
parser.add_argument("square",type=int
    , help="echo the string you use here")
#argumento para o verbose, para o if a seguir( restringe-se as...
#  escolhas para poder ter apenas os 3 tipos de resposta diferentes)
parser.add_argument("-v", "--verbose" ,type=int, choices=[0,1,2]
    , help="helps increase output verbosity")
args= parser.parse_args()
answer= args.square**2 #calculo do quadrado

if args.verbose==2: 
    #se existirem 2 argumentos ( valor -v 2(ou 1))
    # irá sair expressao competa( dependendo do int que aparecer)
    print(f"the square of {args.square} equals {answer}")
elif args.verbose==1:
    print (f'{args.square}^2 equals {answer}')
else:
    #senao existirem 2 argumentos só manda o valor
    print(answer)





parser= argparse.ArgumentParser()

# argumento para os quadrado do int
parser.add_argument("square",type=int
    , help="echo the string you use here")
#argumento para o verbose, para o if a seguir( restringe-se as...
#  escolhas para poder ter apenas os 3 tipos de resposta diferentes, ao contar o numero de v no arg)
parser.add_argument("-v", "--verbose" ,action='count', default=0
    , help="helps increase output verbosity")
args= parser.parse_args()
answer= args.square**2 #calculo do quadrado

if args.verbose>=2: # faz com que -vvvv seja lido
    #se existirem 2 argumentos ( valor -v 2(ou 1))
    # irá sair expressao competa( dependendo do int que aparecer)
    print(f"the square of {args.square} equals {answer}")
elif args.verbose>=1:
    print (f'{args.square}^2 equals {answer}')
else:
    #senao existirem 2 argumentos só manda o valor
    print(answer)





parser= argparse.ArgumentParser()

# argumento para os quadrado do int
parser.add_argument("x",type=int
    , help="a base")
#argumento para o verbose, para o if a seguir( restringe-se as...
#  escolhas para poder ter apenas os 3 tipos de resposta diferentes, ao contar o numero de v no arg)
parser.add_argument("y",type=int
    , help="o expoente")
#argumento para o verbose, para o if a seguir( restringe-se as...
#  escolhas para poder ter apenas os 3 tipos de resposta diferentes, ao contar o numero de v no 

parser.add_argument("-v", "--verbose" ,action='store_true'
    ,help='sends extra information')
parser.add_argument("-q",'--quiet',action='store_true'
    ,help=" sends only result")
args= parser.parse_args()
answer= args.x**args.y #calculo do quadrado (preciso por .args para saber o que é)

if args.quiet: # ver com o argumento-quiet
    print(f"{answer}")
elif args.verbose:
    print("{} to the power of {} equals {}".format(args.x, args.y, answer))
else:
    #senao existirem 2 argumentos só manda o valor
    print('{}^{}== {}'.format(args.x, args.y, answer))



