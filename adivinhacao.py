import random
from enum import Enum

class Dificuldade(Enum):
    FACIL = 10
    NORMAL = 50
    DIFICIL = 100

nivel_dificuldade = Dificuldade[input("Qual a dificuldade? \nFACIL \nMedio \nDIFICIL\n:").upper()].value

numero_aleatorio = random.randint(0, nivel_dificuldade)
tentativas = 5

chutes = []

while(tentativas != 0):

    chute = int(input('Digite seu chute:\n'))
    
    if chute not in chutes:    
        if chute == numero_aleatorio:
            print('\nParabéns você ganhou')
            tentativas = 0
        else:
            chutes.append(chute)
            tentativas -= 1
            print('\nVocê errou, mas ainda tem '+str(tentativas)+' Tentativas')
    else:
        print('Você já tentou esse numero. Tente com outro numero')