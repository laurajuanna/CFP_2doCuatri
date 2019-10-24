class Transporte:
    def __init__(self,patente,capacidad,consumo,vel_max):
        self.__patente = patente
        self.__capacidad = capacidad
        self.__pasajeros = []
        self.__consumo = consumo
        self.__vel_max = vel_max

    @property # ESTO ES PARA SACAR EL PRECIO EN EL ARCHIVO PASAJERO.PY
    def pasa(self):
        return self.__pasajeros

    @property
    def consumo(self):
        return self.__consumo

    @property
    def velocidad(self):
        return self.__vel_max

    def agregar_pasajero(self,pax): #pasajero
        self.__pasajeros.append(pax)

    def dar_ingreso(self):
        pass

    @staticmethod
    def listar_pasajeros(self):
        print('\nPatente: ' + self.__patente)
        for valor in range(len(self.__pasajeros)):
            print(self.__pasajeros[valor])
        print('\nAsientos ocupados: '+str(len(self.__pasajeros))+'\nAsientos libres: '+str(self.__capacidad - len(self.__pasajeros)))

    def dar_consumo(self):
        pass

    def dar_costo(self):
        pass
