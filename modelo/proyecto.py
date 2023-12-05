class Proyecto:
    def __init__(self, nombre_proyecto, es_internacional, linea_investigacion,tiempo_duracion_proyecto, jefe_proyecto):
        self.__nombre_proyecto = nombre_proyecto
        self.__es_internacional = es_internacional
        self.__linea_investigacion = linea_investigacion
        self.__tiempo_duracion_proyecto = tiempo_duracion_proyecto
        self.__jefe_proyecto = jefe_proyecto


    @property
    def nombre_proyecto(self):
        return self.__nombre_proyecto

    @nombre_proyecto.setter
    def nombre_proyecto(self, valor):
        self.__nombre_proyecto = valor

    @property
    def es_internacional(self):
        return self.__es_internacional

    @es_internacional.setter
    def es_internacional(self, valor):
        self.__es_internacional = valor

    @property
    def linea_investigacion(self):
        return self.__linea_investigacion

    @linea_investigacion.setter
    def linea_investigacion(self, valor):
        self.__linea_investigacion = valor
        
    @property
    def tiempo_duracion_proyecto(self):
        return self.__tiempo_duracion_proyecto

    @tiempo_duracion_proyecto.setter
    def tiempo_duracion_proyecto(self, valor):
        self.__tiempo_duracion_proyecto = valor

    @property
    def jefe_proyecto(self):
        return self.__jefe_proyecto

    @jefe_proyecto.setter
    def jefe_proyecto(self, valor):
        self.__jefe_proyecto = valor
        


    

            
    