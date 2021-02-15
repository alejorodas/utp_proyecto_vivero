# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searh_producer_farm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 668)
        Dialog.setAutoFillBackground(False)
        self.groupBox_producer = QtWidgets.QGroupBox(Dialog)
        self.groupBox_producer.setGeometry(QtCore.QRect(10, 10, 821, 341))
        self.groupBox_producer.setObjectName("groupBox_producer")
        self.push_search_producer = QtWidgets.QPushButton(self.groupBox_producer)
        self.push_search_producer.setGeometry(QtCore.QRect(640, 60, 113, 32))
        self.push_search_producer.setObjectName("push_search_producer")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_producer)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 60, 501, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_identity_document = QtWidgets.QLabel(self.layoutWidget)
        self.label_identity_document.setObjectName("label_identity_document")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_identity_document)
        self.line_identity_document = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_identity_document.setObjectName("line_identity_document")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_identity_document)
        self.widget = QtWidgets.QWidget(self.groupBox_producer)
        self.widget.setGeometry(QtCore.QRect(130, 120, 531, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_name = QtWidgets.QLineEdit(self.widget)
        self.line_name.setReadOnly(True)
        self.line_name.setObjectName("line_name")
        self.gridLayout.addWidget(self.line_name, 1, 2, 1, 1)
        self.label_email = QtWidgets.QLabel(self.widget)
        self.label_email.setObjectName("label_email")
        self.gridLayout.addWidget(self.label_email, 2, 0, 1, 1)
        self.line_email = QtWidgets.QLineEdit(self.widget)
        self.line_email.setReadOnly(True)
        self.line_email.setObjectName("line_email")
        self.gridLayout.addWidget(self.line_email, 2, 1, 1, 2)
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 2)
        self.label_apellido = QtWidgets.QLabel(self.widget)
        self.label_apellido.setObjectName("label_apellido")
        self.gridLayout.addWidget(self.label_apellido, 1, 3, 1, 1)
        self.line_last_name = QtWidgets.QLineEdit(self.widget)
        self.line_last_name.setReadOnly(True)
        self.line_last_name.setObjectName("line_last_name")
        self.gridLayout.addWidget(self.line_last_name, 1, 4, 1, 1)
        self.label_phone = QtWidgets.QLabel(self.widget)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout.addWidget(self.label_phone, 2, 3, 1, 1)
        self.line_phone = QtWidgets.QLineEdit(self.widget)
        self.line_phone.setReadOnly(True)
        self.line_phone.setObjectName("line_phone")
        self.gridLayout.addWidget(self.line_phone, 2, 4, 1, 1)
        self.table_farm_properties = QtWidgets.QTableWidget(Dialog)
        self.table_farm_properties.setGeometry(QtCore.QRect(100, 370, 581, 192))
        self.table_farm_properties.setObjectName("table_farm_properties")
        self.table_farm_properties.setColumnCount(2)
        self.table_farm_properties.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_farm_properties.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_farm_properties.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.line_identity_document, self.push_search_producer)
        Dialog.setTabOrder(self.push_search_producer, self.line_name)
        Dialog.setTabOrder(self.line_name, self.line_last_name)
        Dialog.setTabOrder(self.line_last_name, self.line_email)
        Dialog.setTabOrder(self.line_email, self.line_phone)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Buscar Productor"))
        self.groupBox_producer.setTitle(_translate("Dialog", "Productor"))
        self.push_search_producer.setText(_translate("Dialog", "Buscar"))
        self.label_identity_document.setText(_translate("Dialog", "Documento Identidad"))
        self.label_email.setText(_translate("Dialog", "Correo"))
        self.label_name.setText(_translate("Dialog", "Nombre"))
        self.label_apellido.setText(_translate("Dialog", "Apellido"))
        self.label_phone.setText(_translate("Dialog", "Telefono"))
        item = self.table_farm_properties.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Núm. Catastro"))
        item = self.table_farm_properties.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Municipio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
