
def menu( ):
    return'''   1-Inverter o valor
                2- Informar a metade
                3- Descobrir a área do quadrado
                4-Descobrir a área do retangulo
                5-descobrir a área do circulo 
                6-Sair'''

op=10
while(op!=0):
    print(menu( ))
    op=int(input('Informe uma opção:'))

    if(op==1):
        def inverter(n):
            return n * -1
        n=int(input('Informe o valor:'))
        print(inverter(n))

    if(op==2):
        def metade(n):
            return n / 2
        n=int(input('Informe o valor:'))
        print(metade(n))

    if(op==3):
        def areadoquadrado(n):
            return n ** 2
        n = int(input('Informe o valor:'))
        print(areadoquadrado(n))

    if(op==4):
        def areadoretangulo(n, m):
            return n * m
        n=int(input('Informe o valor:'))
        m=int(input('Informe outro valor:'))
        print(areadoretangulo(n,m))

    if(op==5):
        def areacirculo(r):
            return 3,14*r**2
        r=int(input('Informe o valor:'))
        print(areacirculo(r))

    else:
        print('Opção invalida, Tente Novamente')
    print('=_=' * 10)
    print('Fim do Programa. Volte Sempre')
