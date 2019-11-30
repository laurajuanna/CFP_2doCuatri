import unittest
#import papel2
import carrito

class T_carrito(unittest.TestCase):
    def setUp(self):
        self.c = carrito.Carrito()
        self.c.agregar( carrito.Item("A100", "regla", 25.0))
        self.c.agregar( carrito.Item("A201", "escuadra", 35.0))
        self.c.agregar( carrito.Item("B070", "marcador", 40.0))

    def test_getTotal(self):
        self.assertEqual(self.c.getTotal(21), 121.0)

    def test_getTotal_err(self):
        with self.assertRaises(TypeError):
            self.c.getTotal("A")

    def test_item_setprecio(self):
        with self.assertRaises(TypeError):
            it = carrito.Item("A234", "cualquiera", "445")

    def test_deprueba(self):
        self.assertAlmostEqual(11.2568, 11.2564, 3)

unittest.main()        
