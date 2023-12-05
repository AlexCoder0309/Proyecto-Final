from modelo.facultad import Facultad
from modelo.proyecto import Proyecto
from vista.gestionar_proyectos import CRUDProyectos


class PresentadorProyectos:
    def __init__(self, facultad):
        self.__facultad = facultad

    def iniciar(self):
        self.__vista = CRUDProyectos(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for proyecto in self.__facultad.lista_proyectos():
            i = self.__vista.tabla_proyectos.rowCount()
            self.__vista.tabla_proyectos.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, proyecto.nombre_proyecto)
            self.__vista.agregar_elemento_tabla(i, 1, str(proyecto.es_internacional))
            self.__vista.agregar_elemento_tabla(i, 2, proyecto.linea_investigacion)
            self.__vista.agregar_elemento_tabla(i, 3, str(proyecto.tiempo_duracion_proyecto))
            self.__vista.agregar_elemento_tabla(i, 4, proyecto.jefe_proyecto)
        self.__vista.tabla_proyectos.resizeColumnsToContents()

    def insertar_proyecto(self):
        try:
            self.__vista.validar_controles()
            nombre_proyecto = self.__vista.valor_nombre_proyecto
            es_internacional = self.__vista.valor_es_internacional
            linea_investigacion = self.__vista.valor_linea_investigacion
            tiempo_duracion_proyecto = self.__vista.valor_tiempo_duracion_proyecto
            jefe_proyecto = self.__vista.valor_jefe_proyecto

            proyecto = Proyecto(nombre_proyecto, es_internacional, linea_investigacion, tiempo_duracion_proyecto, jefe_proyecto)
            self.__facultad.insertar_proyecto(proyecto)

            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_proyecto(self):
        try:
            ind = self.__vista.tabla_proyectos.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            nombre_proyecto_ant = self.__vista.tabla_proyectos.item(ind, 0).text()

            self.__vista.validar_controles()
            nombre_proyecto = self.__vista.valor_nombre_proyecto
            es_internacional = self.__vista.valor_es_internacional
            linea_investigacion = self.__vista.valor_linea_investigacion
            tiempo_duracion_proyecto = self.__vista.valor_tiempo_duracion_proyecto
            jefe_proyecto = self.__vista.valor_jefe_proyecto

            proyecto = Proyecto(nombre_proyecto, es_internacional, linea_investigacion, tiempo_duracion_proyecto, jefe_proyecto)
            self.__facultad.actualizar_proyecto(nombre_proyecto_ant, proyecto)

            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_proyecto(self):
        try:
            ind = self.__vista.tabla_proyectos.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            nombre_proyecto = self.__vista.tabla_proyectos.item(ind, 0).text()

            self.__facultad.eliminar_proyecto(nombre_proyecto)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla_proyectos(self):
        ind = self.__vista.tabla_proyectos.currentRow()
        if ind != -1:
            nombre_proyecto = self.__vista.tabla_proyectos.item(ind, 0).text()
            es_internacional = self.__vista.tabla_proyectos.item(ind, 1).text() == 'True'
            linea_investigacion = self.__vista.tabla_proyectos.item(ind, 2).text()
            tiempo_duracion_proyecto = self.__vista.tabla_proyectos.item(ind, 3).text()
            jefe_proyecto = self.__vista.tabla_proyectos.item(ind, 4).text()

            self.__vista.valor_nombre_proyecto = nombre_proyecto
            self.__vista.valor_es_internacional = es_internacional
            self.__vista.valor_linea_investigacion = linea_investigacion
            self.__vista.valor_tiempo_duracion_proyecto = tiempo_duracion_proyecto
            self.__vista.valor_jefe_proyecto = jefe_proyecto