from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDateTime
from PyQt5 import uic


class AsignarInternet(QDialog):
    def __init__(self, presentador):
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('vista/ui/asign_internet.ui', self)  
        self.setMinimumSize(800, 600)
        self.btn_asignar.clicked.connect(self.__presentador.asignar_internet)

    @property
    def valor_ip(self):
        return self.txt_ip.text().strip()

    @valor_ip.setter
    def valor_ip(self, value):
        self.txt_ip.setText(value)

    @property
    def valor_mac(self):
        return self.txt_mac.text().strip()

    @valor_mac.setter
    def valor_mac(self, value):
        self.txt_mac.setText(value)
        
    @property
    def valor_respuesta(self):
        return self.respuesta.text().strip()

    @valor_mac.setter
    def valor_respuesta(self, value):
        self.respuesta.setText(value)
        
    @property
    def valor_hora_inicio(self):
        return self.date_hora_inicio.dateTime().toString("hh:mm")

    @valor_hora_inicio.setter
    def valor_hora_inicio(self, value):
        datetime = QDateTime.fromString(value, "hh:mm")
        self.date_hora_inicio.setDateTime(datetime)

    @property
    def valor_hora_final(self):
        return self.date_hora_final.dateTime().toString("hh:mm")

    @valor_hora_final.setter
    def valor_hora_final(self, value):
        datetime = QDateTime.fromString(value, "hh:mm")
        self.date_hora_final.setDateTime(datetime)
        
    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_ip) == 0:
            raise ValueError(msg.format('IP'))
        
    def restablecer_controles(self):
        self.valor_ip = ''
        self.valor_mac = ''
        self.valor_respuesta = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
