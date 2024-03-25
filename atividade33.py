import math
altura_degrau = float(input("Insira a altura do degrau em metros: "))
altura_desejada = float(input("Insira a altura que deseja alcançar subindo a escada em metros: "))
degraus_necessarios = math.ceil(altura_desejada / altura_degrau)
print("O usuário precisará subir", degraus_necessarios, "degraus para atingir a altura desejada.")
