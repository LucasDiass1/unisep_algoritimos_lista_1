custo_fabrica = float(input("Insira o custo de fábrica do carro: "))
porcentagem_distribuidor = 0.12  # 12%
porcentagem_impostos = 0.45  # 45%
custo_distribuidor = custo_fabrica * porcentagem_distribuidor
custo_impostos = custo_fabrica * porcentagem_impostos
custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos
print("O custo ao consumidor do carro é de R$", custo_consumidor)