class Papel:
    def __init__(self):
        self.texto = ""

    def escribir (self, agregarCad):
        self.texto += agregarCad

    def __str__(self):
        return self.texto


class Birome:
    def __init__(self,tinta):
        self.tinta = tinta

    def escribir(self,Papel,agregarCad):
        cantidadLetras = len(agregarCad)
        self.tinta = self.tinta - cantidadLetras
        if self.tinta >= 0:
            Papel.escribir(agregarCad)
        else:
            print("Ya no hay tinta!")

    def getTinta (self):
        return self.tinta


class Marcador(Birome):
    def __init__(self,tinta):
        self.tinta = tinta

    def recargar (self,nroRecarga):
        self.tinta = self.tinta + nroRecarga


if __name__== "__main__" :
    u = Papel()
    bir = Birome(50)
    bir.escribir(u, "Hola, soy el papel uno.")
    print(u)
    print("El nivel de tinta es de: " + str(bir.getTinta()))

    d = Papel()
    marc = Marcador(20)
    marc.recargar(10)
    marc.escribir(d, "Hola, soy el Papel dos.")
    print(d)

    print("El nivel de tinta es de: " + str(marc.getTinta()))