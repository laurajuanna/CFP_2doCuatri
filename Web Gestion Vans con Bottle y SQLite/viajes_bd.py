#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('combis.db')


# CREACION DE TABLAS

conn.execute('''CREATE TABLE if not exists RESERVAS
     (id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      nombre    TEXT    NOT NULL,
      telefono  INT     NOT NULL,
      fecha     TEXT    NOT NULL,
      origen   TEXT     NOT NULL,
      destino TEXT      NOT NULL,
      hora      TEXT    NOT NULL,
      asiento   INT     NOT NULL
      );''')

conn.execute('''CREATE TABLE if not exists PASAJEROS
     (id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      nombre   TEXT             NOT NULL,
	  telefono      INT              NOT NULL
      );''')

conn.execute('''CREATE TABLE if not exists TRANSPORTE
     (id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      patente       TEXT              NOT NULL,
      capacidad     INT,
	  consumo       INT,
	  max_vel  INT
      );''')


def agregar_reserva(valores):
    print(valores)
    qry = '''INSERT INTO RESERVAS
                 (nombre, telefono, fecha, origen, destino, hora, asiento)
          VALUES
                ('{}','{}','{}','{}','{}','{}','{}')
        '''.format(valores['nombre'],\
        int(valores['telefono']),valores['fecha'],\
        valores['origen'],valores['destino'],\
        valores['hora'],int(valores['asiento']))
    conn.execute(qry)
    conn.commit()


def agregar_pasajeros(datos):
    print(datos)
    qry = ''' INSERT INTO PASAJEROS
        (nombre, telefono)
        VALUES
        ('{}','{}')
        '''.format(datos['nombre'],int(datos['telefono']))
    conn.execute(qry)
    conn.commit()

def agregar_transporte(datos):
    qry = ''' INSERT INTO TRANSPORTE
        (patente, capacidad, consumo, max_vel)
        VALUES
        ('{}','{}','{}','{}')
        '''.format(datos[0],int(datos[1]),int(datos[2]), \
                   int(datos[3]))
    conn.execute(qry)
    conn.commit()

def modificar(valores, id):
    print(" ", valores)
    qry = '''UPDATE combis SET
                nombre = '{}',
                telefono = '{}',
                subeEn = '{}',
                bajaEn = '{}',
                nroAsiento = {},
                pago = {}
			where id = {}
			'''.format(valores['nombre'], \
                       valores['tele'], valores['sube'], \
                       valores['baja'], valores['asiento'], \
                       int(valores['pagado']), int(id))

    print(qry)

    conn.execute(qry)
    conn.commit()


def borrar(rid):
    qry = '''DELETE FROM RESERVAS WHERE id = {}'''.format(rid)

    conn.execute(qry)
    conn.commit()


def dar_ocupados():
    ocupados = []
    cc = conn.execute("SELECT asiento FROM RESERVAS")
    resultado = list(cc)
    for x in resultado:
        ocupados.append(x[0])
    return ocupados
    cc.close()


def mostrar_segmentos(condi):
    cc = conn.execute("SELECT * FROM " + condi +" ORDER BY asiento")
    return list(cc)
    cc.close()

def mostrar_por_fecha(condi):
    cc = conn.execute("SELECT * FROM RESERVAS WHERE fecha = '{}'".format(condi))
    return list(cc)
    cc.close()

def mostrar_todo(name_table):
    lista = mostrar_segmentos(name_table)
    for x in range(len(lista)):
        print(lista[x])

def borrar_muchos(nro_inicial,nro_final):
    for x in range(nro_inicial,nro_final):
        borrar(x)

#borrar_muchos(56,58)
#print(mostrar_todo("RESERVAS"))

#print(dar_ocupados())

#print(mostrar_por_fecha("2019-12-04"))

#print(mostrar_segmentos("RESERVAS"))





#if __name__ == '__main__':
    #print(listar())
    #print("------")
    #    print(listar(" nombre like 'A%'"))
    #print("------")
    # print(listar(" dni > 40000000"))
    # print(dar_lugares())