from modelo.facultad import Facultad
from vista.calcular_desgaste import PorCientoDesgaste

class PresentadorPorCientoDesgaste:
    def __init__(self, facu):
        self.__facultad = facu

    def iniciar(self):
        self.__vista = PorCientoDesgaste(self)
        self.__vista.show()

    def calcular_desgaste(self):
        try:
            self.__vista.validar_controles()
            ip = self.__vista.valor_ip
            desgaste = self.__facultad.calcular_desgaste(ip)  
            if desgaste == None:
                self.__vista.valor_porcentaje = 'No se ha encontrado ninguna computadora con esa dirección IP'
            else:
                msg = 'El porcentaje de desgaste es de: {}%'.format(desgaste)
                self.__vista.valor_porcentaje = msg
        except Exception as e:
            self.__vista.mostrar_error('Error desconocido: {}'.format(str(e)))
