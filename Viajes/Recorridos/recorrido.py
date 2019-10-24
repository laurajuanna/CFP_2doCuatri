class Recorrido:
    def __init__(self,nombre):
        self.__recorrido = [] #segmento
        self.__nombre = nombre

    def dar_longitud(self):
        pass

    def dar_tiempo(self,transporte):
        pass

    def dar_consumo(self,transporte):
        pass

    def dar_costo(self,transporte,precio_combustible):
        pass

    def agregar_segmento(self,segmento):
        self.__recorrido.append(segmento)

    @staticmethod
    def dar_recorrido(self):
        for obje in range (len(self.__recorrido)):
            print(self.__recorrido[obje])
