from modelo.facultad import Facultad
from modelo.local import Local
from vista.gestionar_locales import CRUDLocales  


class PresentadorLocales:
    def __init__(self, facu):
        self.__facultad = facu

    def iniciar(self):
        self.__vista = CRUDLocales(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for local in self.__facultad.lista_locales():
            i = self.__vista.tabla_locales.rowCount()
            self.__vista.tabla_locales.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, local.nombre_local)
            self.__vista.agregar_elemento_tabla(i, 1, local.tipo_local)
            self.__vista.agregar_elemento_tabla(i, 2, str(local.es_docente))
            self.__vista.agregar_elemento_tabla(i, 3, local.responsable)
        self.__vista.tabla_locales.resizeColumnsToContents()

    def insertar_local(self):
        try:
            self.__vista.validar_controles()
            nombre_local = self.__vista.valor_nombre_local
            tipo_local = self.__vista.valor_tipo_local
            es_docente = self.__vista.valor_es_docente
            responsable = self.__vista.valor_responsable
            local = Local(nombre_local, tipo_local, es_docente, responsable)
            self.__facultad.insertar_local(local)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_local(self):
        try:
            ind = self.__vista.tabla_locales.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            nombre_local_ant = self.__vista.tabla_locales.item(ind, 0).text()

            self.__vista.validar_controles()
            nombre_local = self.__vista.valor_nombre_local
            tipo_local = self.__vista.valor_tipo_local
            es_docente = self.__vista.valor_es_docente
            responsable = self.__vista.valor_responsable
            local = Local(nombre_local, tipo_local, es_docente, responsable)
            self.__facultad.actualizar_local(nombre_local_ant, local)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_local(self):
        try:
            ind = self.__vista.tabla_locales.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            nombre_local = self.__vista.tabla_locales.item(ind, 0).text()

            self.__facultad.eliminar_local(nombre_local)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla_locales(self):
        ind = self.__vista.tabla_locales.currentRow()
        if ind != -1:
            nombre_local = self.__vista.tabla_locales.item(ind, 0).text()
            tipo_local = self.__vista.tabla_locales.item(ind, 1).text()
            es_docente = self.__vista.tabla_locales.item(ind, 2).text() == 'True'
            responsable = self.__vista.tabla_locales.item(ind, 3).text()
            self.__vista.valor_nombre_local = nombre_local
            self.__vista.valor_tipo_local = tipo_local
            self.__vista.valor_es_docente = es_docente
            self.__vista.valor_responsable = responsable