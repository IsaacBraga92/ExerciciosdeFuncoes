# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores
# para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O
# programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro
# valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o
# programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
# pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor
# da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(prestacao, diasAtrasados):
    if diasAtrasados > 0:
        valor_final = (((3 + diasAtrasados * 0.1) / 100) * prestacao) + prestacao
    else:
        valor_final = prestacao
    return valor_final


valor_total_das_prestacoes = 0
quantidade_prestacoes_pagas = 0
while True:
    valor = float(input("Digite o valor da prestação: "))
    if valor == 0:
        break
    atraso = int(input("Informe a quantidade de dias de atraso: "))
    quantidade_prestacoes_pagas += 1
    valorTotal = valorPagamento(valor, atraso)
    valor_total_das_prestacoes += round(valorTotal)
    print(f"O valor a ser pago é de R$: {round(valorTotal, 2)} reais")

print(f"A quantidade prestações pagas foi {quantidade_prestacoes_pagas}")
print(f"O valor total das prestações que foram pagas é de R$:{valor_total_das_prestacoes} reais")
