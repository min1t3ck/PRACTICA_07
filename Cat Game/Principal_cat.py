from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtCore import pyqtSlot
from Ui_cat import Ui_Form
import sys

class Gato(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.jugador_actual = "X"
        self.movimientos = 0

        self.botones = [
            self.pushButton_6,
            self.pushButton_8,
            self.pushButton_9,
            self.pushButton_2,
            self.pushButton,
            self.pushButton_3,
            self.pushButton_5,
            self.pushButton_4,
            self.pushButton_7,
        ]

        for boton in self.botones:
            boton.clicked.connect(self.marcar_casilla)

    @pyqtSlot()
    def marcar_casilla(self):
        boton = self.sender()
        if boton.text() == "":
            boton.setText(self.jugador_actual)
            self.movimientos += 1
            if self.comprobar_ganador():
                self.mostrar_mensaje_ganador()
                self.reiniciar_juego()
            elif self.movimientos == 9:
                self.mostrar_mensaje_empate()
                self.reiniciar_juego()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def comprobar_ganador(self):
        # Comprobar filas
        for i in range(3):
            if self.botones[i * 3].text() == self.botones[i * 3 + 1].text() == self.botones[i * 3 + 2].text() != "":
                return True

        # Comprobar columnas
        for i in range(3):
            if self.botones[i].text() == self.botones[i + 3].text() == self.botones[i + 6].text() != "":
                return True

        # Comprobar diagonales
        if self.botones[0].text() == self.botones[4].text() == self.botones[8].text() != "":
            return True
        if self.botones[2].text() == self.botones[4].text() == self.botones[6].text() != "":
            return True

        return False

    def mostrar_mensaje_ganador(self):
        mensaje = QMessageBox()
        mensaje.setText(f"Ganador: {self.jugador_actual}")
        mensaje.exec()

    def mostrar_mensaje_empate(self):
        mensaje = QMessageBox()
        mensaje.setText("Empate")
        mensaje.exec()

    def reiniciar_juego(self):
        for boton in self.botones:
            boton.setText("")
            boton.setEnabled(True)
        self.jugador_actual = "X"
        self.movimientos = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    juego = Gato()
    juego.show()
    sys.exit(app.exec())