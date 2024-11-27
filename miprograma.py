from Ui_msn_v1 import *
from Ui_Primera import * 
from Ui_Segunda import *
from Ui_Privado import *
from Ui_Grupos import *

from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget
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
    def __init__(self, socket_thread,*parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.coneccion = socket_thread
        self.coneccion.signal_message.connect(self.mensaje_entrante)
        
        self.msgSend.clicked.connect(self.mensaje_saliente)
        self.msgWrite.returnPressed.connect(self.mensaje_saliente)
        
        #botones auxiliares pra probar las ventanas de privado y grupal
        self.btn_Private.clicked.connect(self.mensajePrivado)
        self.btn_Group.clicked.connect(self.mensajeGrupo)

    def mensaje_saliente(self):
        str = self.msgWrite.text()
        if str != "" and connected:
            server.send(bytes(str, 'utf-8'))
            self.msgWrite.clear()
            self.mensaje_entrante("<Tú> " + str + '\n')
            
    def mensaje_entrante(self, mensaje):
        self.msgView.setPlainText(self.msgView.toPlainText() + mensaje)
        self.msgView.verticalScrollBar().setValue(self.msgView.verticalScrollBar().maximum())
            
    
    def MostrarAdvertencia(self, texto):
        """Mostrar advertencia al usuario en caso de errores"""
        QMessageBox.warning(self, "Advertencia", texto)

    #abre privado
    def mensajePrivado(self):
        self.ventana_privada = Privado(self) 
        self.ventana_privada.show() 
    #abre grupal
    def mensajeGrupo(self):
        self.ventana_privada = Grupo(self) 
        self.ventana_privada.show() 

class Primera(QDialog, Ui_DialogPrim):
    def __init__(self, *args, **kwargs):
        super(Primera, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn1.clicked.connect(self.abrir_principal)  # Botón Siguiente
        self.btn2.clicked.connect(self.abrir_segunda)    # Botón Segunda

    def VerificarUsuario(self):
        usuario = self.Usuario.text()
        contraseña = self.Contra.text()
        
        if not usuario:
            QMessageBox.warning(self, "No hay usuario", "Ingrese un usuario")
            return False
        else:
            return True
    def abrir_principal(self):
        """Cerrar esta ventana para continuar con Principal."""
        if self.VerificarUsuario():
            user = self.Usuario.text()
            port = 3003
            self.coneccion = ThreadSocket('18.119.116.177', int(port), user)
            self.coneccion.start()  
            self.accept()

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
        '''self.btnCrear_Usuario.clicked.connect(self.CrearUsuario)'''

    def cerrar(self):
        """Cerrar la ventana secundaria."""
        self.close()

    def CrearUsuario(self):
        usuario_nuevo = self.Nuevo_usuario.text()
        contraseña_usuario = self.Contra2.text()
        
#Ventana Mensaje privado        
class Privado(QDialog, Ui_Privado):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        



#Ventana mensaje grupal
class Grupo(QDialog, Ui_Grupo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)        


    
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
            ventana_principal = MainWindow(ventana_primera.coneccion)
            ventana_principal.show()
            break  # Salimos del bucle para no volver a abrir `Primera`
        else:
            # Salimos del programa si la ventana `Primera` se cierra con la "X"
            sys.exit()

    sys.exit(app.exec())

    