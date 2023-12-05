from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic


class PorCientoDesgaste(QDialog):
    def __init__(self, presentador):
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('vista/ui/calc_desgaste.ui', self)  
        self.setMinimumSize(800, 600)
        self.btn_calcular.clicked.connect(self.__presentador.calcular_desgaste)

    @property
    def valor_ip(self):
        return self.txt_ip.text().strip()

    @valor_ip.setter
    def valor_ip(self, value):
        self.txt_ip.setText(value)

    @property
    def valor_porcentaje(self):
        return self.porcentaje.text().strip()

    @valor_porcentaje.setter
    def valor_porcentaje(self, value):
        self.porcentaje.setText(value)
        
    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_ip) == 0:
            raise ValueError(msg.format('IP'))
        
    def restablecer_controles(self):
        self.valor_ip = ''
        self.valor_porcentaje = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
