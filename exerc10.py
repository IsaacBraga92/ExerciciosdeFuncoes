# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
# entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
# primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
# este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,
# no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random


def craps():
    return random.randint(2, 12)


print("CRAPS!!!")
while True:
    c = input("Jogar dados? s/n").lower()
    if c == 'n':
        print("Foi um bom jogo!")
        break
    valor_dados = craps()
    if valor_dados == 7 or valor_dados == 11:
        print(f"{valor_dados} - Você ganhou!!!")
    elif valor_dados == 2 or valor_dados == 3 or valor_dados == 12:
        print(f"{valor_dados} - Você perdeu!!!")
    elif valor_dados == 4 or valor_dados == 5 or valor_dados == 6 or valor_dados == 8 or valor_dados == 9 or valor_dados == 10:
        print(f"Este é o seu ponto: {valor_dados}")
        ponto = valor_dados
        while True:
            valor_dados = craps()
            if valor_dados == ponto:
                print(f"{valor_dados} - Você ganhou!!!")
                break
            elif valor_dados == 7:
                print(f"{valor_dados} - Você perdeu!!!")
                break
            else:
                print(f"Valor {valor_dados} diferente de {ponto} ou de 7.")
