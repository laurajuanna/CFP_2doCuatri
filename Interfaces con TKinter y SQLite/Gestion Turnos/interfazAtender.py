import atender as bda
import tkinter
from tkinter import messagebox

# Diccionario para guardar los Clientes en Espera que se mostraran segun el Tipo de tramite
items={}


# Función para atender clientes,
# una vez que los atiende, pregunta si quiere borrarlo de la base de datos
def atender():
    cliente = lstNombres.get(lstNombres.curselection())
    messagebox.showinfo("Cliente Elegido", cliente)
    borrar()

# Función para actualizar los datos
def refrescar():
    lstNombres.delete(0, tkinter.END) # Si había algo mostrandose antiguamente lo borra
    entrada= txtTipoEntry.get() # input del usuario en la casilla de Tipo de Trámite
    tipo=entrada.upper() # pasa lo ingresado anteriormente a Mayúscula
    nrosId= bda.getId(tipo) # Busca en la BD todos los ID asociados al Tipo ingresado y los guarda en una lista
    if not nrosId: # Si no hay ningun cliente en espera muestra un mensaje de aviso
        messagebox.showinfo("Turnos En Espera",("No hay turnos del tipo "+tipo+" en espera.\nPor favor ingrese otro Tipo."))
    for nro in nrosId: # Itera los ID de la lista anterior
        id= nro[0] # Guarda en esta variable el ID iterado
        cliente = bda.getCliente(id)[1] # Busca en la BD los datos asociados al ID anterior y los guarda en esta variable
        lstNombres.insert(id, cliente) # Muestra en el Listbox los datos encontrados
        items[cliente]=id # Guarda los datos en el diccionario Items (clave=clientes, valor=id)


# Función para borrar de la lista de Listbox
def borrarLista():
	cliente = lstNombres.curselection()
	if(cliente != ""):
		lstNombres.delete(cliente)


# Función para borrar a un cliente del Listbox y de la BD
def borrar():
    cliente = lstNombres.get(lstNombres.curselection()) # Esta variable tambien se asocia a la clave del diccionario
    id = items[cliente] # Obtiene el ID del cliente buscando el valor asociado a la clave cliente del diccionario
    if messagebox.askyesno("Atención","Desea borrar al cliente de la Base de Datos?"): # Salta un mensaje
        bda.borrar(id) # Se borra de la base de datos
        borrarLista() # Se borra de la lista de Listbox
        items.clear() # Se borra el contenido del diccionario


# Funcion para cerrar la ventana
def salir():
    if messagebox.askyesno("Atención", "¿Desea salir?"):
        top.destroy()


# Creo la ventana principal
top = tkinter.Tk()
top.title("Admisión de Trámites")  # título de la ventana principal


# Creo todos los widgets
lstNombres = tkinter.Listbox(top)
btnRefrescar = tkinter.Button(top, text="Refrescar Tipo", underline=0, command=refrescar)
btnAtender = tkinter.Button(top, text="Atender", underline=0, command=atender)
btnBorrar = tkinter.Button(top, text="Borrar", underline=0, command=borrar)
lblTipo = tkinter.Label(top, text="Tipo")
txtTipoEntry = tkinter.Entry(top)
btnSalir = tkinter.Button(top, text="Salir", underline=0, command=salir)


# Posiciono cada widget
lstNombres.grid(row=0, column=0, rowspan=4, padx=10, pady=10, ipadx=25)
btnRefrescar.grid(row=5, column=0, ipadx=10)
btnAtender.grid(row=0, column=2)
btnBorrar.grid(row=1, column=2, ipadx=6)
btnSalir.grid(row=2, column=2, padx=5, ipadx=10)
lblTipo.grid(row=5, column=1, ipadx=5, ipady=5)
txtTipoEntry.grid(row=5, column=2, padx=10, pady=5)


# Reproductor
top.mainloop()
