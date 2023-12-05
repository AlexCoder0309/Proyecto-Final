from modelo.computadora import Computadora

class ComputadoraInternet(Computadora):
    def __init__(self, nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion, mac, hora_inicio, hora_final):
        super().__init__(nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion)
        self.__mac = mac
        self.__hora_inicio = hora_inicio
        self.__hora_final = hora_final



    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, valor):
        self.__mac = valor

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        self.__hora_inicio = valor

    @property
    def hora_final(self):
        return self.__hora_final

    @hora_final.setter
    def hora_final(self, valor):
        self.__hora_final = valor

