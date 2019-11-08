#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alumnos.py
# 
  
import sqlite3
conn = sqlite3.connect('alumnos.db')

conn.execute('''CREATE TABLE if not exists ALUMNOS  
     (ID       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      Nombre   TEXT                NOT NULL,
      dni      INT                 NOT NULL,
      aniocursa INT,
      curso    TEXT             
     );''')

def get_id():
    cc = conn.execute("SELECT * FROM alumnos")
    return len(list(cc))+1

def agregarAlumno(nombre, dni, aniocursa, curso):
    id_=get_id()
    conn.execute("INSERT INTO ALUMNOS VALUES (?,?,?,?,?)", (id_, nombre, dni, aniocursa, curso))
    conn.commit()

# qry = f'''INSERT INTO alumnos (id, nombre, dni, aniocursa, curso) VALUES
#             (4, 'Francisco', 44425694, 2019, 'Soldadura')
#            '''
# conn.execute(qry)
# conn.commit()    
      
def listar(condi = ""):
    if condi != "":
        condi = " where " + condi
    cc = conn.execute("SELECT * FROM alumnos" + condi)
    return list(cc)
    cc.close()

def borrar():
    conn.execute("DELETE FROM ALUMNOS WHERE id = 11;")
    conn.commit()

if __name__ == '__main__':
    print(listar())
    print("------")
    print (listar(" nombre like 'L%'"))
    print("------")
    print(listar(" dni > 40000000"))
    print("Aca agrego uno")
    #agregarAlumno("Daniela",5402229,2019,"Cocina")
    print(listar())

