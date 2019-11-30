# Autoevaluación

•	 Hacer un pequeño sistema que permita gestionar una empresa de combis y colectivos de media/larga distancia.

Las clases propuestas son:

```
PASAJERO
--------------------------------------------------
dni: int
nombre: str
origen: str
destino: str
--------------------------------------------------
dar_precio_pasaje: float 
--------------------------------------------------


TRANSPORTE
--------------------------------------------------
patente: str
capacidad: int
consumo: float
vel_max: float
pasajeros:[Pasajero]
--------------------------------------------------
agregar_pasajero(Pasajero)
dar_ingreso_viaje: float 
dar_porcentaje_ocupacion: float
--------------------------------------------------


SEGMENTO
--------------------------------------------------
origen: str
destino: str
precio: float
precio_peajes: float
longitud: float
--------------------------------------------------


RECORRIDO
--------------------------------------------------
nombre: str
recorrido: [Segmentos]
--------------------------------------------------
dar_costo(Transporte, precio_combustible): float
dar_longitud: float
dar_consumo(Transorte): float
dar_tiempo_minimo(Transporte): float

agregar_segmento(Segmento)

esta_completo: bool
existe_lugar(str): bool
--------------------------------------------------
```

•	Hacer cada clase y su código auxiliar en un archivo independiente (persona.py, transporte.py, etc.) y organizar el sistema en paquetes: personas, transportes y trayectos. Por ejemplo:

```
viajes
|
+--	viajes.py
	|
	+--	recorridos 
	|		+-- __init__.py
	|		+-- segmentos.py
	|		+-- recorridos.py
	|		+-- tests
	|			+-- test_recorridos.py
	|			+-- test_segmentos.py
	|
	+--	transportes 
	|       	+-- __init__.py
	|		+-- transporte.py
			+-- tests
	|			+-- test_transporte.py
	|
	+--	pasajeros 
			+-- __init__.py  
			+-- pasajero.py
 			+-- tests
				+-- test_pasajero.py
```

•	En lo posible evitar el ingreso de datos incorrectos. Generar excepciones en casos de situaciones anómalas (transporte completo, recorrido incompleto, etc.)

