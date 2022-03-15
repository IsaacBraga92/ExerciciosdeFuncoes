# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def mes_por_extenso(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_extenso = ''
    i = 0
    while mes - 1 != i:
        i += 1
        if mes - 1 == i:
            mes_extenso = meses[i]
            break
    return f"{dia} de {mes_extenso} de {ano}"


data = mes_por_extenso(5, 12, 1992)
print(data)
