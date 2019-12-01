import tkinter as tk

def codificar():
  mensaje = (entrada1.get())
  codigo = ""
  for x in range(len(mensaje)):
    letra = (mensaje[x])
    numero = (int(ord(letra)))+1
    codigo = codigo+(chr(numero))
    cadena = ("\nSu mensaje ha sido codificado:\n")
  return var.set(cadena+codigo)

def decodificar():
  mensaje = (entrada1.get())
  codigo = ""
  for x in range(len(mensaje)):
    letra = (mensaje[x])
    numero = (int(ord(letra)))-1
    codigo = codigo+(chr(numero))
    cadena = ("\nSu mensaje ha sido decodificado:\n")
  return var.set(cadena+codigo)

ventana = tk.Tk()
ventana.title("Codificador")
ventana.geometry('380x230')
ventana.configure(background='light blue')

var=tk.StringVar()

texto1 = tk.Label(ventana,text="Ingrese el mensaje a codificar:",bg="light blue",fg="black")
texto1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=45,pady=5,ipadx=2,ipady=2)

botoncod=tk.Button(ventana,text="Codificar",fg="black",command=codificar)
botoncod.pack(fill=tk.X,padx=125,pady=5,ipadx=2,ipady=2)

botondec=tk.Button(ventana,text="Decodificar",fg="black",command=decodificar)
botondec.pack(fill=tk.X,padx=125,pady=5,ipadx=2,ipady=2)


res=tk.Label(ventana,bg="light blue",fg="black",textvariable=var,padx=145,pady=2)
res.pack()

ventana.mainloop()