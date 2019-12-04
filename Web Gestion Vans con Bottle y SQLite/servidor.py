import viajes_bd

from bottle import route, run, template, request, static_file

@route('/<filepath:path>')
def server_static(filepath):
    # print(">>>>", filepath)
    return static_file(filepath, root='.')

@route('/')
def menu():
	return template("index.html")

@route('/administrar')
def menu():
	return template("administrar.html", lista_reservas = viajes_bd.mostrar_segmentos("RESERVAS"))

"""	
@route('/lista')
def listado():
    listita = viajes_bd.listar()   
    print(listita) 
    return template('administrar.html', listado = listita)
"""

@route('/reserva')
def reserva():
	return template("reserva", ocupados = viajes_bd.dar_ocupados())


@route('/reserva_post', method='post')
def reserva_post():
    while True:
        try:
            viajes_bd.agregar_reserva(dict(request.POST))
            viajes_bd.agregar_pasajeros(dict(request.POST))
            return template('reserva_ok.html')
        except:
            return template('reserva_fallo.html')

""" 		
@route('/editar', method='get')       
def editar():
    rid = request.GET.get("id")
    datos = viajes_bd.listar(" id = {}".format(rid))
    # print(datos)
    print(list(viajes_bd.dar_lugares()))
    return template('modificar.html', datorig = datos[0], lista_lugares=viajes_bd.dar_lugares())	
   
@route('/editar_post', method='post')
def editar_post():
    viajes_bd.modificar(dict(request.POST), request.POST.get("id"))
	
    listita = viajes_bd.listar()    
   
    return template('lista_combis.html', listado = listita)        
    
@route('/borrar', method='get')
def borrar_reserva():
    rid = request.GET.get("id")
    viajes_bd.borrar(rid)        

    listita = viajes_bd.listar()    
   
    return template('lista_combis.html', listado = listita)    

@route('/buscar')
def consulta():
    return template('buscar.html')
   
@route('/buscar_resultado', method='get')
def consulta_combis():
    abuscar = request.GET.get("telbuscar")
    #listita = combis.listar(" telefono like %s" % (abuscar))
    listita = viajes_bd.listar(" telefono like '{}%'".format(abuscar))    
    return template('lista_combis.html', listado = listita)
"""
if __name__ == '__main__':    
    run(host='127.0.0.1', port=5500, debug=True, reloader=True)