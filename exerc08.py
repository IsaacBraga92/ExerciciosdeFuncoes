# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def tamanho(n):
    t = str(abs(int(n)))
    return len(t)

i = int(input("Digite um número: "))
print(tamanho(i))

