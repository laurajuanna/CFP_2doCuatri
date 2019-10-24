class Recorrido:
    def __init__(self,nombre):
        self.__recorrido = [] #segmento
        self.__nombre = nombre

    def dar_longitud(self):
        total = 0
        for obje in self.__recorrido:
            total += obje.largo
        return total

    def dar_tiempo_minimo(self, transporte):
        valor = self.dar_longitud() / transporte.velocidad
        return "{0:.2f}".format(valor)

    def dar_consumo(self,transporte):
        return self.dar_longitud()* transporte.consumo

    def dar_costo(self,transporte,precio_combustible):
        pass

    def agregar_segmento(self,segmento):
        self.__recorrido.append(segmento)

    @staticmethod
    def dar_recorrido(self):
        print(self.__nombre)
        for obje in range (len(self.__recorrido)):
            print(self.__recorrido[obje])
