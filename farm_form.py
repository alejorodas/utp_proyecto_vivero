# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'farm_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from utp_proyecto_vivero import farm
from utp_proyecto_vivero import main_window_greenhouse_system as main_greenhouse
from utp_proyecto_vivero import producer_form

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_form_farm(object):
    farms_to_add = []
    producer_to_associated =''
    
    def setupUi(self, form_farm):
        form_farm.setObjectName("form_farm")
        form_farm.resize(857, 304)
        self.groupBox = QtWidgets.QGroupBox(form_farm)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 781, 111))
        self.groupBox.setObjectName("groupBox")
        self.line_municipality = QtWidgets.QLineEdit(self.groupBox)
        self.line_municipality.setGeometry(QtCore.QRect(490, 50, 125, 14))
        self.line_municipality.setObjectName("line_municipality")
        self.line_land_registry = QtWidgets.QLineEdit(self.groupBox)
        self.line_land_registry.setGeometry(QtCore.QRect(240, 50, 125, 15))
        self.line_land_registry.setObjectName("line_land_registry")
        self.label_land_registry = QtWidgets.QLabel(self.groupBox)
        self.label_land_registry.setGeometry(QtCore.QRect(80, 50, 121, 15))
        self.label_land_registry.setObjectName("label_land_registry")
        self.label_municipality = QtWidgets.QLabel(self.groupBox)
        self.label_municipality.setGeometry(QtCore.QRect(400, 50, 59, 14))
        self.label_municipality.setObjectName("label_municipality")
        self.push_add_farm = QtWidgets.QPushButton(self.groupBox)
        self.push_add_farm.setGeometry(QtCore.QRect(620, 70, 113, 32))
        self.push_add_farm.setObjectName("push_add_farm")

        self.retranslateUi(form_farm)
        QtCore.QMetaObject.connectSlotsByName(form_farm)

        Ui_form_farm.producer_to_associated = producer_form.Ui_form_producter.producer
        self.push_add_farm.clicked.connect(self.save_farm)

    def retranslateUi(self, form_farm):
        _translate = QtCore.QCoreApplication.translate
        form_farm.setWindowTitle(_translate("form_farm", "Finca"))
        self.groupBox.setTitle(_translate("form_farm", "Finca"))
        self.label_land_registry.setText(_translate("form_farm", "Número de catastro"))
        self.label_municipality.setText(_translate("form_farm", "Municipio"))
        self.push_add_farm.setText(_translate("form_farm", "Insertar"))
    
    def show_window_farm(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.window.show()
    
    def save_farm(self, producer):
        land_registry = self.line_land_registry.text().strip()
        municipality = self.line_municipality.text().strip()
        
        if (not (land_registry and municipality)):
            self.show_pop_up("Error al insertar Productor", QMessageBox.Critical)
        else:
            self.farm = farm.Farm(land_registry, municipality)
            Ui_form_farm.farms_to_add.append(self.farm)
            self.save_register()
            self.show_pop_up("Productor Agregado!!", QMessageBox.Information)

    
    def show_pop_up(self, message, type_message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setIcon(type_message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
    

    def save_register(self):
        for farm in Ui_form_farm.farms_to_add:
            producer_and_farms = Ui_form_farm.producer_to_associated.asociar(farm)
            greenhouse_list = main_greenhouse.Ui_main_window_greenhouse_system.greenhouse_system_register_list.append(producer_and_farms)
            print("Guardar registro: ", farm)
        print("Guardar Registro:", producer_form.Ui_form_producter.producer)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_farm = QtWidgets.QWidget()
    ui = Ui_form_farm()
    ui.setupUi(form_farm)
    form_farm.show()
    sys.exit(app.exec_())
