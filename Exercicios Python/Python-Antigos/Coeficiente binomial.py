n=5
k=3
def fatorial(n):
    fat=1
    while(n>1):
        fat=fat*n
        n=n-1
    return fat
print(fatorial(n))

def numero_binominal(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))
print(numero_binominal(n,k))


def menu( ):
    return'''   1-converter anos em meses
                2- conveter meses em dias
                3- converter dias em horas 
                4-converter anos ,meses e dias em horas'''