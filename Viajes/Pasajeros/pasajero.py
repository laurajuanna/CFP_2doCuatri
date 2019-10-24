class Pasajero:
    def __init__(self, dni, nombre, origen, destino):
        self.__dni = dni
        self.__nombre = nombre
        self.__origen = origen
        self.__destino = destino

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.__dni, self.__nombre, self.__origen,self.__destino)

    @staticmethod # ESTO ES PARA SACAR EL PRECIO DE CADA PASAJERO. TODAVIA NO ENTIENDO LA LOGICA
    def dar_precio(transporte):
        for pasajero in transporte.pasa:
            origen = pasajero.__origen
            destino = pasajero.__destino
            print(origen,destino)
