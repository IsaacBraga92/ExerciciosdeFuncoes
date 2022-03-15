# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def imposto(taxa, custo):
    return (1 + taxa / 100) * custo


taxaImposto = float(input("Digite a taxa de imposto: "))
valor = float(input("Digite o valor do item: "))

print(round(imposto(taxaImposto,valor),2))
