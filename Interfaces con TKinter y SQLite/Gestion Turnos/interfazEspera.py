import espera as bde
import tkinter
from tkinter import messagebox


# Función que guarda los turnos en la BD
def turno():
    nombre = str(txtNombre.get()) # Guarda en la variable lo ingresado el el campo de Nombre
    dni = txtDni.get() # Guarda en la variable lo ingresado en el campo Dni
    entryTipo = str(txtTipo.get()) # Guarda en la variable lo ingresado en el campo Tipo
    tipo= entryTipo.upper() # Transforma lo ingresado en el campo Tipo a Mayuscula y lo guarda en la variable
    if validarDni(dni) == True and validarTipo(tipo)==True: # Valida que lo ingresado sea correcto
        bde.ingresar(nombre,dni,tipo) # Si es correcto lo ingresa en la Base de datos
        id = bde.getId(nombre,dni) # Busca el ID de los datos recien guardados en la BD y la guarda en la variable
        nroTurno = tipo+(str(id)) # Guarda en la variable el Nro de Turno asociado al ID y luego lo muestra en el Messagebox
        messagebox.showinfo("Turno Asignado", ("Bienvenida/o "+nombre+" !\nSu número de turno asignado es el:\n---> "+nroTurno))


# Función para validar el Tipo de trámite
def validarTipo(tipo):
    ref_anotacion = {"A": "A", "B": "B", "C": "C"} # Diccionario con las opciones correctas
    if tipo not in ref_anotacion:  # Si lo ingresado no está en el diccionario dará error
        messagebox.showinfo("Error", "El Tipo de trámite ingresado no es correcto.\nIngrese trámites Tipo A, B o C.")
        return False
    else:
        return True


# Función para validar el DNI
def validarDni(dni):
    nro = dni # Asignamos lo ingresado en el campo DNI a la variable nro
    esValido = False # Asociamos a esta variable el valor False para poder controlar el siguiente While
    while (esValido == False):
        try:
            val = int(nro)
            esValido = True
            return True # Si el DNI ingresado es correcto retornará True (dentro del IF de la función turno)
        except ValueError: # Si el DNI ingresado es incorrecto mostrará el error hasta que el Try retorne True
            messagebox.showinfo("Error", "El DNI ingresado no es correcto, inténtelo nuevamente.")
            esValido = True


# Función para cerrar el programa
def salir():
    mainWind.destroy()


# Creo el objeto Ventana
mainWind = tkinter.Tk()

# Agrego un titulo a la ventana
mainWind.title("Asignación de Turnos")

# Creo textos y entry's

lblNombre = tkinter.Label(mainWind, text="Apellido y Nombre")
txtNombre = tkinter.Entry(mainWind)

lblDni = tkinter.Label(mainWind, text="DNI Número")
txtDni = tkinter.Entry(mainWind)

lblTipo = tkinter.Label(mainWind, text="Tipo de Trámite")
txtTipo = tkinter.Entry(mainWind)


# Creo botones

btnTurno = tkinter.Button(mainWind, text="Sacar turno", command=turno)
btnSalir = tkinter.Button(mainWind, text="Salir", command=salir)


# Ubico todos los objetos en la grilla

lblNombre.grid(column=0, row=0, columnspan=2, ipadx=5)
txtNombre.grid(column=2, row=0, columnspan=2, padx=5,pady=5,ipadx=4,ipady=1)

lblDni.grid(column=0, row=1, columnspan=2, ipadx=5)
txtDni.grid(column=2, row=1, columnspan=2, padx=0,pady=2,ipadx=4,ipady=1)

lblTipo.grid(column=0, row=2, columnspan=2, ipadx=5)
txtTipo.grid(column=2, row=2, columnspan=2, padx=5,pady=5,ipadx=4,ipady=1)

btnTurno.grid(column=1, row=3, padx=1,pady=1, ipadx=8,ipady=1)

btnSalir.grid(column=2, row=3, columnspan=2, padx=1,pady=1, ipadx=26,ipady=1)


# Reproductor
mainWind.mainloop()
