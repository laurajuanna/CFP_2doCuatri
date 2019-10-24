class Segmento:
    def __init__(self,origen,destino,precio,peaje,largo):
        self.__origen = origen # str
        self.__destino = destino # str
        self.__precio = precio # float
        self.__peaje = peaje # float
        self.__largo = largo # float

    def __str__(self):
        return '{} - {} - $ {} - Peaje $ {} - {} Km.'.format(self.__origen, self.__destino, self.__precio, self.__peaje, self.__largo)

    def dar_consumo(self,transporte): # float
        return transporte.consumo * self.__largo

    @property
    def precio(self):
        return self.__precio + self.__peaje

    @property
    def largo(self):
        return self.__largo
