from Ui_msn_v1 import *
from Ui_Primera import * 
from Ui_Segunda import *
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication
import sys
#Bklblblbllb
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)


class Primera(QDialog, Ui_DialogPrim):
    def __init__(self, *args, **kwargs):
        super(Primera, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn1.clicked.connect(self.abrir_principal)  # Botón Siguiente
        self.btn2.clicked.connect(self.abrir_segunda)    # Botón Segunda

    def abrir_principal(self):
        """Cerrar esta ventana para continuar con Principal."""
        self.accept()  # Cierra `Primera` e informa al bucle principal

    def abrir_segunda(self):
        """Abrir la ventana secundaria como un diálogo modal."""
        self.ventana_segunda = Segunda(self)  # Pasar como hija
        self.ventana_segunda.exec()  # Bloquear mientras `Segunda` está activa

    def closeEvent(self, event):
        """Cerrar todo el programa si se cierra esta ventana."""
        QApplication.instance().quit()  # Garantiza salida completa
        event.accept()


    def cerrar(self):
        """Cerrar la ventana secundaria."""
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    while True:
        # Instanciar y mostrar `Primera`
        print("hola")
        ventana_primera = Primera()
        resultado = ventana_primera.exec()  # Bloquea hasta cerrar `Primera`
        print("adios")

        if resultado == QDialog.DialogCode.Accepted:
            # Abrir `Principal` si el usuario presionó "Siguiente"
            ventana_principal = MainWindow()
            ventana_principal.show()
            break  # Salimos del bucle para no volver a abrir `Primera`
        else:
            # Salimos del programa si la ventana `Primera` se cierra con la "X"
            sys.exit()

    sys.exit(app.exec())

#abfjbaejmfbj,aenfk