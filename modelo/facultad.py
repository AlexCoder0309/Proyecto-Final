from datetime import date, datetime
from modelo.computadora_internet import ComputadoraInternet  

class Facultad:
    def __init__(self):
        self.__lista_computadoras = []
        self.__lista_computadoras_internet = []
        self.__lista_proyectos = []
        self.__lista_locales = []
        self.__lista_usuarios = []
        self.__lista_vinculadas = []

    
    def lista_usuarios(self):
        return self.__lista_usuarios

    def lista_vinculadas(self):
        return self.__lista_vinculadas

    #Crud Computadoras con Internet
    def insertar_computadora_internet(self, computadora):
        self.__lista_computadoras_internet.append(computadora)

    def lista_computadoras_internet(self):
        return self.__lista_computadoras_internet
    
    def actualizar_computadora_internet(self, nombre_red, nueva_computadora):
        for i, computadora in enumerate(self.__lista_computadoras_internet):
            if computadora.nombre_red == nombre_red:
                self.__lista_computadoras_internet[i] = nueva_computadora
                break

    def eliminar_computadora_internet(self, nombre_red):
        for computadora in self.__lista_computadoras_internet:
            if computadora.nombre_red == nombre_red:
                self.__lista_computadoras_internet.remove(computadora)   
                
                
    #Crud Computadoras
    def insertar_computadora(self, computadora):
        self.__lista_computadoras.append(computadora)

    def lista_computadoras(self):
        return self.__lista_computadoras
    
    def actualizar_computadora(self, nombre_red, nueva_computadora):
        for i, computadora in enumerate(self.__lista_computadoras):
            if computadora.nombre_red == nombre_red:
                self.__lista_computadoras[i] = nueva_computadora
                break

    def eliminar_computadora(self, nombre_red):
        for computadora in self.__lista_computadoras:
            if computadora.nombre_red == nombre_red:
                self.__lista_computadoras.remove(computadora)   
                          
                          
    #Crud Proyectos
    def insertar_proyecto(self, proyecto):
        self.__lista_proyectos.append(proyecto)

    def lista_proyectos(self):
        return self.__lista_proyectos
           
    def actualizar_proyecto(self, nombre_proyecto, proyecto_nuevo):
        for i, proyecto in enumerate(self.__lista_proyectos):
            if proyecto.nombre_proyecto == nombre_proyecto:
                self.__lista_proyectos[i] = proyecto_nuevo
                break

    def eliminar_proyecto(self, nombre_proyecto):
        for proyecto in self.__lista_proyectos:
            if proyecto.nombre_proyecto == nombre_proyecto:
                self.__lista_proyectos.remove(proyecto)      

     
    #CRUD Locales
    def insertar_local(self, local):
        self.__lista_locales.append(local)

    def lista_locales(self):
        if self.__lista_locales is None:
            return []
        return self.__lista_locales
                
    def actualizar_local(self, nombre_local, local_nuevo):
        for i, local in enumerate(self.__lista_locales):
            if local.nombre_local == nombre_local:
                self.__lista_locales[i] = local_nuevo
                break
            
    def eliminar_local(self, nombre_local):
        for local in self.__lista_locales:
            if local.nombre_local == nombre_local:
                self.__lista_locales.remove(local)


    def asignar_internet(self, ip, mac, hora_inicio, hora_final):
        for computadora_internet in self.__lista_computadoras_internet:
            if computadora_internet.ip == ip:
                return False

        for computadora in self.__lista_computadoras:
            if computadora.ip == ip:
                computadora_internet = ComputadoraInternet(
                    computadora.nombre_red,
                    computadora.ip,
                    computadora.local,
                    computadora.microprocesador,
                    computadora.espacio_disco_duro,
                    computadora.ram_integrada,
                    computadora.fecha_adquisicion,
                    mac,
                    hora_inicio,
                    hora_final
                )
                self.__lista_computadoras_internet.append(computadora_internet)
                self.__lista_computadoras.remove(computadora)
                return True

        return False

    
    
    def calcular_desgaste(self, ip):
        for computadora in self.__lista_computadoras_internet + self.__lista_computadoras:
            if computadora.ip == ip:
                fecha_actual = datetime.now()
                fecha_adquisicion = datetime.strptime(computadora.fecha_adquisicion, "%d-%m-%Y")
                tiempo_transcurrido = fecha_actual - fecha_adquisicion
                desgaste = (tiempo_transcurrido.days / 2555) * 100

                if isinstance(computadora, ComputadoraInternet):
                    horas_iniciales, minutos_iniciales = computadora.hora_inicio.split(":")
                    horas_iniciales = float(horas_iniciales)
                    minutos_iniciales = float(minutos_iniciales)
                    minutos_iniciales /= 60
                    horas_finales, minutos_finales = computadora.hora_final.split(":")
                    horas_finales = float(horas_finales)
                    minutos_finales = float(minutos_finales)
                    minutos_finales /= 60
                    hora_terminacion = horas_finales + minutos_finales
                    horas_iniciacion = horas_iniciales + minutos_iniciales 
                    tiempo_navegacion = (hora_terminacion - horas_iniciacion)
                    desgaste += 0.3 * tiempo_navegacion

                if computadora.microprocesador == "AMD":
                    desgaste -= 1

                return round(max(desgaste, 0), 2)
        return None



    def porcentaje_computadoras_con_navegacion(self):
        total_computadoras = len(self.__lista_computadoras) + len(self.__lista_computadoras_internet)
        computadoras_con_navegacion = 0

        for computadora in self.__lista_computadoras_internet:
            if isinstance(computadora, ComputadoraInternet):
                computadoras_con_navegacion += 1
        if total_computadoras > 0:
            porcentaje = (computadoras_con_navegacion / total_computadoras) * 100
        else:
            porcentaje = 0

        return porcentaje
    
    
    
    def obtener_computadoras_docentes_con_internet_por_responsable(self, nombre_responsable):
        computadoras_docentes_con_internet = []

        for computadora in self.__lista_computadoras_internet:
            for local in self.__lista_locales:
                if computadora.local == local.nombre_local and local.responsable == nombre_responsable:
                    computadoras_docentes_con_internet.append(computadora)

        computadoras_docentes_con_internet.sort(key=lambda x: x.nombre_red)

        return computadoras_docentes_con_internet

    def vincular_computadoras(self, nombre_proyecto, ip, usuarios):
        for proyecto in self.__lista_proyectos:
            if proyecto.nombre_proyecto == nombre_proyecto:
                for computadora in self.__lista_computadoras_internet + self.__lista_computadoras:
                    if computadora.ip == ip:
                        nueva_vinculada = (nombre_proyecto, ip, usuarios)
                        self.__lista_vinculadas.append(nueva_vinculada)
                        return self.__lista_vinculadas

        return None


    def desvincular_computadoras(self, nombre_proyecto, ip):
        for vinculada in self.__lista_vinculadas:
            if vinculada[0] == nombre_proyecto and vinculada[1] == ip:
                self.__lista_vinculadas.remove(vinculada)
                return self.__lista_vinculadas
        return self.__lista_vinculadas
