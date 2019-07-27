import random

numero_aleatorio = random.randint(0, 50)
tentativas = 5

while(tentativas != 0):

    chute = int(input('Digite seu chute:\n'))

    if chute == numero_aleatorio:
        print('\nParabéns você ganhou')
        tentativas = 0
    else:
        tentativas -= 1
        print('\nVocê errou, mas ainda tem '+str(tentativas)+' Tentativas')
        