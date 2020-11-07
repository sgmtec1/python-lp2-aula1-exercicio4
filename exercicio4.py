'''Escreva uma função que recebe como parâmetro de entrada um número N positivo, e retorna o
fatorial de N.
'''

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i               # fat *= i
        print (i)
    return fat


n = int(input('Informe um numero inteiro positivo: '))
f = fatorial(n)
print("O fatorial de {} é {}".format(n, f))

