from Ui_msn_v1 import *
from Ui_Primera import * 
from Ui_Segunda import *
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.Enviar_chat_general.clicked.connect(self.EnviarGrupal)

    def EnviarGrupal(self):
        "Agregar funcionalidades del servidor"
        mensaje = self.texto_chat_general.text().strip()
        if mensaje:  # Validar que el mensaje no esté vacío
            self.MostrarGrupal(mensaje)
            self.texto_chat_general.clear()
        else:
            self.MostrarAdvertencia("El mensaje no puede estar vacío.")
    
    def MostrarGrupal(self, mensaje):
        """
        Agregar mensaje al chat general.
        """
        self.chat_general.setPlainText(
            self.chat_general.toPlainText() + mensaje + "\n"
        )

        self.chat_general.verticalScrollBar().setValue(
            self.chat_general.verticalScrollBar().maximum()
        )
    
    def MostrarAdvertencia(self, texto):
        """
        Mostrar advertencia al usuario en caso de errores.
        """
        QMessageBox.warning(self, "Advertencia", texto)

               
class Primera(QDialog, Ui_DialogPrim):
    def __init__(self, *args, **kwargs):
        super(Primera, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn1.clicked.connect(self.abrir_principal)  # Botón Siguiente
        self.btn2.clicked.connect(self.abrir_segunda)    # Botón Segunda

    def abrir_principal(self):
        """Cerrar esta ventana para continuar con Principal."""
        "Agregar funciones para verificacion de usuario"
        self.accept()  # Cierra `Primera` e informa al bucle principal

    def abrir_segunda(self):
        """Abrir la ventana secundaria como un diálogo modal."""
        self.ventana_segunda = Segunda(self)  # Pasar como hija
        self.ventana_segunda.exec()  # Bloquear mientras `Segunda` está activa

    def closeEvent(self, event):
        """Cerrar todo el programa si se cierra esta ventana."""
        QApplication.instance().quit()  # Garantiza salida completa
        event.accept()


class Segunda(QDialog, Ui_DialogSeg):
    def __init__(self, parent=None, *args, **kwargs):
        super(Segunda, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn3.clicked.connect(self.cerrar)
        self.btnCrear_Usuario.clicked.connect(self.CrearUsuario)

    def cerrar(self):
        """Cerrar la ventana secundaria."""
        self.close()
    
    def CrearUsuario(self):
        usuario_nuevo = self.Nuevo_usuario.text()
        contraseña_usuario = self.Contra2.text()


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

    