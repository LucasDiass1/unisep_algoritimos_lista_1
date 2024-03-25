salario_base = float(input("Insira o salário-base do funcionário: "))
gratificacao = 0.05 * salario_base
imposto = 0.07 * salario_base
salario_a_receber = salario_base + gratificacao - imposto
print("O salário a receber é R$ {:.2f}".format(salario_a_receber))