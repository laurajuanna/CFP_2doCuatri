from Recorridos import segmento

class Pasajero:
    def __init__(self, dni, nombre, origen, destino):
        self.__dni = dni
        self.__nombre = nombre
        self.__origen = origen
        self.__destino = destino

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.__dni, self.__nombre, self.__origen,self.__destino)

    def dar_precio(self):
        return segmento.Segmento.precio
