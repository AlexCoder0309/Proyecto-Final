from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QDate
from modelo.computadora import Computadora
from vista.vincular_computadoras_proyectos import VincularComputadorasProyectos

class PresentadorVincularComputadorasProyectos:
    def __init__(self, facultad):
        self.__facultad = facultad

    def iniciar(self):
        self.__vista = VincularComputadorasProyectos(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
            nombre_proyecto = self.__vista.valor_nombre_proyecto
            ip = self.__vista.valor_ip
            usuarios = self.__vista.valor_usuarios
            try:
                self.__vista.validar_controles()
                computadoras_vinculadas = self.__facultad.vincular_computadoras(nombre_proyecto, ip, usuarios)
                if computadoras_vinculadas:
                    for computadora in computadoras_vinculadas:
                        if not self.computadora_presente_en_tabla(computadora):
                            i = self.__vista.tabla_vinculacion.rowCount()
                            self.__vista.tabla_vinculacion.insertRow(i)
                            self.__vista.agregar_elemento_tabla(i, 0, computadora[0])
                            self.__vista.agregar_elemento_tabla(i, 1, computadora[1])
                            self.__vista.agregar_elemento_tabla(i, 2, computadora[2])
                        self.__vista.restablecer_controles()
                else:
                    self.__vista.valor_respuesta = "No se ha encontrado ninguna computadora con esa IP o Proyecto con ese nombre"
            except Exception as e:
                self.__vista.mostrar_error(e.args[0])



    def computadora_presente_en_tabla(self, computadora):
        for row in range(self.__vista.tabla_vinculacion.rowCount()):
            if (
                self.__vista.tabla_vinculacion.item(row, 0).text() == computadora[0] and
                self.__vista.tabla_vinculacion.item(row, 1).text() == computadora[1] and
                self.__vista.tabla_vinculacion.item(row, 2).text() == computadora[2]
            ):
                return True
        return False
    
    def desvincular_computadora_proyecto(self):
        nombre_proyecto = self.__vista.valor_nombre_proyecto
        ip = self.__vista.valor_ip

        self.__facultad.desvincular_computadoras(nombre_proyecto, ip)

        self.eliminar_fila_tabla(nombre_proyecto, ip)
        
        
    def eliminar_fila_tabla(self, nombre_proyecto, ip):
        for i in range(self.__vista.tabla_vinculacion.rowCount()):
            if (
                self.__vista.tabla_vinculacion.item(i, 0).text() == nombre_proyecto and
                self.__vista.tabla_vinculacion.item(i, 1).text() == ip
            ):
                self.__vista.tabla_vinculacion.removeRow(i)
                break