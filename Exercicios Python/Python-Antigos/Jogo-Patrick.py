from random import randint
computador=randint(0,10)
print('Sou o Computador, acabei  de pensar em número de 0 e 10.')
print('Consegue advinhar qual foi ?')
acertou=False
palpite=0
while not acertou:
    player=int(input('Qual é o número:'))
    palpite=palpite+1
    if player==computador:
        acertou=True
    else:
        if player<computador:
            print('Tá quente... Tente novamente')
        elif player>computador:
            print('Tá Frio. Tente novamente')
print('Acertou com {} Tentativas. GAME OVER!.'.format(palpite))


