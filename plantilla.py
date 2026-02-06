# PRINCIPIO - INDICE GRASA CORPORAL

def calcular_igc():
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

# FIN - INDICE GRASA CORPORAL


from menu import mostrar_menu
from tmb import calcular_tmb
from iGc import calcular_imc 

def calcular_IMC(peso, altura):
    return peso / (altura * altura)


def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    imc = calcular_IMC(peso, altura)
    return (1.2 * imc) + (0.23 * edad) - (10.8 * valor_genero) - 5.4


def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    altura_cm = altura * 100
    return (10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_imc()
        elif opcion == "2":
            calcular_tmb()
        elif opcion == "3":
            calcular_igc()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

