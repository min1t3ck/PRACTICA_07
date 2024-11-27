from Ui_msn_v1 import *
from Ui_Primera import * 
from Ui_Segunda import *
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import socket

class ThreadSocket(QThread):
    global connected
    signal_message = pyqtSignal(str)
    def __init__(self, host, port, name):
        global connected
        super().__init__()
        server.connect(('18.119.116.177', 3003))
        connected = True
        server.send(bytes(f"<name>{name}", 'utf-8'))

    def run(self):
        global connected
        try:
            while connected:
                message = server.recv(BUFFER_SIZE)
                if message:
                    self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconected!!>")
                    break
                
        except ...:
            self.signal_message.emit("<!!error!!>")
        finally:
            server.close()
            connected = False
        
    def stop(self):
        global connected
        connected = False
        self.wait()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.Enviar_chat_general.clicked.connect(self.mensaje_saliente)
        self.texto_chat_general.returnPressed.connect(self.mensaje_saliente)
        
    def mensaje_saliente(self):
        str = self.texto_chat_general.text()
        if str != "" and connected:
            server.send(bytes(str, 'utf-8'))
            self.texto_chat_general.clear()
            self.mensage_entrante("<Tú> " + str + '\n')
            
    def mensage_entrante(self, mensaje):
        self.chat_general.setPlainText(self.chat_general.toPlainText() + mensaje)
        self.chat_general.verticalScrollBar().setValue(self.chat_general.verticalScrollBar().maximum())
            
    
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
        self.accept()  # Cierra `Primera` e informa al bucle principa
        port = 3003
        user = 'vic'
        self.coneccion = ThreadSocket('18.119.116.177', int(port), user)

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
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
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

    