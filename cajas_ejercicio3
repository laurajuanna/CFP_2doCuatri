"""
EJERCICIO 3
Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio desglosado por tipo de billete.
(por ejemplo, en el kiosco de la esquina hay 5 billetes de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos).
Se tiene que poder comparar cajas por la cantidad de dinero que hay en cada una,
y además ordenar una lista de cajas de menor a mayor según la cantidad de dinero disponible.
"""


class Moneda: # Primero creo la clase moneda y defino x defecto que hay 0 cantidad de cada moneda y la lista total vacia
    def __init__(self):
        self.mon_5c = 0
        self.mon_10c = 0
        self.mon_25c = 0
        self.mon_50c = 0
        self.mon_1p = 0
        self.mon_2p = 0
        self.mon_5p = 0
        self.mon_total = [] # Lista de la cantidad de monedas de cada valor

    def agregarMoneda (self,valor,cantidad): # Esta funcion agrega la cantidad de monedas a su respectiva variable
        if valor == 0.05:
            self.mon_5c += cantidad
        if valor == 0.10:
            self.mon_10c += cantidad
        if valor == 0.25:
            self.mon_25c += cantidad
        if valor == 0.50:
            self.mon_50c += cantidad
        if valor == 1:
            self.mon_1p += cantidad
        if valor == 2:
            self.mon_2p += cantidad
        if valor == 5:
            self.mon_5p += cantidad

    def get_ListaMonedas(self): # Esta función devuelve la lista de cantidad de monedas x valor
        self.mon_total = [self.mon_5c, self.mon_10c, self.mon_25c, self.mon_50c, self.mon_1p, self.mon_2p, self.mon_5p]
        return self.mon_total

    def get_SumaMonedas (self): # Esta lista multiplica la cantidad de monedas x su valor y devuelve la suma total
        suma = 0
        self.mon_total = [self.mon_5c * 0.05, self.mon_10c * 0.10, self.mon_25c * 0.25, self.mon_50c * 0.5,
                          self.mon_1p * 1, self.mon_2p * 2, self.mon_5p * 5]
        for mon in self.mon_total:
            suma += mon
        return suma

    def print_Monedas (self): # Esta función IMPRIME la lista de monedas x cantidad
        return '5 ctvs: {} | 10 ctvs: {} | 25 ctvs: {} | 50 ctvs: {} | 1 peso: {} | 2 pesos: {} | 5 pesos: {}'.format(
            self.mon_5c, self.mon_10c, self.mon_25c, self.mon_50c, self.mon_1p, self.mon_2p, self.mon_5p)



class Billete: # Primero creo la clase billete y defino x defecto que hay 0 cantidad de cada billete y la lista total vacia
    def __init__(self):
        self.bil_5 = 0
        self.bil_10 = 0
        self.bil_20 = 0
        self.bil_50 = 0
        self.bil_100 = 0
        self.bil_500 = 0
        self.bil_1000 = 0
        self.bil_total = [] # Lista de la cantidad de billetes de cada valor

    def agregarBillete(self,valor,cantidad): # Esta funcion agrega la cantidad de billetes a su respectiva variable
        if valor == 5:
            self.bil_5 +=cantidad
        if valor == 10:
            self.bil_10 += cantidad
        if valor == 20:
            self.bil_20 += cantidad
        if valor == 50:
            self.bil_50 += cantidad
        if valor == 100:
            self.bil_100 += cantidad
        if valor == 500:
            self.bil_500 += cantidad
        if valor == 1000:
            self.bil_1000 += cantidad

    def get_ListaBilletes (self): # Esta función devuelve la lista de cantidad de billetes x valor
        self.bil_total = [self.bil_5, self.bil_10, self.bil_20, self.bil_50, self.bil_100, self.bil_500, self.bil_1000]
        return self.bil_total

    def get_SumaBilletes (self): # Esta lista multiplica la cantidad de billetes x su valor y devuelve la suma total
        suma = 0
        self.bil_total = [self.bil_5 * 5, self.bil_10 * 10, self.bil_20 * 20, self.bil_50 * 50, self.bil_100 * 100,
                          self.bil_500 * 500, self.bil_1000 * 1000]
        for bil in self.bil_total:
            suma += bil
        return suma

    def print_Billetes (self): # Esta función IMPRIME la lista de billetes x cantidad
        return '5 pesos: {} | 10 pesos: {} | 20 pesos: {} | 50 pesos: {} | 100 pesos: {} | 500 pesos: {} | 1000: {}'.format(
            self.bil_5, self.bil_10, self.bil_20, self.bil_50, self.bil_100, self.bil_500, self.bil_1000)



