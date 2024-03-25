investimento_amigo1 = float(input("Informe o valor investido pelo primeiro amigo: "))
investimento_amigo2 = float(input("Informe o valor investido pelo segundo amigo: "))
investimento_amigo3 = float(input("Informe o valor investido pelo terceiro amigo: "))
valor_premio = float(input("Informe o valor total do prêmio: "))
total_investido = investimento_amigo1 + investimento_amigo2 + investimento_amigo3
ganho_amigo1 = (investimento_amigo1 / total_investido) * valor_premio
ganho_amigo2 = (investimento_amigo2 / total_investido) * valor_premio
ganho_amigo3 = (investimento_amigo3 / total_investido) * valor_premio
print("O primeiro amigo ganharia R$", ganho_amigo1)
print("O segundo amigo ganharia R$", ganho_amigo2)
print("O terceiro amigo ganharia R$", ganho_amigo3)