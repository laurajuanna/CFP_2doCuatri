from Recorridos import segmento

class Pasajero:
    def __init__(self, dni, nombre, origen, destino):
        self.__dni = dni
        self.__nombre = nombre
        self.__origen = origen
        self.__destino = destino

    def dar_precio(self):
        return segmento.Segmento.precio