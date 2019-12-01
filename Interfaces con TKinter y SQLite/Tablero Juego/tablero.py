from tkinter import *
import random

# VENTANA PRINCIPAL
principal = Tk()
principal.title("A V A N T I")
principal.geometry('500x500')
principal.resizable(width=False, height=False)
principal.configure(background='light blue')


class Juego():
    def __init__(self):
        self.cantidad = 0
        self.dado = 0
        self.avaAz = ""
        self.avaVe = ""
        self.avaVi = ""
        self.avaNa = ""
        self.ubicAz = 0
        self.ubicVe = 0
        self.ubicVi = 0
        self.ubicNa = 0
        self.eneAz = 40
        self.eneVe = 40
        self.eneVi = 40
        self.eneNa = 40
    def setDado (self):
        self.dado = random.randint(1,5)
    def setNombre(self,color,nombre):
        if color == "azul":
            self.avaAz = nombre
        if color == "verde":
            self.avaVe = nombre
        if color == "violeta":
            self.avaVi = nombre
        if color == "naranja":
            self.avaNa = nombre
    def setUbicacion(self,color,casillero):
        if color == "azul":
            self.ubicAz = casillero
        if color == "verde":
            self.ubicVe = casillero
        if color == "violeta":
            self.ubicVi = casillero
        if color == "naranja":
            self.ubicNa = casillero
    def getCantidad(self):
        return self.cantidad



class Inicio(Juego):
    def __init__(self):
        def comenzar():
            self.comenzar.place_forget()
            color = "azul"
            nombre = entryAzu.get()
            nuevo.setNombre(color,nombre)
            if nombre != '':
                nuevo.cantidad +=1
            color = "verde"
            nombre = entryVer.get()
            if nombre != '':
                nuevo.cantidad +=1
            nuevo.setNombre(color,nombre)
            color = "violeta"
            nombre = entryVio.get()
            if nombre != '':
                nuevo.cantidad +=1
            nuevo.setNombre(color,nombre)
            color = "naranja"
            nombre = entryNar.get()
            if nombre != '':
                nuevo.cantidad +=1
            nuevo.setNombre(color,nombre)
            jugadores.place_forget()
            jugAzu.place_forget()
            jugVer.place_forget()
            jugVio.place_forget()
            jugNar.place_forget()
            txtAzu.place_forget()
            txtVer.place_forget()
            txtVio.place_forget()
            txtNar.place_forget()
            entryAzu.place_forget()
            entryVer.place_forget()
            entryVio.place_forget()
            entryNar.place_forget()
            btn1.place_forget()
            btn2.place_forget()
            btn3.place_forget()
            btn4.place_forget()
            Tablero()
        self.canvas = Canvas(principal, width=486, height=332, bg="light yellow")
        self.canvas.place(x=5, y=5)
        self.fondo = PhotoImage(file="fondo2.png")
        self.canvas.create_image(9, 9, anchor=NW, image=self.fondo)
        self.comenzar = Button(principal,text="COMENZAR", font="Arial 17 bold", fg="DodgerBlue4", command=comenzar)
        self.comenzar.place(x=277, y=395, width=154, height=50)
        self.azul = PhotoImage(file="avAz.png")
        self.verde = PhotoImage(file="avVe.png")
        self.violeta = PhotoImage(file="avVi.png")
        self.naranja = PhotoImage(file="avNa.png")

        jugadores = Label(principal, bg="Light blue", text="INGRESE JUGADORES", font= "Helvetica 12")
        jugadores.place(x=35,y=346)

        jugAzu = Label(principal, bg="light blue", image=self.azul)
        jugAzu.place(x=15, y=370)
        txtAzu = Label(principal, text = "Jugador 1", bg="Light Blue")
        txtAzu.place(x=46, y=375)
        entryAzu = Entry(principal,state="disable")
        entryAzu.place (x=105, y=375, width=85)
        def chkAzu ():
            entryAzu.config(state="normal")
        btn1= Button(principal, text="+", font=6, command=chkAzu)
        btn1.place(x=195, y=375, width=20, height=20)

        jugVer = Label(principal, bg="light blue", image=self.verde)
        jugVer.place(x=15, y=400)
        txtVer = Label(principal, text = "Jugador 2", bg="Light Blue")
        txtVer.place(x=46, y=405)
        entryVer = Entry(principal, state="disable")
        entryVer.place (x=105, y=405, width=85)
        def chkVer():
            entryVer.config(state="normal")
        btn2= Button(principal, text="+", font=6, command=chkVer)
        btn2.place(x=195, y=405, width=20, height=20)

        jugVio = Label(principal, bg="light blue", image=self.violeta)
        jugVio.place(x=15, y=430)
        txtVio = Label(principal, text = "Jugador 3", bg="Light Blue")
        txtVio.place(x=46, y=435)
        entryVio = Entry(principal, state="disable")
        entryVio.place (x=105, y=435, width=85)
        def chkVio():
            entryVio.config(state="normal")
        btn3= Button(principal, text="+", font=6, command=chkVio)
        btn3.place(x=195, y=435, width=20, height=20)

        jugNar = Label(principal, bg="light blue", image=self.naranja)
        jugNar.place(x=15, y=460)
        txtNar = Label(principal, text = "Jugador 4", bg="Light Blue")
        txtNar.place(x=46, y=465)
        entryNar = Entry(principal, state="disable")
        entryNar.place (x=105, y=465, width=85)
        def chkNar():
            entryNar.config(state="normal")
        btn4= Button(principal, text="+", font=6, command=chkNar)
        btn4.place(x=195, y=465, width=20, height=20)

        mainloop()

