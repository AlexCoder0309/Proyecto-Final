from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic
from datetime import datetime
import re
import socket

class CRUDComputadorasInternet(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/gest_compu_con_internet.ui', self)
        self.setMinimumSize(1150, 750)

        self.btn_insertar.clicked.connect(self.__presentador.insertar_computadora_internet)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_computadora_internet)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_computadora_internet)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_computadoras_internet.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla_computadora_internet)


        self.tabla_computadoras_internet.setColumnCount(10)
        self.tabla_computadoras_internet.setHorizontalHeaderLabels(['Nombre Red', 'IP', 'Local', 'Microprocesador', 'Espacio Disco Duro', 'RAM Integrada', 'Fecha', 'MAC', 'Hora Inicio', 'Hora Final'])
        self.tabla_computadoras_internet.resizeColumnsToContents()

    @property
    def valor_nombre_red(self):
        return self.txt_nombre_red.text().strip()

    @valor_nombre_red.setter
    def valor_nombre_red(self, value):
        self.txt_nombre_red.setText(value)

    @property
    def valor_ip(self):
        return self.txt_ip.text().strip()

    @valor_ip.setter
    def valor_ip(self, value):
        self.txt_ip.setText(value)

    @property
    def valor_local(self):
        return self.txt_local.text().strip()


    @valor_local.setter
    def valor_local(self, value):
        self.txt_local.setText(value)

    @property
    def valor_microprocesador(self):
        if self.rbtn_amd.isChecked():
            return "AMD"
        elif self.rbtn_intel.isChecked():
            return "Intel"
        else:
            return ""

    @valor_microprocesador.setter
    def valor_microprocesador(self, value):
        if value.lower() == "amd":
            self.rbtn_amd.setChecked(True)
        elif value.lower() == "intel":
            self.rbtn_intel.setChecked(True)
        else:
            pass

    @property
    def valor_espacio_disco_duro(self):
        return self.txt_espacio_disco_duro.text().strip()
        
    @valor_espacio_disco_duro.setter
    def valor_espacio_disco_duro(self, value):
        self.txt_espacio_disco_duro.setText(value)

    @property
    def valor_ram_integrada(self):
        return self.txt_ram_integrada.text().strip()


    @valor_ram_integrada.setter
    def valor_ram_integrada(self, value):
        self.txt_ram_integrada.setText(value)
        
    @property
    def valor_fecha_adquisicion(self):
        return self.date_fecha_adquisicion.date()

    @valor_fecha_adquisicion.setter
    def valor_fecha_adquisicion(self, value):
        if isinstance(value, str):
            value = QDate.fromString(value, "dd-MM-yyyy")
        self.date_fecha_adquisicion.setDate(value)
        
    @property
    def valor_mac(self):
        return self.txt_mac.text().strip()

    @valor_mac.setter
    def valor_mac(self, value):
        self.txt_mac.setText(value)

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

        if len(self.valor_nombre_red) == 0:
            raise Exception(msg.format('nombre de red'))

        if len(self.valor_ip) == 0:
            raise Exception(msg.format('IP'))

        if len(self.valor_local) == 0:
            raise Exception(msg.format('local'))

        if len(self.valor_microprocesador) == 0:
            raise Exception(msg.format('microprocesador'))

        if len(self.valor_mac) == 0:
            raise Exception(msg.format('MAC'))

        if not self.txt_espacio_disco_duro.text().strip().isdigit():
            raise Exception('La capacidad de disco debe ser un número entero.')

        if not self.txt_ram_integrada.text().strip().isdigit():
            raise Exception('La capacidad de RAM debe ser un número entero.')

        espacio_disco_duro = int(self.valor_espacio_disco_duro)
        if espacio_disco_duro <= 0:
            raise Exception('La capacidad de disco debe ser un número mayor que 0.')

        ram_integrada = int(self.valor_ram_integrada)
        if ram_integrada <= 0:
            raise Exception('La capacidad de RAM debe ser un número mayor que 0.')

        if not self.rbtn_amd.isChecked() and not self.rbtn_intel.isChecked():
            raise Exception('Se debe seleccionar un fabricante de microprocesador.')

        if len(self.date_fecha_adquisicion.text()) == 0:
            raise Exception('La fecha de adquisición es obligatoria.')
        
        if self.valor_fecha_adquisicion > datetime.today():
            raise Exception('La fecha de adquisición no puede ser mayor que la fecha actual.')
        if not re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", self.valor_mac):
            raise Exception('La dirección MAC no es correcta')
        
        try:
            socket.inet_pton(socket.AF_INET, self.valor_ip)
        except socket.error:
            raise Exception('La dirección IP es incorrecta')

    def restablecer_controles(self):
        self.valor_nombre_red = ''
        self.valor_ip = ''
        self.valor_local = ''
        self.valor_microprocesador = ''
        self.valor_espacio_disco_duro = ''
        self.valor_ram_integrada = ''
        self.valor_fecha_adquisicion = ''
        self.valor_mac = ''
        self.valor_hora_inicio = ''
        self.valor_hora_final = ''

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_computadoras_internet.rowCount() > 0:
            self.tabla_computadoras_internet.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_computadoras_internet.setItem(fila, columna, QTableWidgetItem(texto))
