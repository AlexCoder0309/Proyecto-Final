from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QComboBox, QLabel, QVBoxLayout, QWidget,QFrame, QAction, QMessageBox, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QResizeEvent, QFont, QIcon, QColor, QColorSpace
from PyQt5 import uic
from vista.recursos import *


from PyQt5.QtWidgets import QMainWindow, QMenu, QMessageBox
from PyQt5.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('vista/ui/ventana_principal.ui', self)

        self.btn_gestionar.clicked.connect(self.mostrar_menu_gestionar)
        self.btn_funcionalidades.clicked.connect(self.mostrar_menu_funcionalidades)
        self.btn_acerca.clicked.connect(self.__presentador.presentador_acerca_de)

        estilos = ("QMenu {background-color:white;border-radius:5px;border-color: rgb(225, 81, 81);font: 9pt 'Bahnschrift Light SemiCondensed';}"
                                            "QMenu::item {background-color:white; padding: 8px 16px;border-radius:5px;border-color: rgb(225, 81, 81);font: 9pt 'Bahnschrift Light SemiCondensed'; }"
                                            "QMenu::item:selected { background-color: rgb(225, 81, 81); color: #ffffff;border: 1px solid white; border-radius:5px;border-color: rgb(225, 81, 81);font: 9pt 'Bahnschrift Light SemiCondensed';}")
        # Crear un menú desplegable
        self.menu_gestionar = QMenu(self)
        self.menu_gestionar.setStyleSheet(estilos)
        
        self.menu_gestionar.addAction("Computadoras con Internet", self.__presentador.presentador_computadoras_internet)
        self.menu_gestionar.addAction("Computadoras sin Internet", self.__presentador.presentador_computadoras)
        self.menu_gestionar.addAction("Locales", self.__presentador.presentador_locales)
        self.menu_gestionar.addAction("Proyectos", self.__presentador.presentador_proyectos)
        
        self.menu_funcionalidades = QMenu(self)
        self.menu_funcionalidades.setStyleSheet(estilos)
        
        self.menu_funcionalidades.addAction("Asignar Internet", self.__presentador.presentador_asignar_internet)
        self.menu_funcionalidades.addAction("Calcular Desgaste", self.__presentador.presentador_calcular_desgaste)
        self.menu_funcionalidades.addAction("Computadoras por Responsable", self.__presentador.presentador_obtener_responsable)
        self.menu_funcionalidades.addAction("Porciento de Computadoras con Internet", self.__presentador.presentador_porcentaje_computadoras)
        self.menu_funcionalidades.addAction("Vincular Computadora a Proyectos", self.__presentador.presentador_vincular_computadoras_proyectos)

    def mostrar_menu_gestionar(self):
        # Mostrar el menú desplegable en las coordenadas actuales del botón
        self.menu_gestionar.exec_(self.btn_gestionar.mapToGlobal(self.btn_gestionar.rect().bottomLeft()))
        
    def mostrar_menu_funcionalidades(self):
        # Mostrar el menú desplegable en las coordenadas actuales del botón
        self.menu_funcionalidades.exec_(self.btn_funcionalidades.mapToGlobal(self.btn_funcionalidades.rect().bottomLeft()))



    def resizeEvent(self, event):
        '''
        método especial de PyQt5 para ser disparada cuando se redimensione
        la pantalla
        '''
        #cargando mapa de pixeles con ruta del fondo en background
        background = QPixmap('vista/imgs/fondo1.jpg')
        background = background.scaled(self.size(),Qt.IgnoreAspectRatio)
        #estableciendo el escalado de la imagen
        #cargando paleta en variable pal
        pal = self.palette()
        #estableciendo tipo de paleta
        pal.setBrush(QPalette.Background, QBrush(background))
        #poniendo paleta en la ventana principal
        self.setPalette(pal)
        