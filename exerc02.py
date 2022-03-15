# Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def numeros_crescente(n: int):
    for i in range(1, n + 1):
        for m in range(1, i+1):
            print(m, end=' ')
        print()


n = int(input("Digite um número: "))
numeros_crescente(n)
