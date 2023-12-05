from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDateTime
from PyQt5 import uic


class PorcentajeComputadorasInternet(QDialog):
    def __init__(self, presentador):
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('vista/ui/porc_compu_con_internet.ui', self)  
        self.setMinimumSize(800, 600)
        self.btn_calcular.clicked.connect(self.__presentador.calcular_porcentaje)

    @property
    def valor_respuesta(self):
        return self.respuesta.text().strip()

    @valor_respuesta.setter
    def valor_respuesta(self, value):
        self.respuesta.setText(value)

        
    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_ip) == 0:
            raise ValueError(msg.format('IP'))
        
    def restablecer_controles(self):
        self.valor_respuesta = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
