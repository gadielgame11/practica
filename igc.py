#PRINCIPIO - INDICE GRASA CORPORAL

edad = int(input("Ingrese su edad: "))
imc = float(input("Ingrese su IMC: "))

genero = int(input("¿Cuál es tu género?\n1. Femenino\n2. Masculino\n"))

# Condición del género
if genero == 2:
    valor_genero = 10.8
else:
    valor_genero = 0

# Fórmula
igc = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

# Resultado
print(f"El porcentaje de grasa corporal es: {igc}%")

#FIN -INDICE GRASA CORPORAL