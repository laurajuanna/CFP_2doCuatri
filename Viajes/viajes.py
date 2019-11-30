from Pasajeros import pasajero
from Recorridos import recorrido, segmento
from Transporte import transporte

# Creo los segmentos
s1 = segmento.Segmento("Retiro","Liniers",30, 160, 5)
s2 = segmento.Segmento("Liniers", "Lujan", 180, 300, 70)
s3 = segmento.Segmento("Lujan", "Chacabuco", 275, 120, 175)
s4 = segmento.Segmento("Chacabuco", "Junin", 175, 0, 60)

# Creo el recorrido
r = recorrido.Recorrido("IDA RETIRO - JUNIN")

# Agrego los segmentos al recorrido
r.agregar_segmento(s1)
r.agregar_segmento(s2)
r.agregar_segmento(s3)
r.agregar_segmento(s4)

# Muestro el recorrido
r.dar_recorrido(r)

# Doy la longitud total del recorrido
print('\nLongitud total del recorrido: '+ str(r.dar_longitud())+' Km.')

# Pregunto si el recorrido tiene huecos
print("\nEl recorrido esta completo? " + str(r.esta_completo()))

# Creo los pasajeros
pasajero_1 = pasajero.Pasajero(23123123, 'Ana', 'Liniers', 'Chacabuco',r)
pasajero_2 = pasajero.Pasajero(54321321, 'Pablo', 'Retiro', 'Junin',r)
pasajero_3 = pasajero.Pasajero(43432433, 'Carla', 'Retiro', 'Chacabuco',r)

# Creo el transporte
t = transporte.Transporte('OVD543', 62, 0.85, 90)

# Agrego los pasajeros
t.agregar_pasajero(pasajero_1)
t.agregar_pasajero(pasajero_2)
t.agregar_pasajero(pasajero_3)

# Doy la lista de pasajeros con el metodo estático
t.listar_pasajeros(t)

# Muestro el porcentaje de ocupacion
t.dar_porcentaje_ocupacion()


# Muestro el tiempo mínimo del recorrido
print('\nTiempo mínimo en completar el recorrido: '+str(r.dar_tiempo_minimo(t))+' Horas')

# Muestro el consumo total de combustible del recorrido
print('\nConsumo total del recorrido: '+str(r.dar_consumo(t))+' Lts x Km de Combustible.')

# Muestro el costo total del recorrido (agregando el precio del Litro de combustible
print("\nCosto total del recorrido: $"+str(r.dar_costo(t,54)))

# Muestro el ingreso total
print('\nIngreso total del recorrido: $' + str(t.dar_ingreso()))

# Pregunto si existe un lugar en el recorrido y da TRUE
print('\nExiste éste lugar en el recorrido? '+str(r.existe_lugar("Liniers")).upper())

# Pregunto si existe un lugar en el recorrido y da FALSE
print('\nExiste éste lugar en el recorrido? '+str(r.existe_lugar("La Boca")).upper())