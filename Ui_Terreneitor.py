# Form implementation generated from reading ui file 'c:\Users\victo\OneDrive\Escritorio\UPIITA\4 semestre\programacion avanzada\programas\segundo parcial\practica 7\PRACTICA_07\Terreneitor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Terreneitor(object):
    def setupUi(self, Terreneitor):
        Terreneitor.setObjectName("Terreneitor")
        Terreneitor.resize(900, 600)
        Terreneitor.setMinimumSize(QtCore.QSize(900, 600))
        Terreneitor.setMaximumSize(QtCore.QSize(900, 600))
        self.btn_adelante = QtWidgets.QPushButton(parent=Terreneitor)
        self.btn_adelante.setGeometry(QtCore.QRect(340, 130, 75, 24))
        self.btn_adelante.setObjectName("btn_adelante")
        self.btn_izquierda = QtWidgets.QPushButton(parent=Terreneitor)
        self.btn_izquierda.setGeometry(QtCore.QRect(200, 200, 75, 24))
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.btn_derecha = QtWidgets.QPushButton(parent=Terreneitor)
        self.btn_derecha.setGeometry(QtCore.QRect(450, 190, 75, 24))
        self.btn_derecha.setObjectName("btn_derecha")
        self.btn_atras = QtWidgets.QPushButton(parent=Terreneitor)
        self.btn_atras.setGeometry(QtCore.QRect(350, 230, 75, 24))
        self.btn_atras.setObjectName("btn_atras")

        self.retranslateUi(Terreneitor)
        QtCore.QMetaObject.connectSlotsByName(Terreneitor)

    def retranslateUi(self, Terreneitor):
        _translate = QtCore.QCoreApplication.translate
        Terreneitor.setWindowTitle(_translate("Terreneitor", "Form"))
        self.btn_adelante.setText(_translate("Terreneitor", "PushButton"))
        self.btn_izquierda.setText(_translate("Terreneitor", "PushButton"))
        self.btn_derecha.setText(_translate("Terreneitor", "PushButton"))
        self.btn_atras.setText(_translate("Terreneitor", "PushButton"))
