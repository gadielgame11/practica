print("=== CALCULADORA DE METABOLISMO ===")

sexo = input("Sexo (H/M): ").strip().upper()
edad = int(input("Edad (años): "))
peso = float(input("Peso (kg): "))
altura = float(input("Altura (cm): "))

# Calcular TMB (Mifflin-St Jeor)
if sexo == "H":
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
else:
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

print("\nNivel de actividad física:")
print("1. Sedentario")
print("2. Ligero (1-3 días/semana)")
print("3. Moderado (3-5 días/semana)")
print("4. Intenso (6-7 días)")
print("5. Muy intenso")

opcion = int(input("Elige opción (1-5): "))

factores = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

factor = factores.get(opcion, 1.2)

get = tmb * factor

print("\n===== RESULTADOS =====")
print(f"Tasa Metabólica Basal (TMB): {tmb:.2f} calorías/día")
print(f"Gasto Energético Total (GET): {get:.2f} calorías/día")

# Opcional: metas
print("\n--- Calorías según objetivo ---")
print(f"Para bajar peso: {get - 500:.2f} kcal/día")
print(f"Para subir masa: {get + 300:.2f} kcal/día")
