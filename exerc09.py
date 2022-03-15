# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverter(n):
    x = n[::-1]
    return x

i = (input("Digite um número: "))
print(inverter(i))