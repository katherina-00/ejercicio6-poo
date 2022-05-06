import sys
from menu import muestraMenu
from ManejadorViajero import ManejadorViajeros

if __name__ == "__main__":

    v = ManejadorViajeros()
    v.CrearViajero()
    print('Viajeros: \n')
    print(v)

    while True:
        op = muestraMenu()
        if op == '1':
            v.mayorMillas()
        elif op == '2':
            v.acumulaMillas()
        elif op == '3':
            v.canjearMillas()
        elif op == '4':
            sys.exit(0)
