matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input('Digite um valor [{l}, {C}]: '))
for l in range(0,3):
    for c in range (0,3):
        print(f'{matriz[l][c]}]',end=' ')
    print( )