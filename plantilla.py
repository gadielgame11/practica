from menu import mostrar_menu
from tmb import calcular_tmb
from imc import calcular_imc

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
