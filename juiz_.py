"""
EJERCICIO 3
Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio desglosado por tipo de billete.
(por ejemplo, en el kiosco de la esquina hay 5 billetes de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos).
Se tiene que poder comparar cajas por la cantidad de dinero que hay en cada una,
y además ordenar una lista de cajas de menor a mayor según la cantidad de dinero disponible.
"""
class BilMon:
    def __init__(self, tipo, valor):
        if tipo not in "mMbB":
            raise TypeError
        tipo = tipo.upper()
        self.denominacion = tipo+" "#+ str(valor)
        self.valor = valor

    def __contains__(self, other):
       return self.denominacion == other.denominacion and self.valor == other.valor

    def __str__(self):
        ''.format()
            
class Caja:
    def __init__(self, nombre, lisBilMon = {}):
        self.__lisBilMon = lisBilMon
        self.__nombre = nombre

    def agregarBilMon(self, bm, cantidad):
        print(bm.__str__())
        if bm not in self.__lisBilMon.keys():
            self.__lisBilMon[bm] = cantidad
        else:
            print("esta")
            self.__lisBilMon[bm] += cantidad

    def darTotal(self):
        t = 0
        for k in self.__lisBilMon.keys(): # Keys es dentro de las claves Clave=Valor
            t += k.valor * self.__lisBilMon[k]
        return t

    def listaValores(self):
        s = self.__nombre + " --> \n"
        for k in self.__lisBilMon.keys():
            s += k.denominacion + str(k.valor) + ": " + str(self.__lisBilMon[k]) + "\n"
        return s

    def __lt__(self, other):
        return self.darTotal() < other.darTotal()

    def __str__(self):
        return self.__nombre + " $" + str(self.darTotal())


if __name__ == "__main__": # PARA PROBAR LAS CLASES Y FUNCIONES

    caja_Laura = Caja("Laura", {}) # Crea la caja Laura

    caja_Laura.agregarBilMon(BilMon("m", 5), 3) # Tipo y valor, cantidad

    caja_Laura.agregarBilMon(BilMon("b",5),3)
    caja_Laura.agregarBilMon(BilMon("b",5),3)
    caja_Laura.agregarBilMon(BilMon("b", 500), 2)
    caja_Laura.agregarBilMon(BilMon("b", 20), 10)

    print(caja_Laura.listaValores())
    print("Este es el total")
    print(caja_Laura.darTotal())
    print(" ")

    c = Caja("Otra", {})
    c.agregarBilMon(BilMon("b", 50), 10)
    c.agregarBilMon(BilMon("b",50),20)

    print(c.listaValores())
    print("Este es el total")
    print(c.darTotal())
    print(" ")

    d = Caja("Tercera", {})
    d.agregarBilMon(BilMon("b", 100), 20)
    d.agregarBilMon(BilMon("m", 2), 300)

    print(d.listaValores())
    print("Este es el total")
    print(d.darTotal())
    print(" ")

    cajas = []
    cajas.append(caja_Laura)
    cajas.append(c)
    cajas.append(d)

    print("Estas son las cajas")
    for cjs in cajas:
        print(cjs)

    print("\nEstas son las cajas ordenadas")
    cajas.sort()

    for cjs in cajas:
        print(cjs)