class Tablero(Juego):
    def __init__(self):
        # ---------- TABLERO
        self.canvas = Canvas(principal, width=486,height=332, bg="light yellow")
        self.canvas.place(x=5,y=5)
        self.fondo = PhotoImage(file="fondo2.png")
        self.canvas.create_image(9,9, anchor=NW, image=self.fondo)
        self.azul = PhotoImage(file="avAz.png")  # -------------- AVATAR AZUL
        self.verde = PhotoImage(file="avVe.png")  # -------------- AVATAR VERDE
        self.violeta = PhotoImage(file="avVi.png")  # -------------- AVATAR VIOLETA
        self.naranja = PhotoImage(file="avNa.png")  # -------------- AVATAR NARANJA
        # ------------- AVATARES
        cantidad = nuevo.getCantidad()
        if cantidad == 1:
            azul = PhotoImage(file="avAz.png") # -------------- AVATAR AZUL
            self.canvas.create_image(12,116, anchor=NW, image=azul)
        if cantidad == 2:
            azul = PhotoImage(file="avAz.png")  # -------------- AVATAR AZUL
            self.canvas.create_image(12, 116, anchor=NW, image=azul)
            verde = PhotoImage(file="avVe.png") # -------------- AVATAR VERDE
            self.canvas.create_image(37,116, anchor=NW, image=verde)
        if cantidad == 3:
            azul = PhotoImage(file="avAz.png")  # -------------- AVATAR AZUL
            self.canvas.create_image(12, 116, anchor=NW, image=azul)
            verde = PhotoImage(file="avVe.png")  # -------------- AVATAR VERDE
            self.canvas.create_image(37, 116, anchor=NW, image=verde)
            violeta = PhotoImage(file="avVi.png") # -------------- AVATAR VIOLETA
            self.canvas.create_image(12,141, anchor=NW, image=violeta)
        if cantidad == 4:
            azul = PhotoImage(file="avAz.png")  # -------------- AVATAR AZUL
            self.canvas.create_image(12, 116, anchor=NW, image=azul)
            verde = PhotoImage(file="avVe.png")  # -------------- AVATAR VERDE
            self.canvas.create_image(37, 116, anchor=NW, image=verde)
            violeta = PhotoImage(file="avVi.png")  # -------------- AVATAR VIOLETA
            self.canvas.create_image(12, 141, anchor=NW, image=violeta)
            naranja = PhotoImage(file="avNa.png") # -------------- AVATAR NARANJA
            self.canvas.create_image(37,141, anchor=NW, image=naranja)
        dado0 = PhotoImage(file="dado0.png")
        dado1 = PhotoImage(file="dado1.png")
        dado2 = PhotoImage(file="dado2.png")
        dado3 = PhotoImage(file="dado3.png")
        dado4 = PhotoImage(file="dado4.png")
        dado5 = PhotoImage(file="dado5.png")
        def tirarDado():
            nuevo.setDado()
            dado = nuevo.dado
            if dado == 1:
                btnDado.config(image=dado1)
            if dado == 2:
                btnDado.config(image=dado2)
            if dado == 3:
                btnDado.config(image=dado3)
            if dado == 4:
                btnDado.config(image=dado4)
            if dado == 5:
                btnDado.config(image=dado5)
            color = "azul"
            super(Mover.setPosicion(self,color))
        txtDado = Label(principal,text="TIRAR\nDADOS", font="Helvetica 11 bold", bg="light blue", fg="DodgerBlue4")
        txtDado.place(x=377, y=358)
        btnDado = Button(principal, image=dado0, command=tirarDado)
        btnDado.place(x= 375, y= 400)
        mainloop()

