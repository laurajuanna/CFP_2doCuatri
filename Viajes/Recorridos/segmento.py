from Transporte import transporte

class Segmento:
    def __init__(self,origen,destino,precio,peaje,largo):
        self.__origen = origen # str
        self.__destino = destino # str
        self.__precio = precio # float
        self.__peaje = peaje # float
        self.__largo = largo # float

    def dar_consumo(self): # float
        return transporte.Transporte.consumo * self.__largo

    @property
    def precio(self):
        return self.__precio + self.__peaje