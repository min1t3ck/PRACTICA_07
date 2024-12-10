from Ui_msn_v1 import *
from Ui_Primera import * 
from Ui_Segunda import *
from Ui_Privado import *
from Ui_Grupos import *
from Ui_Terreneitor import *


from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import socket
import pickle

class ThreadSocket(QThread):
    global connected
    signal_message = pyqtSignal(str)
    signal_update_contacts = pyqtSignal(list)  
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
                    try:
                        # Intentamos deserializar el mensaje
                        deserialized = pickle.loads(message)
                        if isinstance(deserialized, list):
                            # Es una lista de usuarios, actualizamos contactos
                            self.signal_update_contacts.emit(deserialized)
                        else:
                            # Mensaje normal
                            self.signal_message.emit(message.decode("utf-8"))
                    except (pickle.UnpicklingError, UnicodeDecodeError):
                        self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconnected!!>")
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
        self.coneccion.signal_update_contacts.connect(self.actualizar_contactos)
        
        
        self.msgSend.clicked.connect(self.mensaje_saliente)
        self.msgWrite.returnPressed.connect(self.mensaje_saliente)
        
        #botones auxiliares pra probar las ventanas de privado y grupal
        self.btn_Private.clicked.connect(self.abrir_privado)
        self.btn_Group.clicked.connect(self.mensajeGrupo)
        
        self.btn_Tereneitor.clicked.connect(self.terreneitor)
        

    def mensaje_saliente(self):
        str = self.msgWrite.text()
        if str != "" and connected:
            server.send(bytes(str, 'utf-8'))
            self.msgWrite.clear()
            self.mensaje_entrante("<Tú> " + str + '\n')
            
    def mensaje_entrante(self, mensaje):
            self.msgView.setPlainText(self.msgView.toPlainText() + mensaje)
            self.msgView.verticalScrollBar().setValue(self.msgView.verticalScrollBar().maximum())
            
    def actualizar_contactos(self, contactos):
        self.Lista_Contactos.clear()
        self.Lista_Contactos.addItems(contactos)
        print(f"Contactos: {contactos}")
    
    #Método para abrir la ventana de mensaje privado
    def abrir_privado(self):
        indice_seleccionado = self.Lista_Contactos.currentRow()
        if indice_seleccionado != -1:
            contacto_seleccionado = self.Lista_Contactos.item(indice_seleccionado).text()
            self.mostrar_ventana_contacto(contacto_seleccionado)
    
    def MostrarAdvertencia(self, texto):
        """Mostrar advertencia al usuario en caso de errores"""
        QMessageBox.warning(self, "Advertencia", texto)

    def mostrar_ventana_contacto(self, contacto):
        self.ventana_privada = Privado(self, contacto) 
        self.ventana_privada.show() 
        
    #abre grupal
    def mensajeGrupo(self):
        self.ventana_privada = Grupo(self) 
        self.ventana_privada.show() 
        
    def terreneitor(self):
        self.ventana_terreneitor = Terrene(self)
        self.ventana_terreneitor.show()
        
    def closeEvent(self, event):
        global connected
        connected = False
        try:
            server.close()  
        except Exception as e:
            print(f"Error al cerrar el socket del cliente: {e}")
        event.accept()

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
    signal_enviar = pyqtSignal(str, str)
    def __init__(self, parent=None, contacto=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_Close.clicked.connect(self.cerrarVentana)
        print("Contacto:", contacto)
        self.userName.setText(contacto)
    
    def mensaje_saliente_privado(self):
        str = self.msgWritePrivate.text()
        if str != "" and connected:
            server.send(bytes(f"<privado>{self.contacto}:{str}", 'utf-8'))
            self.msgWritePrivate.clear()
            self.mensaje_entrante_privado("<Tú> " + str + '\n')
            
    def mensaje_entrante_privado(self, mensaje):
            self.msgViewPrivate.setPlainText(self.msgViewPrivate.toPlainText() + mensaje)
            self.msgViewPrivate.verticalScrollBar().setValue(self.msgViewPrivate.verticalScrollBar().maximum())

    def cerrarVentana(self):
        self.close()

class Terrene(QDialog, Ui_Terreneitor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)        
        self.btn_adelante.pressed.connect(self.enviar_adelante)
        self.btn_adelante.released.connect(self.parar)
        
        self.btn_atras.pressed.connect(self.enviar_atras)
        self.btn_atras.released.connect(self.parar)
        
        self.btn_izquierda.pressed.connect(self.izquierda)
        self.btn_izquierda.released.connect(self.parar)
        
        self.btn_derecha.pressed.connect(self.derecha)
        self.btn_derecha.released.connect(self.parar)
        
        
    def cerrarVentana(self):
        self.close()
        
    def enviar_adelante(self):
        server.send(bytes('<command>Adelante', 'utf-8'))
        
    def enviar_atras(self):
        server.send(bytes('<command>Atras', 'utf-8'))
        
        
    def derecha(self):
        server.send(bytes('<command>Derecha', 'utf-8'))
        
    def izquierda(self):
        server.send(bytes('<command>Izquierda', 'utf-8'))
        
    def parar(self):
        server.send(bytes('<command>Parar', 'utf-8'))
    
    


#Ventana mensaje grupal
class Grupo(QDialog, Ui_Grupo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)        
        self.btn_Close.clicked.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.close()
    
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


    