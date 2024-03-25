valor_diaria = 30.00
dias_trabalhados = int(input("Por favor, insira o número de dias trabalhados pelo encanador: "))
valor_bruto = dias_trabalhados * valor_diaria
previdencia_social = 0.11 * valor_bruto
imposto_renda = 0.08 * valor_bruto
valor_liquido = valor_bruto - previdencia_social - imposto_renda
print("A quantia líquida a ser paga ao encanador é R$ {:.2f}".format(valor_liquido))