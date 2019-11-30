class Transporte:
    def __init__(self,patente,capacidad,consumo,vel_max):
        self.__patente = patente
        self.__capacidad = capacidad
        self.__pasajeros = []
        self.__consumo = consumo
        self.__vel_max = vel_max

    @property
    def pasajeros(self):
        return self.__pasajeros

    @property
    def consumo(self):
        return self.__consumo

    @property
    def velocidad(self):
        return self.__vel_max

    def agregar_pasajero(self,pax): # probado
        capacidad = self.__capacidad
        ocupados = len(self.__pasajeros)
        if ocupados < capacidad:
            self.__pasajeros.append(pax)
        else:
            print("Vehiculo completo")

    def dar_ingreso(self): # probado
        total = 0
        for pax in self.__pasajeros:
            total += pax.precio
        return total

    @staticmethod
    def listar_pasajeros(self): # probado
        print('\nPatente: ' + self.__patente)
        for valor in range(len(self.__pasajeros)):
            print(self.__pasajeros[valor])


    def dar_porcentaje_ocupacion(self): # probado
        print('\nAsientos ocupados: ' + str(len(self.__pasajeros)) + '\nAsientos libres: ' + str(self.__capacidad - len(self.__pasajeros)))