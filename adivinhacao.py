import random

numero_aleatorio = random.randint(0, 50)
controle = True

while(controle == True):

    chute = int(input('Digite seu chute:\n'))

    if chute == numero_aleatorio:
        print('\nParabéns você ganhou')
        controle = False
    else:
        print('\nVocê errou, tente novamente')