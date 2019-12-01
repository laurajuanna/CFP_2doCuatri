#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

import sqlite3

base = sqlite3.connect('cEspera.db')
conn = base.cursor()


# Función para obtener todos los ID de la BD asociados al Tipo de trámite ingresado por el Usuario
def getId(tipo):
	sentencia=("SELECT id FROM espera WHERE tipo = ?;")
	conn.execute(sentencia,[tipo])
	busqueda=conn.fetchall()
	resultado= busqueda
	base.commit()
	return resultado


# Función para obtener todos los datos de la BD asociados al ID seleccionado
def getDatos(id):
	sentencia=("SELECT id, tipo, nombre, dni FROM espera WHERE id= ?;")
	conn.execute(sentencia,[id])
	busqueda=conn.fetchall()
	resultado= busqueda
	base.commit()
	return resultado


# Función que devuelve una tupla con el ID y un string con los datos del cliente seleccionado
def getCliente(id):
	datos = getDatos(id)
	id= datos[0][0]
	tipo= datos[0][1]
	nombre= datos[0][2]
	dni= datos[0][3]
	return (id,((tipo+str(id))+(" - ")+nombre+(" - ")+(str(dni))))


# Función para borrar de la BD todos los datos asociados a un determinado ID
def borrar(id):
	sentencia = ('DELETE FROM espera WHERE id = ?;')
	conn.execute(sentencia, [id])
	base.commit()
