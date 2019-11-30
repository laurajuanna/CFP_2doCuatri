import unittest
import papel

class Test_papel(unittest.TestCase):
    def setUp(self):
        self.u = papel2.Papel()
        self.bir = papel2.Birome(50)

    def test_escribir(self):
        self.assertEqual((papel2.Papel.escribir("Hola, soy el papel uno.")),"Hola, soy el papel uno.")


unittest.main()
