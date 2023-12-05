from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic

class CRUDComputadorasInternet(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/gest_compu_con_internet.ui', self)
        self.setMinimumSize(1250, 850)

        self.btn_insertar.clicked.connect(self.__presentador.insertar_computadora_internet)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_computadora_internet)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_computadora_internet)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_computadoras_internet.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla_computadora_internet)


        self.tabla_computadoras_internet.setColumnCount(10)
        self.tabla_computadoras_internet.setHorizontalHeaderLabels(['Nombre Red', 'IP', 'Local', 'Microprocesador', 'Espacio Disco Duro', 'RAM Integrada', 'Fecha Adquisición', 'MAC', 'Hora Inicio', 'Hora Final'])
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
        return self.date_fecha_adquisicion.dateTime().toString("dd-MM-yyyy")

    @valor_fecha_adquisicion.setter
    def valor_fecha_adquisicion(self, value):
        datetime = QDateTime.fromString(value, "dd-MM-yyyy")
        self.date_fecha_adquisicion.setDateTime(datetime)
        
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

    def validar_horas(self):
            horas_iniciales, minutos_iniciales = self.valor_hora_inicio.split(":")
            horas_iniciales = float(horas_iniciales)
            minutos_iniciales = float(minutos_iniciales)
            minutos_iniciales /= 60
            horas_finales, minutos_finales = self.valor_hora_final.split(":")
            horas_finales = float(horas_finales)
            minutos_finales = float(minutos_finales)
            minutos_finales /= 60
            hora_terminacion = horas_finales + minutos_finales
            horas_iniciacion = horas_iniciales + minutos_iniciales 
            return horas_iniciacion <= hora_terminacion

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
        
        if not self.validar_horas():
            raise Exception('La hora de inicio no puede ser mayor que la hora final.')

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
