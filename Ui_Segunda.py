# Form implementation generated from reading ui file 'c:\Users\victo\OneDrive\Escritorio\UPIITA\4 semestre\programacion avanzada\programas\segundo parcial\practica 7\PRACTICA_07\Segunda.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogSeg(object):
    def setupUi(self, DialogSeg):
        DialogSeg.setObjectName("DialogSeg")
        DialogSeg.resize(370, 336)
        DialogSeg.setMinimumSize(QtCore.QSize(370, 336))
        DialogSeg.setMaximumSize(QtCore.QSize(370, 336))
        self.splitter_2 = QtWidgets.QSplitter(parent=DialogSeg)
        self.splitter_2.setGeometry(QtCore.QRect(81, 123, 221, 102))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(parent=self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(parent=self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.Nuevo_usuario = QtWidgets.QLineEdit(parent=self.widget)
        self.Nuevo_usuario.setObjectName("Nuevo_usuario")
        self.horizontalLayout.addWidget(self.Nuevo_usuario)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.Contra2 = QtWidgets.QLineEdit(parent=self.widget)
        self.Contra2.setObjectName("Contra2")
        self.horizontalLayout_2.addWidget(self.Contra2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnCrear_Usuario = QtWidgets.QPushButton(parent=self.splitter)
        self.btnCrear_Usuario.setObjectName("btnCrear_Usuario")
        self.btn3 = QtWidgets.QPushButton(parent=self.splitter_2)
        self.btn3.setObjectName("btn3")

        self.retranslateUi(DialogSeg)
        QtCore.QMetaObject.connectSlotsByName(DialogSeg)

    def retranslateUi(self, DialogSeg):
        _translate = QtCore.QCoreApplication.translate
        DialogSeg.setWindowTitle(_translate("DialogSeg", "Dialog"))
        self.label_5.setText(_translate("DialogSeg", "Nuevo Usuario"))
        self.label_6.setText(_translate("DialogSeg", "Contraseña"))
        self.btnCrear_Usuario.setText(_translate("DialogSeg", "Crear Usuario"))
        self.btn3.setText(_translate("DialogSeg", "Volver"))
