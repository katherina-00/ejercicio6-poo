import csv
from ViajeroFrecuente import ViajeroFrecuente
class ManejadorViajeros:
    def __init__(self):
        self.__ListaViajeros=[]
    def __str__(self):
        s = ""
        for viajeros in self.__ListaViajeros:
            s += str(viajeros) + '\n'
        return s

    def agregarViajero(self,unViajero):
        self.__ListaViajeros.append(unViajero)

    def CrearViajero(self):
        with open("viajeros.csv","r") as file:
                reader=csv.reader(file,delimiter=",")
                for fila in reader:
                    numViajero = int(fila[0])
                    dni = int(fila[1])
                    nombre = fila[2]
                    apellido = fila[3]
                    millas_acum = int(fila[4])
                    unViajero = ViajeroFrecuente(numViajero,dni,nombre,apellido,millas_acum)
                    self.agregarViajero(unViajero)

    def mayorMillas(self):
        max=None
        for num, ViajeroFrecuente in enumerate (self.__ListaViajeros):
            if (max is None or ViajeroFrecuente > max):
                max = ViajeroFrecuente.getMillas()
        for num, ViajeroFrecuente in enumerate (self.__ListaViajeros):
            if (ViajeroFrecuente.getMillas() == max):
                print("El/los viajeros que tienen la mayor cantidad de millas es/son: {} {} y su total de millas es: {}".format(ViajeroFrecuente.getNombre(),ViajeroFrecuente.getApellido(),ViajeroFrecuente.getMillas()))

    def acumulaMillas(self):
        v=int(input("Indique el numero de viajero al que desea acumular millas: "))
        b=int(input("Indique la cantidad de millas que desea acumular: "))
        for i, ViajeroFrecuente in enumerate (self.__ListaViajeros):
            if i == v-1:
                objeto = ViajeroFrecuente + b
                print("La cantidad de millas es: {} ".format(objeto.getMillas())

    def canjearMillas(self):
        v=int(input("Indique el numero de viajero al que desea canjear millas: "))
        b=int(input("Ingrese la cantidad de millas a canjear: "))
        for i, ViajeroFrecuente in enumerate (self.__ListaViajeros):
            if i == v-1:
                if b<=ViajeroFrecuente.getMillas():
                    objeto = ViajeroFrecuente - b
                    print("La cantidad de millas restantes son: {}".format(objeto.getMillas())
                else: print("La cantidad de millas a canjear excede la cantidad existente")
