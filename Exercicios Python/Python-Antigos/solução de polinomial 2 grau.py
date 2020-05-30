from sympy import symbol,solve
def calcula_f(x):
    return x**2 -4*x+3

#definir x como uma variavel

x=symbol('x')

# resolver equação calcula_f=0

resultado=solve(y)

print 'x=',resultado

########################################################

# equação do segundo grau (raizes não reais)

from symp import symbol,solve

def calcula_f(x):
    return x**2+x+1
#definir  x como uma variavel
x=symbol('x')

#resolve equação calcula_f=0
y=calcula_f(x)
#######resultado da equação calcula_f(x)=0


