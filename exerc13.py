# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função
# deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
# máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
# forma elegante.

def desenhar(linhas, colunas):
    if linhas > 20:
        linhas = 20
    if colunas > 20:
        colunas = 20
    print('-+-' * colunas)
    c = 0
    while c < linhas:
        z = '|'
        print(f'{z}{z:>{(colunas * 3 - 1)}}')
        c += 1
    print('-+-' * colunas)


linha = int(input("Informe a quantidade de linhas: "))
coluna = int(input("Informe a quantidade de colunas: "))

desenhar(linha, coluna)


