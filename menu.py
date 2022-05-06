def muestraMenu():
    __op = 0
    while True:
        print("----------Eliga una opcion----------\n")
        print("1. Viajeros con mayor cantidad de millas\n")
        print("2. Acumular millas\n")
        print("3. Canjear millas\n")
        print("4. Salir")
        __op = input("Ingrese su opcion: ")
        if __op in ("1", "2", "3", "4"):
            return __op
        input("No se ha ingresado ninguna opcion correcta.\n""Pulsa ENTER para continuar\n")
