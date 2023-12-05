import sys
from PyQt5.QtWidgets import QApplication
from modelo.facultad import Facultad
from presentador.presentador_computadora import PresentadorComputadoras
from presentador.presentador_computadora_internet import PresentadorComputadorasInternet
from presentador.presentador_gest_locales import PresentadorLocales
from presentador.presentador_gest_proyectos import PresentadorProyectos
from presentador.presentador_calcular_desgaste import PresentadorPorCientoDesgaste
from presentador.presentador_asignar_internet import PresentadorAsignarInternet
from presentador.presentador_calcular_porcentaje import PresentadorPorcentajeComputadorasInternet
from presentador.presentador_obtener_responsable import PresentadorObtenerComputadorasResponsable
from presentador.presentador_vincular_computadoras_proyectos import PresentadorVincularComputadorasProyectos
from vista.ventana_principal import VentanaPrincipal
from vista.acerca_de import AcercaDe

class PresentadorPrincipal:
    def __init__(self):
        self.__facultad = Facultad()

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal(self)
        self.__vista.show()
        app.exec()

    def presentador_computadoras(self):
        prc = PresentadorComputadoras(self.__facultad)
        prc.iniciar()

    def presentador_computadoras_internet(self):
        pci = PresentadorComputadorasInternet(self.__facultad)
        pci.iniciar()

    def presentador_locales(self):
        pdl = PresentadorLocales(self.__facultad)
        pdl.iniciar()

    def presentador_proyectos(self):
        pdp = PresentadorProyectos(self.__facultad)
        pdp.iniciar()
        
    def presentador_calcular_desgaste(self):
        pcd = PresentadorPorCientoDesgaste(self.__facultad)
        pcd.iniciar()

    def presentador_asignar_internet(self):
        pai = PresentadorAsignarInternet(self.__facultad)
        pai.iniciar()

    def presentador_porcentaje_computadoras(self):
        pcp = PresentadorPorcentajeComputadorasInternet(self.__facultad)
        pcp.iniciar()
        
    def presentador_obtener_responsable(self):
        por = PresentadorObtenerComputadorasResponsable(self.__facultad)
        por.iniciar()
        
    def presentador_vincular_computadoras_proyectos(self):
        pvp = PresentadorVincularComputadorasProyectos(self.__facultad)
        pvp.iniciar()
        
    def presentador_acerca_de(self):
        pac = AcercaDe()
        pac.exec()