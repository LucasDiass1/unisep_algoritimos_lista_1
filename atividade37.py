segundos = int(input("Insira um valor inteiro em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)