class Mover(Juego):
    def __init__(self):
        pass
    def setPosicion(self,color):
        if color == "azul":
            lugar = nuevo.ubicAz
            dado = nuevo.dado
            for nro in range(dado):
                lugar += 1
                if lugar == 26:
                    lugar = 0
            self.canvas.delete(self.azul)
            self.azul = PhotoImage(file="avAz.png")
            if lugar == 0:
                self.azul
                self.canvas.create_image(12, 116, anchor=NW, image=self.azul)
            if lugar == 1:
                self.canvas.create_image(12, 64, anchor=NW, image=self.azul)
            if lugar == 2:
                self.canvas.create_image(12, 12, anchor=NW, image=self.azul)
            if lugar == 3:
                self.canvas.create_image(64, 12, anchor=NW, image=self.azul)
            if lugar == 4:
                self.canvas.create_image(116, 12, anchor=NW, image=self.azul)
            if lugar == 5:
                self.canvas.create_image(168, 12, anchor=NW, image=self.azul)
            if lugar == 6:
                self.canvas.create_image(220, 12, anchor=NW, image=self.azul)
            if lugar == 7:
                self.canvas.create_image(272, 12, anchor=NW, image=self.azul)
            if lugar == 8:
                self.canvas.create_image(324, 12, anchor=NW, image=self.azul)
            if lugar == 9:
                self.canvas.create_image(376, 12, anchor=NW, image=self.azul)
            if lugar == 10:
                self.canvas.create_image(428, 12, anchor=NW, image=self.azul)
            if lugar == 11:
                self.canvas.create_image(428, 64, anchor=NW, image=self.azul)
            if lugar == 12:
                self.canvas.create_image(428, 116, anchor=NW, image=self.azul)
            if lugar == 13:
                self.canvas.create_image(428, 168, anchor=NW, image=self.azul)
            if lugar == 14:
                self.canvas.create_image(428, 220, anchor=NW, image=self.azul)
            if lugar == 15:
                self.canvas.create_image(428, 272, anchor=NW, image=self.azul)
            if lugar == 16:
                self.canvas.create_image(376, 272, anchor=NW, image=self.azul)
            if lugar == 17:
                self.canvas.create_image(324, 272, anchor=NW, image=self.azul)
            if lugar == 18:
                self.canvas.create_image(272, 272, anchor=NW, image=self.azul)
            if lugar == 19:
                self.canvas.create_image(220, 272, anchor=NW, image=self.azul)
            if lugar == 20:
                self.canvas.create_image(168, 272, anchor=NW, image=self.azul)
            if lugar == 21:
                self.canvas.create_image(116, 272, anchor=NW, image=self.azul)
            if lugar == 22:
                self.canvas.create_image(64, 272, anchor=NW, image=self.azul)
            if lugar == 23:
                self.canvas.create_image(12, 272, anchor=NW, image=self.azul)
            if lugar == 24:
                self.canvas.create_image(12, 220, anchor=NW, image=self.azul)
            if lugar == 25:
                self.canvas.create_image(12, 168, anchor=NW, image=self.azul)
        if color == "verde":
            lugar = nuevo.ubicVe
            dado = nuevo.dado
            for nro in range(dado):
                lugar += 1
                if lugar == 26:
                    lugar = 0
            if lugar == 0:
                self.canvas.create_image(37, 116, anchor=NW, image=self.verde) # Posicion Inicial
            if lugar == 1:
                self.canvas.create_image(37, 64, anchor=NW, image=self.verde) # Resta Y
            if lugar == 2:
                self.canvas.create_image(37, 12, anchor=NW, image=self.verde)
            if lugar == 3:
                self.canvas.create_image(89, 12, anchor=NW, image=self.verde) # Suma X
            if lugar == 4:
                self.canvas.create_image(141, 12, anchor=NW, image=self.verde)
            if lugar == 5:
                self.canvas.create_image(193, 12, anchor=NW, image=self.verde)
            if lugar == 6:
                self.canvas.create_image(245, 12, anchor=NW, image=self.verde)
            if lugar == 7:
                self.canvas.create_image(297, 12, anchor=NW, image=self.verde)
            if lugar == 8:
                self.canvas.create_image(349, 12, anchor=NW, image=self.verde)
            if lugar == 9:
                self.canvas.create_image(401, 12, anchor=NW, image=self.verde)
            if lugar == 10:
                self.canvas.create_image(453, 12, anchor=NW, image=self.verde)
            if lugar == 11:
                self.canvas.create_image(453, 64, anchor=NW, image=self.verde) # Suma Y
            if lugar == 12:
                self.canvas.create_image(453, 116, anchor=NW, image=self.verde)
            if lugar == 13:
                self.canvas.create_image(453, 168, anchor=NW, image=self.verde)
            if lugar == 14:
                self.canvas.create_image(453, 220, anchor=NW, image=self.verde)
            if lugar == 15:
                self.canvas.create_image(453, 272, anchor=NW, image=self.verde)
            if lugar == 16:
                self.canvas.create_image(401, 272, anchor=NW, image=self.verde) # Resta X
            if lugar == 17:
                self.canvas.create_image(349, 272, anchor=NW, image=self.verde)
            if lugar == 18:
                self.canvas.create_image(297, 272, anchor=NW, image=self.verde)
            if lugar == 19:
                self.canvas.create_image(245, 272, anchor=NW, image=self.verde) # HICE HASTA ACA
            if lugar == 20:
                self.canvas.create_image(193, 272, anchor=NW, image=self.verde)
            if lugar == 21:
                self.canvas.create_image(141, 272, anchor=NW, image=self.verde)
            if lugar == 22:
                self.canvas.create_image(89, 272, anchor=NW, image=self.verde)
            if lugar == 23:
                self.canvas.create_image(37, 272, anchor=NW, image=self.verde)
            if lugar == 24:
                self.canvas.create_image(37, 220, anchor=NW, image=self.verde) # Resta Y
            if lugar == 25:
                self.canvas.create_image(37, 168, anchor=NW, image=self.verde)
        mainloop()

"""
class Tablero():
    # ---------- TABLERO
    canvas = Canvas(mainWind, width=486,height=332, bg="light yellow")
    canvas.place(x=5,y=5)
    fondo = PhotoImage(file="fondo2.png")
    canvas.create_image(9,9, anchor=NW, image=fondo)
    # ------------- AVATARES
    azul = PhotoImage(file="avAz.png") # -------------- AVATAR AZUL
    #canvas.create_image(12,116, anchor=NW, image=azul)
    verde = PhotoImage(file="avVe.png") # -------------- AVATAR VERDE
    #canvas.create_image(37,116, anchor=NW, image=verde)
    violeta = PhotoImage(file="avVi.png") # -------------- AVATAR VIOLETA
    #canvas.create_image(12,141, anchor=NW, image=violeta)
    naranja = PhotoImage(file="avNa.png") # -------------- AVATAR NARANJA
    #canvas.create_image(37,141, anchor=NW, image=naranja)
    mainloop()"""

nuevo = Juego()
avanti = Inicio()
jugada = Tablero()
mov = Mover()