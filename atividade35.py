numero = int(input("Insira um número inteiro de três dígitos (de 100 a 999): "))
if 100 <= numero <= 999:
    numero_invertido = int(str(numero)[::-1])
    print("O número gerado com os dígitos invertidos é:", numero_invertido)
else:
    print("O número não está no intervalo de três dígitos (de 100 a 999).")