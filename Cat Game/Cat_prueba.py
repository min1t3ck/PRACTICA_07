import sys
from PyQt6.QtWidgets import QApplication, QToolBox, QPushButton, QVBoxLayout, QWidget

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QToolBox Dinámico')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.toolbox = QToolBox()
        self.layout.addWidget(self.toolbox)

        self.contactos = []

        self.agregar_contacto("Juan Pérez")
        self.agregar_contacto("María García")

    def agregar_contacto(self, nombre):
        self.contactos.append(nombre)

        boton = QPushButton(nombre)
        boton.clicked.connect(lambda checked, nombre=nombre: self.mostrar_detalle_contacto(nombre))

        indice = len(self.contactos) - 1
        self.toolbox.addItem(boton, f"Contacto {indice + 1}")

    def mostrar_detalle_contacto(self, nombre):
        print(f"Mostrando detalles de {nombre}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())