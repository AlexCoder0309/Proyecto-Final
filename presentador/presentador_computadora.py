from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QDate
from modelo.computadora import Computadora
from vista.gestionar_computadoras import CRUDComputadoras

class PresentadorComputadoras:
    def __init__(self, facultad):
        self.__facultad = facultad

    def iniciar(self):
        self.__vista = CRUDComputadoras(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for computadora in self.__facultad.lista_computadoras():
            i = self.__vista.tabla_computadoras.rowCount()
            self.__vista.tabla_computadoras.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, computadora.nombre_red)
            self.__vista.agregar_elemento_tabla(i, 1, computadora.ip)
            self.__vista.agregar_elemento_tabla(i, 2, computadora.local)
            self.__vista.agregar_elemento_tabla(i, 3, computadora.microprocesador)
            self.__vista.agregar_elemento_tabla(i, 4, str(computadora.espacio_disco_duro))
            self.__vista.agregar_elemento_tabla(i, 5, str(computadora.ram_integrada))
            self.__vista.agregar_elemento_tabla(i, 6, computadora.fecha_adquisicion)
        self.__vista.tabla_computadoras.resizeColumnsToContents()

    def insertar_computadora(self):
        try:
            self.__vista.validar_controles()
            nombre_red = self.__vista.valor_nombre_red
            ip = self.__vista.valor_ip
            local = self.__vista.valor_local
            microprocesador = self.__vista.valor_microprocesador
            espacio_disco_duro = self.__vista.valor_espacio_disco_duro
            ram_integrada = self.__vista.valor_ram_integrada
            fecha_adquisicion = self.__vista.valor_fecha_adquisicion.toPyDate()
            fecha_adquisicion = fecha_adquisicion.strftime('%d-%m-%Y')
            nueva_computadora = Computadora(nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion)
            self.__facultad.insertar_computadora(nueva_computadora)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_computadora(self):
        try:
            ind = self.__vista.tabla_computadoras.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            nombre_red_ant = self.__vista.tabla_computadoras.item(ind, 0).text()

            self.__vista.validar_controles()
            nombre_red = self.__vista.valor_nombre_red
            ip = self.__vista.valor_ip
            local = self.__vista.valor_local
            microprocesador = self.__vista.valor_microprocesador
            espacio_disco_duro = self.__vista.valor_espacio_disco_duro
            ram_integrada = self.__vista.valor_ram_integrada
            fecha_adquisicion = self.__vista.valor_fecha_adquisicion.toPyDate()
            fecha_adquisicion = fecha_adquisicion.strftime('%d-%m-%Y')
            computadora = Computadora(nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion)
            self.__facultad.actualizar_computadora(nombre_red_ant, computadora)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_computadora(self):
        try:
            ind = self.__vista.tabla_computadoras.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            nombre_red = self.__vista.tabla_computadoras.item(ind, 0).text()

            self.__facultad.eliminar_computadora(nombre_red)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla_computadora(self):
        ind = self.__vista.tabla_computadoras.currentRow()
        if ind != -1:
            nombre_red = self.__vista.tabla_computadoras.item(ind, 0).text()
            ip = self.__vista.tabla_computadoras.item(ind, 1).text()
            local = self.__vista.tabla_computadoras.item(ind, 2).text()
            microprocesador = self.__vista.tabla_computadoras.item(ind, 3).text()
            espacio_disco_duro = self.__vista.tabla_computadoras.item(ind, 4).text()
            ram_integrada = self.__vista.tabla_computadoras.item(ind, 5).text()
            fecha_adquisicion = self.__vista.tabla_computadoras.item(ind, 6).text()

            self.__vista.valor_nombre_red = nombre_red
            self.__vista.valor_ip = ip
            self.__vista.valor_local = local
            self.__vista.valor_microprocesador = microprocesador
            self.__vista.valor_espacio_disco_duro = espacio_disco_duro
            self.__vista.valor_ram_integrada = ram_integrada
            self.__vista.valor_fecha_adquisicion = QDate.fromString(fecha_adquisicion, "yyyy-MM-dd")
