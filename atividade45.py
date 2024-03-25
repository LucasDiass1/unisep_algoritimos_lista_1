nome_aluno = input("Digite o nome do aluno: ")
nota_prova = float(input("Digite a nota da prova (de 0 a 10): "))
nota_qualitativa = float(input("Digite a nota qualitativa (de 0 a 10): "))
media = (nota_prova * 2 + nota_qualitativa * 1) / 3
print("A média do aluno", nome_aluno, "na disciplina de Estrutura de Dados é:", media)