# Form implementation generated from reading ui file 'c:\Users\toshiba\Desktop\Programacion\Pyton\Practica 7\PRACTICA_07\PRACTICA_07-1\Privado.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Privado(object):
    def setupUi(self, Privado):
        Privado.setObjectName("Privado")
        Privado.resize(900, 600)
        Privado.setMinimumSize(QtCore.QSize(900, 600))
        Privado.setMaximumSize(QtCore.QSize(900, 600))
        self.msgView = QtWidgets.QPlainTextEdit(parent=Privado)
        self.msgView.setGeometry(QtCore.QRect(285, 155, 580, 300))
        self.msgView.setMinimumSize(QtCore.QSize(580, 300))
        self.msgView.setMaximumSize(QtCore.QSize(580, 300))
        self.msgView.setReadOnly(True)
        self.msgView.setObjectName("msgView")
        self.msgWrite = QtWidgets.QLineEdit(parent=Privado)
        self.msgWrite.setGeometry(QtCore.QRect(285, 461, 500, 25))
        self.msgWrite.setMinimumSize(QtCore.QSize(500, 25))
        self.msgWrite.setMaximumSize(QtCore.QSize(580, 400))
        self.msgWrite.setObjectName("msgWrite")
        self.msgSend = QtWidgets.QPushButton(parent=Privado)
        self.msgSend.setGeometry(QtCore.QRect(790, 460, 75, 27))
        self.msgSend.setMinimumSize(QtCore.QSize(75, 27))
        self.msgSend.setMaximumSize(QtCore.QSize(580, 400))
        self.msgSend.setObjectName("msgSend")
        self.btn_friendPicture = QtWidgets.QPushButton(parent=Privado)
        self.btn_friendPicture.setGeometry(QtCore.QRect(50, 40, 180, 180))
        self.btn_friendPicture.setMinimumSize(QtCore.QSize(180, 180))
        self.btn_friendPicture.setMaximumSize(QtCore.QSize(180, 180))
        self.btn_friendPicture.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\toshiba\\Desktop\\Programacion\\Pyton\\Practica 7\\PRACTICA_07\\PRACTICA_07-1\\../Practica 7/Icons/Icon_Fish.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_friendPicture.setIcon(icon)
        self.btn_friendPicture.setIconSize(QtCore.QSize(165, 165))
        self.btn_friendPicture.setObjectName("btn_friendPicture")
        self.btn_profilePicture = QtWidgets.QPushButton(parent=Privado)
        self.btn_profilePicture.setGeometry(QtCore.QRect(50, 350, 180, 180))
        self.btn_profilePicture.setMinimumSize(QtCore.QSize(180, 180))
        self.btn_profilePicture.setMaximumSize(QtCore.QSize(180, 180))
        self.btn_profilePicture.setText("")
        self.btn_profilePicture.setIcon(icon)
        self.btn_profilePicture.setIconSize(QtCore.QSize(165, 165))
        self.btn_profilePicture.setObjectName("btn_profilePicture")
        self.layoutWidget = QtWidgets.QWidget(parent=Privado)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 520, 163, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_Play = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_Play.setObjectName("btn_Play")
        self.horizontalLayout.addWidget(self.btn_Play)
        self.btn_Close = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_Close.setObjectName("btn_Close")
        self.horizontalLayout.addWidget(self.btn_Close)
        self.userName = QtWidgets.QLabel(parent=Privado)
        self.userName.setGeometry(QtCore.QRect(270, 40, 381, 40))
        self.userName.setMinimumSize(QtCore.QSize(370, 40))
        self.userName.setMaximumSize(QtCore.QSize(580, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.userName.setFont(font)
        self.userName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.userName.setObjectName("userName")

        self.retranslateUi(Privado)
        QtCore.QMetaObject.connectSlotsByName(Privado)

    def retranslateUi(self, Privado):
        _translate = QtCore.QCoreApplication.translate
        Privado.setWindowTitle(_translate("Privado", "Form"))
        self.msgSend.setText(_translate("Privado", "Enviar"))
        self.btn_Play.setText(_translate("Privado", "Jugar"))
        self.btn_Close.setText(_translate("Privado", "Cerrar"))
        self.userName.setText(_translate("Privado", "Name_Friend"))
