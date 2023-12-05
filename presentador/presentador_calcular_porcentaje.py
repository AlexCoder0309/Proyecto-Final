from modelo.facultad import Facultad
from vista.porcentaje_computadoras_internet import PorcentajeComputadorasInternet

class PresentadorPorcentajeComputadorasInternet:
    def __init__(self, facu):
        self.__facultad = facu

    def iniciar(self):
        self.__vista = PorcentajeComputadorasInternet(self)
        self.__vista.show()

    def calcular_porcentaje(self):
        try:
            asignacion = self.__facultad.porcentaje_computadoras_con_navegacion()
            if asignacion:
                self.__vista.valor_respuesta = 'El porcentaje de computadoras con navegación es de: {}%'.format(asignacion)
            else:
                self.__vista.valor_respuesta = 'No se encontró ninguna computadora con navegación'
        except ValueError as e:
            self.__vista.mostrar_error(str(e))
        except Exception as e:
            self.__vista.mostrar_error('Error desconocido: {}'.format(str(e)))
