class Recorrido:
    def __init__(self,nombre):
        self.__recorrido = [] #segmento
        self.__nombre = nombre

    def __str__(self):
        return self.__recorrido

    def dar_largo(self):
        pass

    def dar_tiempo(self,transporte):
        pass

    def dar_consumo(self,transporte):
        pass

    def dar_costo(self,transporte,precio_combustible):
        pass

    def agregar_segmento(self,segmento):
        self.__recorrido.append(segmento)
        print(self.__recorrido)

    @staticmethod
    def dar_recorrido(self):
        return self.__recorrido