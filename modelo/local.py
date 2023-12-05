class Local:
    def __init__(self, nombre_local, tipo_local, es_docente, responsable):
        self.__nombre_local = nombre_local
        self.__tipo_local = tipo_local
        self.__es_docente = es_docente
        self.__responsable = responsable

    @property
    def nombre_local(self):
        return self.__nombre_local

    @nombre_local.setter
    def nombre_local(self, valor):
        self.__nombre_local = valor

    @property
    def tipo_local(self):
        return self.__tipo_local

    @tipo_local.setter
    def tipo_local(self, valor):
        self.__tipo_local = valor

    @property
    def es_docente(self):
        return self.__es_docente

    @es_docente.setter
    def es_docente(self, valor):
        self.__es_docente = valor

    @property
    def responsable(self):
        return self.__responsable

    @responsable.setter
    def responsable(self, valor):
        self.__responsable = valor
