from Pasajeros import pasajero
from Recorridos import recorrido,segmento
from Transporte import transporte

s1 = segmento.Segmento("Retiro","Liniers",30,160,5)
s2 = segmento.Segmento("Liniers", "Lujan", 180, 300, 70)
s3 = segmento.Segmento("Lujan", "Chacabuco", 275, 120, 175)
s4 = segmento.Segmento("Chacabuco", "Junin", 175,0,60)

r = recorrido.Recorrido("Ida Retiro - Junin")
r.agregar_segmento(s1)
r.agregar_segmento(s2)
r.agregar_segmento(s3)
r.agregar_segmento(s4)

recorrido.Recorrido.dar_recorrido(r)

pax1 = pasajero.Pasajero(23123123,'Ana','Liniers','Chacabuco')
pax2 = pasajero.Pasajero(54321321, 'Pablo', 'Retiro', 'Junin')
pax3 = pasajero.Pasajero(43432433, 'Carla', 'Retiro', 'Chacabuco')

t = transporte.Transporte('OVD543', 62, 0.85, 90)
t.agregar_pasajero(pax1)
t.agregar_pasajero(pax2)
t.agregar_pasajero(pax3)

print('\nEl total del recorrido tiene una longitud de '+ str(recorrido.Recorrido.dar_longitud(r))+' Km.')
#print Esta_completo !!! Preguntar a que se refiere con esto, los huecos del recorrido?
transporte.Transporte.listar_pasajeros(t)

print('\nEl tiempo mínimo en completar el recorrido es de: '+str(recorrido.Recorrido.dar_tiempo_minimo(r, t))+' Horas')
print('El total del recorrido consume '+str(recorrido.Recorrido.dar_consumo(r,t))+' Litros de Combustible.')

# pasajero.Pasajero.dar_precio(t) # ESTO ES PARA SACAR EL PRECIO DE CADA PASAJERO, TODAVIA NO ENTIENDO LA LOGICA
