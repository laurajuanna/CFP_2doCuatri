class Item:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.setPrecio(precio)

    def getCodigo(self):
        return self.__codigo

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio):
        if isinstance(precio, float)  \
                or isinstance(precio, int):
            self.__precio = precio
        else:
            raise TypeError

    def getNombre(self):
        return self.__nombre

class Carrito:
    def __init__(self):
        self.items = []        

    def agregar(self, item):
        if isinstance(item, Item):
            self.items.append(item)
        else:
            raise TypeError

    def getItem(self, pos):
        if pos >= len(self.items) or pos < 0:
            raise ValueError
        else:
            return self.items[pos]

    def getTotal(self, impu):
        if isinstance(impu, float) \
                or isinstance(impu, int):
            total = 0
            for it in self.items:
                total += it.getPrecio()

            return total * (1 + impu / 100)
        else:
            raise TypeError
        
if __name__ == '__main__':
    c = Carrito()
    c.agregar( Item("A100", "regla", 25.0))
    c.agregar( Item("A201", "escuadra", 35.0))
    c.agregar( Item("B070", "marcador", 40.0))

    print( c.getTotal(21))

    i = Item("VB", "toto", 25.00)
