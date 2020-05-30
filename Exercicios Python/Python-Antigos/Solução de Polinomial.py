from sympy import symbol,solve

def calc_f(x):
    return 2*x+1
# define x como variavel
x=symbol('x')

# resolva a equação calcula_f=0

y=calc_f(x)

resultado=solver(y)

print '\n'
print 'Resultado da equação 2*x+1=0'
print 'x=',resultado