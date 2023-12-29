from PyQt5.QtWidgets import QMessageBox
from modelo.computadora import Computadora
from vista.obtener_computadoras_responsable import ObtenerComputadorasResponsable

class PresentadorObtenerComputadorasResponsable:
    def __init__(self, facultad):
        self.__facultad = facultad

    def iniciar(self):
        self.__vista = ObtenerComputadorasResponsable(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        nombre_responsable = self.__vista.valor_responsable

        if not nombre_responsable:
            self.__vista.valor_respuesta = 'No hay computadoras asignadas a ningún responsable'
            return

        computadoras_docentes = self.__facultad.obtener_computadoras_docentes_con_internet_por_responsable(nombre_responsable)

        if computadoras_docentes:
            for computadora in computadoras_docentes:
                i = self.__vista.tabla_computadoras.rowCount()
                self.__vista.tabla_computadoras.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, computadora.nombre_red)
                self.__vista.agregar_elemento_tabla(i, 1, computadora.ip)
                self.__vista.agregar_elemento_tabla(i, 2, computadora.local)
                self.__vista.agregar_elemento_tabla(i, 3, computadora.microprocesador)
                self.__vista.agregar_elemento_tabla(i, 4, computadora.espacio_disco_duro)
                self.__vista.agregar_elemento_tabla(i, 5, computadora.ram_integrada)
                self.__vista.agregar_elemento_tabla(i, 6, computadora.fecha_adquisicion)
                self.__vista.agregar_elemento_tabla(i, 7, computadora.mac)
                self.__vista.agregar_elemento_tabla(i, 8, computadora.hora_inicio)
                self.__vista.agregar_elemento_tabla(i, 9, computadora.hora_final)
            self.__vista.tabla_computadoras.resizeColumnsToContents()
            self.__vista.valor_respuesta = ''
        else:
            self.__vista.restablecer_controles()
            self.__vista.valor_respuesta = f'No hay computadoras asignadas al responsable {nombre_responsable}'
