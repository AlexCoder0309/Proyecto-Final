import unittest
from modelo.computadora_internet import ComputadoraInternet

class TestComputadoraInternet(unittest.TestCase):

    def setUp(self):

        self.o1 = ComputadoraInternet('red', '192.168.43.5', 'loc', 'AMD', 128, 2, '1/3/2010', '255.0.0.255', '8', '16')
        self.o2 = ComputadoraInternet('Red1', '192.168.43.1', 'Local', 'INTEL', 256, 4, '4/5/2010', '255.255.255.0', '9', '15')

    def test_mac(self):

        self.assertEqual(self.o1.mac, '255.0.0.255')
        self.assertFalse(self.o1.mac == '255.255.255.0')

        self.assertEqual(self.o2.mac, '255.255.255.0')
        self.assertFalse(self.o2.mac == '255.0.0.255')

    def test_hora_inicio(self):

        self.assertEqual(self.o1.hora_inicio, '8')
        self.assertFalse(self.o1.hora_inicio == '9')

        self.assertEqual(self.o2.hora_inicio, '9')
        self.assertFalse(self.o2.hora_inicio == '8')

    def test_hora_final(self):

        self.assertEqual(self.o1.hora_final, '16')
        self.assertFalse(self.o1.hora_final == '15')

        self.assertEqual(self.o2.hora_final, '15')
        self.assertFalse(self.o2.hora_final == '16')


