# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'producer_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_producter(object):
    def setupUi(self, form_producter):
        form_producter.setObjectName("form_producter")
        form_producter.resize(923, 466)
        self.groupBox_producer = QtWidgets.QGroupBox(form_producter)
        self.groupBox_producer.setGeometry(QtCore.QRect(20, 30, 781, 191))
        self.groupBox_producer.setObjectName("groupBox_producer")
        self.push_add_producer = QtWidgets.QPushButton(self.groupBox_producer)
        self.push_add_producer.setGeometry(QtCore.QRect(630, 150, 113, 32))
        self.push_add_producer.setObjectName("push_add_producer")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_producer)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 60, 231, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_identity_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_identity_name.setObjectName("label_identity_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_identity_name)
        self.line_identity_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_identity_name.setObjectName("line_identity_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_identity_name)
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.line_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_name.setObjectName("line_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_name)
        self.label_phone = QtWidgets.QLabel(self.layoutWidget)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.line_phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_phone.setObjectName("line_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_phone)
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_producer)
        self.layoutWidget_2.setGeometry(QtCore.QRect(340, 80, 271, 64))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_apellido = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_apellido.setObjectName("label_apellido")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_apellido)
        self.line_last_name = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_last_name.setObjectName("line_last_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_last_name)
        self.label_email = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_email.setObjectName("label_email")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.line_email = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_email.setObjectName("line_email")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_email)

        self.retranslateUi(form_producter)
        QtCore.QMetaObject.connectSlotsByName(form_producter)

    def retranslateUi(self, form_producter):
        _translate = QtCore.QCoreApplication.translate
        form_producter.setWindowTitle(_translate("form_producter", "Productor"))
        self.groupBox_producer.setTitle(_translate("form_producter", "Productor"))
        self.push_add_producer.setText(_translate("form_producter", "Insertar"))
        self.label_identity_name.setText(_translate("form_producter", "Documento Identidad"))
        self.label_name.setText(_translate("form_producter", "Nombre"))
        self.label_phone.setText(_translate("form_producter", "Telefono"))
        self.label_apellido.setText(_translate("form_producter", "Apellido"))
        self.label_email.setText(_translate("form_producter", "Correo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_producter = QtWidgets.QWidget()
    ui = Ui_form_producter()
    ui.setupUi(form_producter)
    form_producter.show()
    sys.exit(app.exec_())