from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QDialog
from PyQt5 import uic

class CRUDProyectos(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('vista/ui/gest_proyectos.ui', self)
        self.minimumSize()


        self.btn_insertar.clicked.connect(self.__presentador.insertar_proyecto)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_proyecto)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_proyecto)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_proyectos.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla_proyectos)


        self.tabla_proyectos.setColumnCount(5)
        self.tabla_proyectos.setHorizontalHeaderLabels(['Nombre Proyecto', 'Internacional', 'Línea Investigación', 'Tiempo Duración', 'Jefe Proyecto'])
        self.tabla_proyectos.resizeColumnsToContents()

    @property
    def valor_nombre_proyecto(self):
        return self.txt_nombre_proyecto.text().strip()

    @valor_nombre_proyecto.setter
    def valor_nombre_proyecto(self, value):
        self.txt_nombre_proyecto.setText(value)

    @property
    def valor_es_internacional(self):
        return "Si" if self.rbtn_si.isChecked() else "No"

    @valor_es_internacional.setter
    def valor_es_internacional(self, value):
        if isinstance(value, bool):
            self.rbtn_si.setChecked(value)
            self.rbtn_no.setChecked(not value)
        elif isinstance(value, str):
            if value.lower() == "si":
                self.rbtn_si.setChecked(True)
                self.rbtn_no.setChecked(False)
            elif value.lower() == "no":
                self.rbtn_si.setChecked(False)
                self.rbtn_no.setChecked(True)
            else:
                raise ValueError("Invalid value for valor_es_internacional. Use 'Si' or 'No'.")
        else:
            raise ValueError("Invalid value type for valor_es_internacional. Use bool or str.")

    @property
    def valor_linea_investigacion(self):
        return self.txt_linea_investigacion.text().strip()

    @valor_linea_investigacion.setter
    def valor_linea_investigacion(self, value):
        self.txt_linea_investigacion.setText(value)

    @property
    def valor_tiempo_duracion_proyecto(self):
        return self.txt_tiempo_duracion.text().strip()

    @valor_tiempo_duracion_proyecto.setter
    def valor_tiempo_duracion_proyecto(self, value):
        self.txt_tiempo_duracion.setText(value)

    @property
    def valor_jefe_proyecto(self):
        return self.txt_jefe_proyecto.text().strip()

    @valor_jefe_proyecto.setter
    def valor_jefe_proyecto(self, value):
        self.txt_jefe_proyecto.setText(value)

    def validar_controles(self):
        msg = 'Es necesario llenar todos los campos para poder insertar los datos en la tabla'
        if len(self.valor_nombre_proyecto) == 0:
            raise Exception(msg)
        if len(self.valor_linea_investigacion) == 0:
            raise Exception(msg)
        try:
            tiempo_duracion = int(self.valor_tiempo_duracion_proyecto)
            if tiempo_duracion <= 0:
                raise ValueError("El tiempo de duración debe ser un entero positivo.")
        except ValueError:
            raise ValueError("El tiempo de duración debe ser un número entero.")

        if len(self.valor_jefe_proyecto) == 0:
            raise Exception(msg)
        if not (self.rbtn_si.isChecked() or self.rbtn_no.isChecked()):
            raise Exception(msg)
        
    def restablecer_controles(self):
        self.valor_nombre_proyecto = ''
        self.valor_linea_investigacion = ''
        self.valor_tiempo_duracion_proyecto = ''
        self.valor_jefe_proyecto = ''

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_proyectos.rowCount() > 0:
            self.tabla_proyectos.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_proyectos.setItem(fila, columna, QTableWidgetItem(texto))