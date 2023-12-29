import unittest
from modelo.computadora import Computadora

class TestComputadora(unittest.TestCase):

    def setUp(self):

        self.o1 = Computadora('red1', '127.0.0.1', 'Loc1', 'AMD', 256, 4, '12/4/2020')
        self.o2 = Computadora('red2', '192.168.43.1', 'Local', 'INTEL', 512, 4, '1/1/2021')

    def test_nombre_red(self):

        self.assertEqual(self.o1.nombre_red, 'red1')
        self.assertFalse(self.o1.nombre_red == 'red2')

        self.assertEqual(self.o2.nombre_red, 'red2')
        self.assertFalse(self.o2.nombre_red == 'red1')

    def test_ip(self):

        self.assertEqual(self.o1.ip, '127.0.0.1')
        self.assertFalse(self.o1.ip == '127.0.0.2')

        self.assertEqual(self.o2.ip, '192.168.43.1')
        self.assertTrue(self.o2.ip == '192.168.43.1')

    def test_local(self):

        self.assertEqual(self.o1.local, 'Loc1')
        self.assertFalse(self.o1.local == 'Loc')

        self.assertEqual(self.o2.local, 'Local')
        self.assertFalse(self.o2.local == 'Loc')

    def test_microprocesador(self):

        self.assertEqual(self.o1.microprocesador, 'AMD')
        self.assertFalse(self.o1.microprocesador == 'amd')

        self.assertEqual(self.o2.microprocesador, 'INTEL')
        self.assertFalse(self.o2.microprocesador == 'intel')

    def test_espacio_disco_duro(self):

        self.assertEqual(self.o1.espacio_disco_duro, 256)
        self.assertFalse(self.o1.espacio_disco_duro == 128)

        self.assertEqual(self.o2.espacio_disco_duro, 512)
        self.assertFalse(self.o2.espacio_disco_duro == 1024)

    def test_ram_integrada(self):

        self.assertEqual(self.o1.ram_integrada, 4)
        self.assertFalse(self.o1.ram_integrada == 2)

        self.assertEqual(self.o2.ram_integrada, 4)
        self.assertFalse(self.o2.ram_integrada == 6)

    def test_fecha_adquisicion(self):

        self.assertEqual(self.o1.fecha_adquisicion, '12/4/2020')
        self.assertFalse(self.o1.fecha_adquisicion == '12/5/2020')

        self.assertEqual(self.o2.fecha_adquisicion, '1/1/2021')
        self.assertFalse(self.o2.fecha_adquisicion == '1/2/2021')

