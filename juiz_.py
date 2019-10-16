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
        
        self.tipo = tipo.upper()
        self.valor = valor
        
    def __hash__(self):
        return ord(self.tipo) + int(self.valor)
        
    def __eq__(self, other):
        return self.tipo == other.tipo and self.valor == other.valor
        
            
class Caja:
    def __init__(self, nombre, lisBilMon = {}):
        self.__lisBilMon = lisBilMon
        self.__nombre = nombre

    def agregarBilMon(self, bm, c):
        if bm in self.__lisBilMon.keys():
            self.__lisBilMon[bm] += c
        else:
            self.__lisBilMon[bm] = c

    def darTotal(self):
        t = 0
        for k in self.__lisBilMon.keys():
            t += k.valor * self.__lisBilMon[k]

        return "Total caja " + self.__nombre +": $ " + str(t) +"\n"

    def listaValores(self):
        s = self.__nombre + " --> \n"
        for k in self.__lisBilMon.keys():
            s += str(k.tipo) +" "+ str(k.valor) + ": " + str(self.__lisBilMon[k]) + "\n"

        return s

    def __lt__(self, other):
        return self.darTotal() < other.darTotal()

    def __str__(self):
        return self.__nombre + " $" + str(self.darTotal())


if __name__ == "__main__": # PARA PROBAR LAS CLASES Y FUNCIONES

    caja_Laura = Caja("Laura", {}) # Crea la caja Laura

    caja_Laura.agregarBilMon(BilMon("m", 0.05), 3) # Crea y agrega valores de moneda    
    caja_Laura.agregarBilMon(BilMon("m", 0.05), 5)
    caja_Laura.agregarBilMon(BilMon("m", 0.25), 3)
    caja_Laura.agregarBilMon(BilMon("m", 1), 6)
    caja_Laura.agregarBilMon(BilMon("b", 5), 20)
    caja_Laura.agregarBilMon(BilMon("b", 500), 5)
    caja_Laura.agregarBilMon(BilMon("b", 20), 10)

    print(caja_Laura.listaValores())
    print(caja_Laura.darTotal())

    c = Caja("Otra", {})
    c.agregarBilMon(BilMon("b", 50), 10)

    d = Caja("Tercera", {})
    d.agregarBilMon(BilMon("b", 100), 20)    
    d.agregarBilMon(BilMon("m", 2), 300)
    d.agregarBilMon(BilMon("b", 100), 20)
    
    print(c.listaValores())
    print(c.darTotal())

    print(d.listaValores())
    print(d.darTotal())

    cajas = []
    cajas.append(caja_Laura)
    cajas.append(c)
    cajas.append(d)

    for cjs in cajas:
        print(cjs)

    cajas.sort()

    for cjs in cajas:
        print(cjs)
