N=1000
marca=[' ']*N
modelo=[' ']*N
preco=[0]*N
disponibilidade=[0]*N
cont=0

op=10
while (op!=0):

    op = int(input('''
        Digite uma opção:
    1- Cadastrar Veículos
    2- Listar Veiculos
    3- Listar Veiculos Alugados 
    4- Listar Carros Disponivel
    5-Listar Carros Populares
    6-Alugar
    7-Disponibilizar veiculos 
    0-Sair'''))

    if(op==1):
        marca=[cont]=input('Diga a marca do Veìculo:')
        modelo[cont]= input('Diga o modelo do Veiculo:')
        preco[cont]=float(input('Informe o preço do aluguel:'))
        disponibilidade[cont]=1
        cont=cont+1


    if(op==2):
        for k in range (cont):
        print('Codigo:', k)
        print('Marca do Veiculo',marca[k])
        print('O Modelo do Veiculo:',modelo[k])
        print('O preço do veículo é',preco[k])
        print('disponivibilidade:',disponibilidade[k])

    elif(op==3):
        for k in range (cont):
            if(disponibilidade[k]==0):
        print('Codigo:', k)
        print('Marca do Veiculo', marca[k])
        print('O Modelo do Veiculo:', modelo[k])
        print('O preço do veículo é', preco[k])
        print('disponibilidade:', disponibilidade[k])

    elif(op==4):
        for k in range(cont):
            if (disponibilidade[k] ==1):
        print('Codigo:', k)
        print('Marca do Veiculo', marca[k])/
        print('O Modelo do Veiculo:', modelo[k])
        print('O preço do veículo é', preco[k])
        print('disponibilidade:', disponibilidade[k])


    elif(op==5):
        for k in range (cont):
            if preco[k]<100:
        print('Codigo:', k)
        print('Marca do Veiculo', marca[k])
        print('O Modelo do Veiculo:', modelo[k])
        print('O preço do veículo é', preco[k])
        print('disponibilidade:', disponibilidade[k])


    elif(op==6):
        cod=int(input('Informe o codigo do veículo:'))
        disponibilidade[codigo]=0:

    elif(op==7):
        cod=int(input('Informe o codigo do veículo:'))
        disponibilidade[codigo]=1:


    elif(op==0):
        print('Finalizando.....')
    else:
        print('Opção invalida, Tente Novamente')
    print('=_=' * 10)
    print('Fim do Programa. Volte Sempre')









