def calcular_promedio_estudiante():
    num_examenes = int(input("Ingrese la cantidad de exámenes realizados: "))
    for i in range(num_examenes):
        nota = int(input(f"Ingrese la nota del examen {i+1}: "))
        notas.append(nota)

    nota_final = sum(notas) / num_examenes

    if nota_final >= 70:
        resultado = "Aprobó"
    elif 60 <= nota_final < 70:
        resultado = "Va a ampliación"
    else:
        resultado = "Reprobó"

    print(f"Nota final: {nota_final}")
    print(resultado)

calcular_promedio_estudiante()
