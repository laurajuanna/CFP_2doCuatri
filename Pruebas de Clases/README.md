# Ejercicios con Objetos

### 1 Codificar las siguientes clases
```
CARRITO
--------------------------
- items [Item]
--------------------------
+ agregar(item)
+ getItem(index): Item        
+ getTotal(impueso): float
--------------------------

ITEM
--------------------------
- codigo: string
- precio: float
--------------------------
```
•	Hacer tests automáticos de la clase Carrito

- [Resolución del ejercicio](https://github.com/laurajuanna/CFP_2doCuatri/blob/master/Pruebas%20de%20Clases/carrito.py).
- [Resolución del test - Incompleto](https://github.com/laurajuanna/CFP_2doCuatri/blob/master/Pruebas%20de%20Clases/test_carrito.py).

### 2 Escribir una clase "Papel" que contenga:
- Un texto
- Un método escribir
- Que reciba una cadena para agregar al texto
- El método __str__ que imprima el contenido del texto.

Escribir una clase Birome que contenga:
- Una cantidad de tinta
- Un método escribir
- Que reciba un texto y un papel sobre el cual escribir
- Cada letra escrita debe reducir la cantidad de tinta contenida.
- Cuando la tinta se acabe, debe lanzar una excepción.

Escribir una clase Marcador que:
- Herede de Birome y agregue el método recargar
- Que reciba la cantidad de tinta a agregar.

- [Resolución del ejercicio](https://github.com/laurajuanna/CFP_2doCuatri/blob/master/Pruebas%20de%20Clases/papel.py).
- [Resolución del test - Incompleto](https://github.com/laurajuanna/CFP_2doCuatri/blob/master/Pruebas%20de%20Clases/test_papel.py).

### 3 Escribir una clase Caja para representar:
Cuánto dinero hay en una caja de un negocio, desglosado por tipo de billete (por ejemplo, en el kiosco de la esquina hay 5 billetes de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos). Se tiene que poder comparar cajas por la cantidad de dinero que hay en cada una, y además ordenar una lista de cajas de menor a mayor según la cantidad de dinero disponible.

- [Resolución del ejercicio](https://github.com/laurajuanna/CFP_2doCuatri/blob/master/Pruebas%20de%20Clases/cajas.py).
