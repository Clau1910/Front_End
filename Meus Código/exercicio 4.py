def recomendar_sala(numero_participantes, tipo_reuniao):
    if tipo_reuniao == "executiva":
        return "Sala Grande"
    elif tipo_reuniao == "normal":
        if numero_participantes <= 5:
            return "Sala Pequena"
        elif numero_participantes <= 15:
            return "Sala Média"
        else:
            return "Sala Grande"
    else:
        return "Tipo de reunião inválido"

numero_participantes = int(input("Número de participantes: "))
tipo_reuniao = input("Tipo de reunião (normal ou executiva): ").strip().lower()

print("Recomendação:", recomendar_sala(numero_participantes, tipo_reuniao))