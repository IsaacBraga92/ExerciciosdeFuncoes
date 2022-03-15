# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(n1, n2, n3):
    resultado = n1+n2+n3
    return resultado


a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

print(soma(a,b,c))