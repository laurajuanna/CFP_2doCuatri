from Pasajeros import pasajero
from Recorridos import recorrido,segmento
from Transporte import transporte

s1 = segmento.Segmento("Retiro","Liniers",30,160,5)
s2 = segmento.Segmento("Liniers", "Lujan", 180, 300, 70)
s3 = segmento.Segmento("Lujan", "Chacabuco", 275, 120, 175)
s4 = segmento.Segmento("Chacabuco", "Junin", 175,0,60)

r = recorrido.Recorrido("ida Retiro-Junin")
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

transporte.Transporte.listar_pasajeros(t)
