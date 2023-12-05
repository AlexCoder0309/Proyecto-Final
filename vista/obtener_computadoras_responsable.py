from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic
from PyQt5.QtCore import QDate, QDateTime


class ObtenerComputadorasResponsable(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/obt_compu_por_responsable.ui', self) 
        self.setMinimumSize(800, 600)


        self.btn_obtener.clicked.connect(self.__presentador.cargar_datos)
        self.tabla_computadoras.setColumnCount(10)
        self.tabla_computadoras.setHorizontalHeaderLabels(['Nombre Red', 'IP', 'Local', 'Microprocesador', 'Espacio Disco Duro', 'RAM Integrada', 'Fecha Adquisición', 'MAC', 'Hora Inicio', 'Hora Final'])
        self.tabla_computadoras.resizeColumnsToContents()

    @property
    def valor_responsable(self):
        return self.txt_responsable.text().strip()

    @valor_responsable.setter
    def valor_responsable(self, value):
        self.txt_responsable.setText(value)

    @property
    def valor_respuesta(self):
        return self.respuesta.text().strip()

    @valor_respuesta.setter
    def valor_respuesta(self, value):
        self.respuesta.setText(value)
 
    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'

        if len(self.valor_responsable) == 0:
            raise Exception(msg.format('valor_responsable'))


    def restablecer_controles(self):
        self.valor_responsable = ''
        self.valor_respuesta = ''


    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_computadoras.rowCount() > 0:
            self.tabla_computadoras.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_computadoras.setItem(fila, columna, QTableWidgetItem(texto))
