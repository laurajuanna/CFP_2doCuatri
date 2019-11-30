class Segmento:
    def __init__(self,origen,destino,precio,peaje,longitud):
        self.__origen = origen # str
        self.__destino = destino # str
        self.__precio = precio # float
        self.__peaje = peaje # float
        self.__longitud = longitud # float


    @property
    def origen(self):
        return self.__origen

    @property
    def destino(self):
        return self.__destino

    @property
    def precio(self):
        return self.__precio

    @property
    def peaje(self):
        return self.__peaje

    @property
    def longitud(self):
        return self.__longitud