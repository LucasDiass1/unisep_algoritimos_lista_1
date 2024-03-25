valor_hora = float(input("Insira o valor da hora de trabalho em reais: "))
horas_trabalhadas = float(input("Insira o número de horas trabalhadas no mês: "))
valor_total = valor_hora * horas_trabalhadas
valor_a_pagar = valor_total * 1.10
print("O valor a ser pago ao funcionário é R$ {:.2f}".format(valor_a_pagar))