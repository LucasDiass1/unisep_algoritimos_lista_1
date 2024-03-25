nome_vendedor = input("Informe o nome do vendedor: ")
num_carros_vendidos = int(input("Informe o número de carros vendidos: "))
valor_total_vendas = float(input("Informe o valor total das vendas: "))
salario_fixo = 500.00
comissao_por_carro = 50.00
porcentagem_comissao_vendas = 0.05
comissao_vendas = valor_total_vendas * porcentagem_comissao_vendas
salario_total = salario_fixo + (num_carros_vendidos * comissao_por_carro) + comissao_vendas
print("O salário total de", nome_vendedor, "é R$", salario_total)