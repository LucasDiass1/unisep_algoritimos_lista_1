hora_inicio = int(input("Insira a hora de início (0-23): "))
minuto_inicio = int(input("Insira o minuto de início (0-59): "))
segundo_inicio = int(input("Insira o segundo de início (0-59): "))
duracao_segundos = int(input("Insira a duração em segundos da experiência: "))
total_segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
total_segundos_termino = total_segundos_inicio + duracao_segundos
hora_termino = (total_segundos_termino // 3600) % 24
minuto_termino = (total_segundos_termino % 3600) // 60
segundo_termino = total_segundos_termino % 60
print("Horário de término da experiência: {:02d}:{:02d}:{:02d}".format(hora_termino, minuto_termino, segundo_termino))