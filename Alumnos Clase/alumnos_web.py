import alumnos

from bottle import route, run, template, request, static_file

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='.')

@route('/lista')
def lista_alumnos():
    listita = alumnos.listar()    
    return template('alumnos.html', listado = listita)

@route('/listacona')
def lista_alumnos_a():
    listita = alumnos.listar(" nombre like 'A%'")    
    return template('alumnos.html', listado = listita)

@route('/buscar', method='get')
def consulta_alumnos():
    abuscar = request.GET.get("nombrebuscar")
    #listita = alumnos.listar(" nombre like %s" % (abuscar))
    listita = alumnos.listar(" nombre like '{}%'".format(abuscar))
    return template('busqueda.html', listado = listita)

@route('/agregar_a')
def agregar():
    return template('agregar_a.html')

@route('/agregar', method='get')
def agregar_alumnos():
    nombre = request.GET.get("agrego_nombre")
    dni = request.GET.get("agrego_dni")
    aniocursa = request.GET.get("agrego_anio")
    curso = request.GET.get("agrego_curso")
    alumnos.agregarAlumno(nombre,dni,aniocursa,curso)
    listita = alumnos.listar()
    return template('alumnos.html', listado=listita)

@route('/consulta')
def consulta():
    return template('consulta.html')

if __name__ == '__main__':    
    run(host='localhost', port=8080, debug=True, reloader=True)