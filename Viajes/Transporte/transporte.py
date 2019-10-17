from Pasajeros import pasajero

class Transporte:
    def __init__(self,patente,capacidad,consumo,vel_max):
        self.__patente = patente
        self.__capacidad = capacidad
        self.__pasajeros = []
        self.__consumo = consumo
        self.__vel_max = vel_max

    @property
    def consumo(self):
        return self.__consumo

    def agregar_pasajero(self,pax): #pasajero
        self.__pasajeros.append(pax)

    def dar_ingreso(self):
        pass

    def listar_pasajeros(self):
        pass

    def dar_consumo(self):
        pass

    def dar_costo(self):
        pass