# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manuskript/ui/editors/completer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_completer(object):
    def setupUi(self, completer):
        completer.setObjectName("completer")
        completer.resize(163, 143)
        self.verticalLayout = QtWidgets.QVBoxLayout(completer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLineEdit(completer)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.list = QtWidgets.QListWidget(completer)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)

        self.retranslateUi(completer)
        QtCore.QMetaObject.connectSlotsByName(completer)

    def retranslateUi(self, completer):
        _translate = QtCore.QCoreApplication.translate
        completer.setWindowTitle(_translate("completer", "Form"))
