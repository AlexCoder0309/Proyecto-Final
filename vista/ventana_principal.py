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

        estilos = ("QMenu {background-color:white;border-radius:5px;border-color: #4070f4;font: 9pt 'Bahnschrift Light SemiCondensed';}"
                                            "QMenu::item {background-color:white; padding: 8px 16px;border-radius:5px;border-color: #4070f4;font: 9pt 'Bahnschrift Light SemiCondensed'; }"
                                            "QMenu::item:selected { background-color: #4070f4;; color: #ffffff;border: 1px solid white; border-radius:5px;border-color: #4070f4;font: 9pt 'Bahnschrift Light SemiCondensed';}")
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
        self.frame_imagen = self.findChild(QFrame, 'frame_imagen')
    def mostrar_menu_gestionar(self):
        # Mostrar el menú desplegable en las coordenadas actuales del botón
        self.menu_gestionar.exec_(self.btn_gestionar.mapToGlobal(self.btn_gestionar.rect().bottomLeft()))
        
    def mostrar_menu_funcionalidades(self):
        # Mostrar el menú desplegable en las coordenadas actuales del botón
        self.menu_funcionalidades.exec_(self.btn_funcionalidades.mapToGlobal(self.btn_funcionalidades.rect().bottomLeft()))



    def resizeEvent(self, a0):
        # Asegurarse de que el QFrame esté presente y visible
        if not self.frame_imagen:
            return

        # Obtener el tamaño del frame_imagen
        width = self.frame_imagen.width()
        height = self.frame_imagen.height()

        # Escalar la imagen al tamaño del frame_imagen
        background = QPixmap('vista/imgs/2.jpeg')
        background = background.scaled(QSize(width, height), Qt.IgnoreAspectRatio)

        # Crear un pincel con la imagen escalada
        pal = self.frame_imagen.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.frame_imagen.setPalette(pal)
        self.frame_imagen.setMask(background.mask())