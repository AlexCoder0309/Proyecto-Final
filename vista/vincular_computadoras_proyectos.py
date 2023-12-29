from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic



class VincularComputadorasProyectos(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/vincu_compu_proyectos.ui', self) 
        self.setMinimumSize(800, 600)

        self.btn_vincular.clicked.connect(self.__presentador.insertar_datos)
        self.btn_desvincular.clicked.connect(self.__presentador.desvincular_computadora_proyecto)


        self.tabla_vinculacion.setColumnCount(3)
        self.tabla_vinculacion.setHorizontalHeaderLabels(['Nombre Proyecto', 'IP Computadora', 'Lista de Usuarios'])
        self.tabla_vinculacion.resizeColumnsToContents()

    @property
    def valor_nombre_proyecto(self):
        return self.txt_nombre_proyecto.text().strip()

    @valor_nombre_proyecto.setter
    def valor_nombre_proyecto(self, value):
        self.txt_nombre_proyecto.setText(value)

    @property
    def valor_ip(self):
        return self.txt_ip.text().strip()

    @valor_ip.setter
    def valor_ip(self, value):
        self.txt_ip.setText(value)

    @property
    def valor_usuarios(self):
        return self.txt_usuarios.text().strip()

    @valor_usuarios.setter
    def valor_usuarios(self, value):
        self.txt_usuarios.setText(value)
        
    @property
    def valor_respuesta(self):
        return self.txt_respuesta.text().strip()

    @valor_respuesta.setter
    def valor_respuesta(self, value):
        self.txt_respuesta.setText(value)


    def restablecer_controles(self):
        self.valor_nombre_proyecto = ''
        self.valor_ip = ''
        self.valor_usuarios = ''
        self.valor_respuesta = ''

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'

        if len(self.valor_nombre_proyecto) == 0:
            raise Exception(msg.format('nombre proyecto'))

        if len(self.valor_ip) == 0:
            raise Exception(msg.format('IP'))

        if len(self.valor_usuarios) == 0:
            raise Exception(msg.format('usuarios'))


    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_vinculacion.rowCount() > 0:
            self.tabla_vinculacion.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_vinculacion.setItem(fila, columna, QTableWidgetItem(texto))
