import unittest
from modelo.local import Local


class TestLocal(unittest.TestCase):

    def setUp(self):

        self.o1 = Local('Red1', 'Algo', True, 'Juan')
        self.o2 = Local('Loc1', 'Algo', False, 'Maria')

    def test_nombre_local(self):

        self.assertEqual(self.o1.nombre_local, 'Red1')
        self.assertFalse(self.o1.nombre_local == 'Loc1')

        self.assertEqual(self.o2.nombre_local, 'Loc1')
        self.assertFalse(self.o2.nombre_local == 'Red1')

    def test_tipo_local(self):

        self.assertEqual(self.o1.tipo_local, 'Algo')
        self.assertFalse(self.o1.tipo_local == 'ALgo2')

        self.assertEqual(self.o2.tipo_local, 'Algo')
        self.assertFalse(self.o2.tipo_local == 'Algo3')

    def test_es_docente(self):

        self.assertTrue(self.o1.es_docente)
        self.assertFalse(self.o1.es_docente == False)

        self.assertFalse(self.o2.es_docente)
        self.assertFalse(self.o2.es_docente == True)

    def test_responsable(self):

        self.assertEqual(self.o1.responsable, 'Juan')
        self.assertFalse(self.o1.responsable == 'Maria')

        self.assertEqual(self.o2.responsable, 'Maria')
        self.assertFalse(self.o2.responsable == 'Juan')

