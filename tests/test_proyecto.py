import unittest
from modelo.proyecto import Proyecto

class TestProyecto(unittest.TestCase):

    def setUp(self):

        self.o1 = Proyecto('Vaca', True, 'Cientifica', 12, 'Godofredo')
        self.o2 = Proyecto('Informatizacion', False, 'Social', 6, 'Yasmany')

    def test_nombre_proyecto(self):

        self.assertEqual(self.o1.nombre_proyecto, 'Vaca')
        self.assertFalse(self.o1.nombre_proyecto == 'Informatizacion')

        self.assertEqual(self.o2.nombre_proyecto, 'Informatizacion')
        self.assertFalse(self.o2.nombre_proyecto == 'Vaca')

    def test_es_inernacional(self):

        self.assertTrue(self.o1.es_internacional)
        self.assertFalse(self.o1.es_internacional == False)

        self.assertFalse(self.o2.es_internacional)
        self.assertFalse(self.o2.es_internacional == True)

    def test_linea_investigacion(self):

        self.assertEqual(self.o1.linea_investigacion, 'Cientifica')
        self.assertFalse(self.o1.linea_investigacion == 'Social')

        self.assertEqual(self.o2.linea_investigacion, 'Social')
        self.assertFalse(self.o2.linea_investigacion == 'Cientifica')

    def test_tiempo_duracion_proyecto(self):

        self.assertEqual(self.o1.tiempo_duracion_proyecto, 12)
        self.assertFalse(self.o1.tiempo_duracion_proyecto == 24)

        self.assertEqual(self.o2.tiempo_duracion_proyecto, 6)
        self.assertFalse(self.o2.tiempo_duracion_proyecto == 12)

    def test_jefe_proyecto(self):

        self.assertEqual(self.o1.jefe_proyecto, 'Godofredo')
        self.assertFalse(self.o1.jefe_proyecto == 'Yasmany')

        self.assertEqual(self.o2.jefe_proyecto, 'Yasmany')
        self.assertFalse(self.o2.jefe_proyecto == 'Godofredo')

