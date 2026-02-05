from menu import mostrar_menu
from tmb import calcular_tmb
from imc import calcular_imc

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
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

