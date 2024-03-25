nota_g1 = float(input("Por favor, insira a nota da G1: "))
nota_g2 = float(input("Por favor, insira a nota da G2: "))
media_ponderada = (nota_g1 + (nota_g2 * 2)) / 3
print("A média do semestre é:", media_ponderada)
if media_ponderada >= 7.0:
    print("Parabéns! Você foi aprovado.")
else:
    print("Infelizmente, você foi reprovado.")