#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  

import sqlite3
base = sqlite3.connect('cEspera.db')
conn = base.cursor()

# Creación de la BD si es que no existe
conn.execute('''CREATE TABLE if not exists espera
	 (id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	  nombre   TEXT                NOT NULL,
	  dni      INT                 NOT NULL,
	  tipo	   TEXT				   NOT NULL,
	  estado   TEXT				
	 );''')


# Función para insertar datos a la BD
def ingresar(nombre,dni,tipo):
	conn.execute("INSERT INTO espera VALUES (?, ?, ?, ?, ?)",
                  (None,nombre, dni, tipo, "E"))
	base.commit()


# Función para obtener el ID asociado a los parametros asociados (nombre y dni)
def getId(nombre,dni):
	sentencia=("SELECT id FROM espera WHERE nombre = ? AND dni = ?;")
	conn.execute(sentencia, [nombre, dni])
	busqueda=conn.fetchall()
	resultado= busqueda[0][0]
	base.commit()
	return resultado
