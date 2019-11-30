class Pasajero:
    def __init__(self, dni, nombre, origen, destino,recorrido):
        self.__dni = dni
        self.__nombre = nombre
        self.__origen = origen
        self.__destino = destino
        self.__precio = self.dar_precio(origen,destino,recorrido)

    def __str__(self):
        return '{}      {}     {} - {}     ${}'.format(self.__dni, self.__nombre, self.__origen,self.__destino,self.__precio)


    @staticmethod
    def dar_precio(origen, destino, recorrido):
        precio_individual = 0
        sumar = 0
        origen_pasajero = origen
        destino_pasajero = destino
        for x in range (len(recorrido.segmentos_recorrido)):
            origen_segmento = recorrido.segmentos_recorrido[x].origen
            destino_segmento = recorrido.segmentos_recorrido[x].destino
            precio_segmento = recorrido.segmentos_recorrido[x].precio
            if origen_pasajero == origen_segmento:
                sumar = 1
            if sumar == 1:
                precio_individual += precio_segmento
            if destino_pasajero == destino_segmento:
                sumar = 0
        return precio_individual

    @property
    def precio(self):
        return self.__precio