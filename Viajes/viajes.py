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

print(recorrido.Recorrido.dar_recorrido)