class Caja(Moneda,Billete): # Se crea la clase Caja que contendrá la lista de monedas y billetes
    def __init__(self,nombre):
        self.nombre_Caja = nombre
        self.caja_valores = []
        self.caja_total = 0

    # Agregamos los nombres de las clases moneda y billete a la lista Caja_valores
    def agregarValores(self,moneda_nombreCaja,billete_nombreCaja):
        monedas = moneda_nombreCaja.get_ListaMonedas()
        self.caja_valores.append(monedas)
        billetes = billete_nombreCaja.get_ListaBilletes()
        self.caja_valores.append(billetes)

    # Devuelve el nombre de la caja y los valores que contiene en su respectiva lista de valores de monedas y billetes
    def getCaja_Valores(self):
        return self.nombre_Caja,self.caja_valores

    # Devuelve el nombre de la caja y la suma total de dinero que contiene
    def sumarTotal(self,moneda,billete):
        monedas = moneda.get_SumaMonedas()
        billetes = billete.get_SumaBilletes()
        suma = monedas+billetes
        return self.nombre_Caja,suma



class BancoDeCajas: # Creación del "Banco de cajas" que contendrá TODAS las cajas creadas
    def __init__(self):
        self.cajas_Totales = [] # Lista de las cajas x nombre y valores contenidos separados x moneda y billete
        self.cajas_Sumas = [] # Lista de cajas x nombre y suma total del dinero contenido

    def agregar_aBanco(self,nombre_caja,moneda_nombreCaja,billete_nombreCaja): #esta función agrega las cajas al banco de cajas
        valores_cajas = nombre_caja.getCaja_Valores()
        self.cajas_Totales.append(valores_cajas)
        sumas_cajas = nombre_caja.sumarTotal(moneda_nombreCaja,billete_nombreCaja)
        self.cajas_Sumas.append(sumas_cajas)

    def get_cajas_Totales(self): # Esta función devuelve todas las cajas que hay y su contenido separado x billetes y monedas
        return self.cajas_Totales

    def get_cajas_Sumas(self): # Esta función devuelve las cajas con sus respectivos nombres ordenadas x el valor del dinero que contiene
        cajas = self.cajas_Sumas
        for ele in cajas:
            self.cajas_Sumas.sort(key=lambda ele: ele[1])
        return cajas



if __name__ == "__main__": # PARA PROBAR LAS CLASES Y FUNCIONES

    caja_General = BancoDeCajas()

    caja_Laura = Caja("Laura") # Crea la caja Laura

    mon_Lau = Moneda() # Crea y agrega valores de moneda
    mon_Lau.agregarMoneda(0.05, 5)
    mon_Lau.agregarMoneda(0.25, 3)
    mon_Lau.agregarMoneda(1, 6)

    bil_Lau = Billete() # Crea y agrega valores de billete
    bil_Lau.agregarBillete(5, 20)
    bil_Lau.agregarBillete(500, 5)
    bil_Lau.agregarBillete(20, 10)

    caja_Laura.agregarValores(mon_Lau, bil_Lau) # Agrega los valores a la caja creada
    caja_General.agregar_aBanco(caja_Laura,mon_Lau,bil_Lau)

    caja_Oliver = Caja("Oliver")  # Crea la caja Oliver

    mon_Oliver = Moneda()
    mon_Oliver.agregarMoneda(0.05,6)
    mon_Oliver.agregarMoneda(2,5)

    bil_Oliver = Billete()
    bil_Oliver.agregarBillete(20,5)
    bil_Oliver.agregarBillete(100,50)

    caja_Oliver.agregarValores(mon_Oliver,bil_Oliver)
    caja_General.agregar_aBanco(caja_Oliver,mon_Oliver,bil_Oliver)

    # Prints para ver si funcan las clases y funciones
    print(mon_Lau.get_ListaMonedas())
    print(mon_Lau.print_Monedas())
    print("Este es el total de monedas de la caja")
    print(mon_Lau.get_SumaMonedas())
    print(bil_Lau.get_ListaBilletes())
    print(bil_Lau.print_Billetes())
    print("Este es el total de billetes de la caja")
    print(bil_Lau.get_SumaBilletes())
    print("Este es el total de monedas y billetes de la caja")
    print(caja_Laura.getCaja_Valores())
    print("Esta es la suma del dinero total de la caja")
    print(caja_Laura.sumarTotal(mon_Lau, bil_Lau))
    print("\nEstas son todas las cajas que hay en el Banco de Cajas")
    print(caja_General.get_cajas_Totales())
    print("\nEstas son todas las cajas ordenadas por el Valor de Dinero que contienen de menor a mayor")
    print(caja_General.get_cajas_Sumas())
