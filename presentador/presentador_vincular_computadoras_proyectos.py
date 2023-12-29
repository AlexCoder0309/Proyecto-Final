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
        self.__vista.vaciar_tabla()
        for computadora in self.__facultad.lista_vinculadas():
                i = self.__vista.tabla_vinculacion.rowCount()
                self.__vista.tabla_vinculacion.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, computadora[0])
                self.__vista.agregar_elemento_tabla(i, 1, computadora[1])
                self.__vista.agregar_elemento_tabla(i, 2, computadora[2])

                    
            
                 
    def insertar_datos(self):
        try:
            self.__vista.validar_controles()
            nombre_proyecto = self.__vista.valor_nombre_proyecto
            ip = self.__vista.valor_ip
            usuarios = self.__vista.valor_usuarios
            computadoras_vinculadas = self.__facultad.vincular_computadoras(nombre_proyecto, ip, usuarios)
            if computadoras_vinculadas is None:
                self.__vista.valor_respuesta = 'No se encontró ningún proyecto con ese nombre o computadora con esa dirección IP'
            else:
                self.cargar_datos()
                self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def desvincular_computadora_proyecto(self):
        try:
            ind = self.__vista.tabla_vinculacion.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para desvincularla.')
            nombre_proyecto = self.__vista.tabla_vinculacion.item(ind, 0).text()
            ip = self.__vista.tabla_vinculacion.item(ind, 1).text()
            self.__facultad.desvincular_computadoras(nombre_proyecto, ip)
            self.cargar_datos()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
            
