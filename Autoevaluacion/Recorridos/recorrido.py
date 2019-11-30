class Recorrido:
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__recorrido = []


    @property
    def segmentos_recorrido(self):
        return self.__recorrido

    def dar_longitud(self): # probado
        total = 0
        for obje in self.__recorrido:
            total += obje.longitud
        return total

    def dar_peajeTotal(self): # probado
        total = 0
        for obje in self.__recorrido:
            total += obje.peaje
        return total

    def dar_tiempo_minimo(self, transporte): # probado
        valor = self.dar_longitud() / transporte.velocidad
        return "{0:.2f}".format(valor)

    def dar_consumo(self,transporte): # probado
        return self.dar_longitud()* transporte.consumo


    def dar_costo(self,transporte,precio_combustible): # probado
        return self.dar_consumo(transporte) * precio_combustible + self.dar_peajeTotal()


    def agregar_segmento(self,segmento): # probado
        nro_recorridos = len(self.__recorrido)
        if nro_recorridos == 0: # Si no hay ningun segmento agregado en el recorrido lo agrega
            self.__recorrido.append(segmento)
        if nro_recorridos >= 1:# Si coincide el destino del ult. segmento agregado con el origen del nuevo segmento lo agrega, sino no.
            if self.__recorrido[nro_recorridos-1].destino == segmento.origen:
                self.__recorrido.append(segmento)
            else:
                print("Hay huecos en el recorrido")


    @staticmethod
    def dar_recorrido(self): # probado
        print('\n'+self.__nombre)
        for obje in range (len(self.__recorrido)):
            print(self.__recorrido[obje].origen +' - ' + self.__recorrido[obje].destino +'  -->  ' + str(self.__recorrido[obje].longitud) + 'Km.')


    def esta_completo(self): # probado
        lista = [] # agrega todos los lugares de origen y destino del recorrido a una lista

        for segmen in self.__recorrido:
            lista.append(segmen.origen)
            lista.append(segmen.destino)

        huecos= []
        for x in range(1,len(lista)-1,2): # itera el recorrido de dos en dos desde el 1er lugar de destino para compararlos
            if lista[x] == lista[x+1]:
                huecos.append(0)# Si son iguales agrega un 0 a la lista "huecos"
            else:
                huecos.append(1)# Si son distintos agrega un 1 a la lista "huecos"

        hay_huecos = "no"
        for nro in huecos: # itera la lista de "huecos" y se fija si hay un 1 en el contenido (significa que hay huecos)
            if nro == 1:
                hay_huecos = "si"
                break
            else:
                pass
        if hay_huecos == "no": # si NO hay huecos en el recorrido devuelve TRUE ya que el recorrido ESTA COMPLETO
            return True
        else: # De lo contrario devuelve FALSE
            return False


    # Busca el lugar dado x parametro en la lista del recorrido y si existe devuelve true, de lo contrario False
    def existe_lugar(self, buscarLugar): # probado
        existe = False
        for obje in range(len(self.__recorrido)):
            lugar_uno = self.__recorrido[obje].origen
            lugar_dos = self.__recorrido[obje].destino

            if lugar_uno == buscarLugar or lugar_dos == buscarLugar:
                existe = True
                break
        return existe
