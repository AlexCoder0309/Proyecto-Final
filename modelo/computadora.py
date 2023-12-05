from datetime import datetime

class Computadora:
    def __init__(self, nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion):
        self.__nombre_red = nombre_red
        self.__ip = ip
        self.__local = local
        self.__microprocesador = microprocesador
        self.__espacio_disco_duro = espacio_disco_duro
        self.__ram_integrada = ram_integrada
        self.__fecha_adquisicion = fecha_adquisicion


        
    #Decoradores
    @property
    def nombre_red(self):
        return self.__nombre_red

    @nombre_red.setter
    def nombre_red(self, valor):
        self.__nombre_red = valor

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, valor):
        self.__ip = valor

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, valor):
        self.__local = valor

    @property
    def microprocesador(self):
        return self.__microprocesador

    @microprocesador.setter
    def microprocesador(self, valor):
        self.__microprocesador = valor

    @property
    def espacio_disco_duro(self):
        return self.__espacio_disco_duro

    @espacio_disco_duro.setter
    def espacio_disco_duro(self, valor):
        self.__espacio_disco_duro = valor

    @property
    def ram_integrada(self):
        return self.__ram_integrada

    @ram_integrada.setter
    def ram_integrada(self, valor):
        self.__ram_integrada = valor

    @property
    def fecha_adquisicion(self):
        return self.__fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self.__fecha_adquisicion = valor
        
    @property
    def lista_usuarios(self):
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, valor):
        self.__lista_usuarios = valor
        

        
