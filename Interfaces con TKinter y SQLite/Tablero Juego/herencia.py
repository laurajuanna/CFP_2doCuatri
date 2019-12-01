class Mascota():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self,mensaje):
        print(mensaje)
    def setEdad(self,edad):
        self.edad = edad
        print("Tiene",self.edad,"años.")
    def getEdad(self):
        print(self.edad)
    def cumplirAnios(self):
        self.edad +=1
        print("Feliz",self.edad,"cumpleaños",self.nombre,"!")

perro = Mascota("pipo",5)

perro.saludar("Guau!")
perro.setEdad(8)
perro.getEdad()
perro.cumplirAnios()

"""
import tkinter

class Dado(tkinter.Button):
    def __init__(self, r, n):
        self.numero = tkinter.StringVar()
        self.numero.set(str(n))
        super().__init__(r, text=str(n),
                         textvariable=self.numero,
                         width=8, height=4)

    def getNumero(self):
        return (int(self.numero.get()))

    def setNumero(self, n):
        self.numero.set(n)


def incre():
    d1.setNumero(d1.getNumero() + 1)


r = tkinter.Tk()

b = tkinter.Button(r, text="uno", command=incre, width=4, height=4)
d1 = Dado(r, 2)
d2 = Dado(r, 4)

b.grid(row=0, column=0)
d1.grid(row=0, column=1)
d2.grid(row=0, column=2)

r.mainloop()
"""