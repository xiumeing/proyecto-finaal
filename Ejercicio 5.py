nombre = ""
estatura = 0.0
peso =0.0


nombre = input("Digite su nombre: ")
estatura = float(input("Digite su estatura: "))
peso = float(input("Digite su peso: "))

imc= peso/estatura**2

print("Hola estimado" ,nombre + "su indice de masa corporal es " ,imc)