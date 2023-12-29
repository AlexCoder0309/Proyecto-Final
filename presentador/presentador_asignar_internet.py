from modelo.facultad import Facultad
from vista.asignar_internet import AsignarInternet

class PresentadorAsignarInternet:
    def __init__(self, facu):
        self.__facultad = facu

    def iniciar(self):
        self.__vista = AsignarInternet(self)
        self.__vista.show()

    def asignar_internet(self):
        try:
            self.__vista.validar_controles()
            ip = self.__vista.valor_ip
            mac = self.__vista.valor_mac
            hora_inicio = self.__vista.valor_hora_inicio
            hora_final = self.__vista.valor_hora_final
            asignacion = self.__facultad.asignar_internet(ip, mac, hora_inicio, hora_final)  
            if asignacion:
                self.__vista.valor_respuesta = 'Se le asignó internet a la computadora correctamente'
            else:
                self.__vista.valor_respuesta = 'No se encontró ninguna computadora sin internet con esa dirección IP'
        except ValueError as e:
            self.__vista.mostrar_error(str(e))
        except Exception as e:
            self.__vista.mostrar_error('Error desconocido: {}'.format(str(e)))
