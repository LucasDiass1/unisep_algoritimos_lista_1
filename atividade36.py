numero = int(input("Insira um número inteiro de quatro dígitos (de 1000 a 9999): "))
if 1000 <= numero <= 9999:
    numero_str = str(numero)
    for digito in numero_str:
        print(digito)
else:
    print("O número não está no intervalo de quatro dígitos (de 1000 a 9999).")