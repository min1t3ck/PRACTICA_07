# Form implementation generated from reading ui file '/home/ja/OneDrive/Documentos/4to_semestre/PA/Practica_07/msn_v1_project/Segunda.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogSeg(object):
    def setupUi(self, DialogSeg):
        DialogSeg.setObjectName("DialogSeg")
        DialogSeg.resize(619, 800)
        self.label = QtWidgets.QLabel(parent=DialogSeg)
        self.label.setGeometry(QtCore.QRect(110, 40, 141, 71))
        self.label.setObjectName("label")
        self.btn3 = QtWidgets.QPushButton(parent=DialogSeg)
        self.btn3.setGeometry(QtCore.QRect(200, 220, 75, 24))
        self.btn3.setObjectName("btn3")

        self.retranslateUi(DialogSeg)
        QtCore.QMetaObject.connectSlotsByName(DialogSeg)

    def retranslateUi(self, DialogSeg):
        _translate = QtCore.QCoreApplication.translate
        DialogSeg.setWindowTitle(_translate("DialogSeg", "Dialog"))
        self.label.setText(_translate("DialogSeg", "Segunda"))
        self.btn3.setText(_translate("DialogSeg", "Volver"))
