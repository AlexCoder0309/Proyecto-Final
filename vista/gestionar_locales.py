from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic

class CRUDLocales(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/gest_locales.ui', self)
        self.minimumSize()

        self.btn_insertar.clicked.connect(self.__presentador.insertar_local)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_local)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_local)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_locales.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla_locales)

        self.tabla_locales.setColumnCount(4)
        self.tabla_locales.setHorizontalHeaderLabels(['Nombre Local', 'Tipo Local', 'Es Docente', 'Responsable'])
        self.tabla_locales.resizeColumnsToContents()

    @property
    def valor_nombre_local(self):
        return self.txt_nombre_local.text().strip()

    @valor_nombre_local.setter
    def valor_nombre_local(self, value):
        self.txt_nombre_local.setText(value)

    @property
    def valor_tipo_local(self):
        if self.rbtn_aula.isChecked():
            tipo_local = 'Aula'
        elif self.rbtn_departamento.isChecked():
            tipo_local = 'Departamento'
        elif self.rbtn_laboratorio.isChecked():
            tipo_local = 'Laboratorio'
        elif self.rbtn_oficina.isChecked():
            tipo_local = 'Oficina'
        else:
            tipo_local = ''
        return tipo_local

    @valor_tipo_local.setter
    def valor_tipo_local(self, value):
        if value == 'Aula':
            self.rbtn_aula.setChecked(True)
        elif value == 'Departamento':
            self.rbtn_departamento.setChecked(True)
        elif value == 'Laboratorio':
            self.rbtn_laboratorio.setChecked(True)
        elif value == 'Oficina':
            self.rbtn_oficina.setChecked(True)

    @property
    def valor_es_docente(self):
        return "Si" if self.rbtn_si.isChecked() else "No"

    @valor_es_docente.setter
    def valor_es_docente(self, value):
        if isinstance(value, bool):
            if value:
                self.rbtn_si.setChecked(True)
            else:
                self.rbtn_no.setChecked(True)
        elif isinstance(value, str):
            if value.lower() == "si":
                self.rbtn_si.setChecked(True)
            elif value.lower() == "no":
                self.rbtn_no.setChecked(True)



    @property
    def valor_responsable(self):
        return self.txt_responsable.text().strip()

    @valor_responsable.setter
    def valor_responsable(self, value):
        self.txt_responsable.setText(value)


    def validar_controles(self):
        msg = 'Es necesario llenar todos los campos para poder insertar los datos en la tabla'
        if len(self.valor_nombre_local) == 0:
            raise Exception(msg)
        if not isinstance(self.valor_tipo_local, str) or len(self.valor_tipo_local) == 0:
            raise Exception("El tipo de local debe ser un texto no vacío.")
        if not (self.valor_responsable.isalpha()) or len(self.valor_responsable) == 0:
            raise Exception("El responsable debe ser un texto no vacío.")
        if not (self.rbtn_si.isChecked() or self.rbtn_no.isChecked()):
            raise Exception("Selecciona 'Si' o 'No' en la opción Es Docente.")

        
        
    def restablecer_controles(self):
        self.valor_nombre_local = ''
        self.valor_tipo_local = ''
        self.valor_es_docente = False
        self.valor_responsable = ''

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_locales.rowCount() > 0:
            self.tabla_locales.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_locales.setItem(fila, columna, QTableWidgetItem(texto))

