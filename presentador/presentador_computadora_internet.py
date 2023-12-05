from modelo.computadora_internet import ComputadoraInternet
from vista.gestionar_computadoras_internet import CRUDComputadorasInternet

class PresentadorComputadorasInternet:
    def __init__(self, modelo):
        self.__modelo = modelo

    def iniciar(self):
        self.__vista = CRUDComputadorasInternet(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for computadora in self.__modelo.lista_computadoras_internet():
            i = self.__vista.tabla_computadoras_internet.rowCount()
            self.__vista.tabla_computadoras_internet.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, computadora.nombre_red)
            self.__vista.agregar_elemento_tabla(i, 1, computadora.ip)
            self.__vista.agregar_elemento_tabla(i, 2, computadora.local)
            self.__vista.agregar_elemento_tabla(i, 3, computadora.microprocesador)
            self.__vista.agregar_elemento_tabla(i, 4, computadora.espacio_disco_duro)
            self.__vista.agregar_elemento_tabla(i, 5, computadora.ram_integrada)
            self.__vista.agregar_elemento_tabla(i, 6, computadora.fecha_adquisicion)
            self.__vista.agregar_elemento_tabla(i, 7, computadora.mac)
            self.__vista.agregar_elemento_tabla(i, 8, computadora.hora_inicio)
            self.__vista.agregar_elemento_tabla(i, 9, computadora.hora_final)
        self.__vista.tabla_computadoras_internet.resizeColumnsToContents()

    def insertar_computadora_internet(self):
        try:
            self.__vista.validar_controles()
            nombre_red = self.__vista.valor_nombre_red
            ip = self.__vista.valor_ip
            local = self.__vista.valor_local
            microprocesador = self.__vista.valor_microprocesador
            espacio_disco_duro = self.__vista.valor_espacio_disco_duro
            ram_integrada = self.__vista.valor_ram_integrada
            fecha_adquisicion = self.__vista.valor_fecha_adquisicion
            mac = self.__vista.valor_mac
            hora_inicio = self.__vista.valor_hora_inicio
            hora_final = self.__vista.valor_hora_final

            computadora = ComputadoraInternet(nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion, mac, hora_inicio, hora_final)
            self.__modelo.insertar_computadora_internet(computadora)

            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_computadora_internet(self):
        try:
            ind = self.__vista.tabla_computadoras_internet.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            nombre_red_ant = self.__vista.tabla_computadoras_internet.item(ind, 0).text()

            self.__vista.validar_controles()
            nombre_red = self.__vista.valor_nombre_red
            ip = self.__vista.valor_ip
            local = self.__vista.valor_local
            microprocesador = self.__vista.valor_microprocesador
            espacio_disco_duro = self.__vista.valor_espacio_disco_duro
            ram_integrada = self.__vista.valor_ram_integrada
            fecha_adquisicion = self.__vista.valor_fecha_adquisicion
            mac = self.__vista.valor_mac
            hora_inicio = self.__vista.valor_hora_inicio
            hora_final = self.__vista.valor_hora_final

            computadora = ComputadoraInternet(nombre_red, ip, local, microprocesador, espacio_disco_duro, ram_integrada, fecha_adquisicion, mac, hora_inicio, hora_final)
            self.__modelo.actualizar_computadora_internet(nombre_red_ant, computadora)

            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_computadora_internet(self):
        try:
            ind = self.__vista.tabla_computadoras_internet.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            nombre_red = self.__vista.tabla_computadoras_internet.item(ind, 0).text()

            self.__modelo.eliminar_computadora_internet(nombre_red)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla_computadora_internet(self):
        ind = self.__vista.tabla_computadoras_internet.currentRow()
        if ind != -1:
            nombre_red = self.__vista.tabla_computadoras_internet.item(ind, 0).text()
            ip = self.__vista.tabla_computadoras_internet.item(ind, 1).text()
            local = self.__vista.tabla_computadoras_internet.item(ind, 2).text()
            microprocesador = self.__vista.tabla_computadoras_internet.item(ind, 3).text()
            espacio_disco_duro = self.__vista.tabla_computadoras_internet.item(ind, 4).text()
            ram_integrada = self.__vista.tabla_computadoras_internet.item(ind, 5).text()
            fecha_adquisicion = self.__vista.tabla_computadoras_internet.item(ind, 6).text()
            mac = self.__vista.tabla_computadoras_internet.item(ind, 7).text()
            hora_inicio = self.__vista.tabla_computadoras_internet.item(ind, 8).text()
            hora_final = self.__vista.tabla_computadoras_internet.item(ind, 9).text()

            self.__vista.valor_nombre_red = nombre_red
            self.__vista.valor_ip = ip
            self.__vista.valor_local = local
            self.__vista.valor_microprocesador = microprocesador
            self.__vista.valor_espacio_disco_duro = espacio_disco_duro
            self.__vista.valor_ram_integrada = ram_integrada
            self.__vista.valor_fecha_adquisicion = fecha_adquisicion
            self.__vista.valor_mac = mac
            self.__vista.valor_hora_inicio = hora_inicio
            self.__vista.valor_hora_final = hora_final
