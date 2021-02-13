# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_greenhouse_system.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from utp_proyecto_vivero import producer_form as producer_window

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction

class Ui_main_window_greenhouse_system(object):
    def setupUi(self, main_window_greenhouse_system):
        main_window_greenhouse_system.setObjectName("main_window_greenhouse_system")
        main_window_greenhouse_system.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window_greenhouse_system)
        self.centralwidget.setObjectName("centralwidget")
        
        main_window_greenhouse_system.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window_greenhouse_system)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        self.menu_producer = QtWidgets.QMenu(self.menubar)
        self.menu_producer.setObjectName("menu_producer")
        
        self.menu_farm = QtWidgets.QMenu(self.menubar)
        self.menu_farm.setObjectName("menu_farm")
        
        main_window_greenhouse_system.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window_greenhouse_system)
        self.statusbar.setObjectName("statusbar")
        main_window_greenhouse_system.setStatusBar(self.statusbar)
        
        self.action_menu_producer_add = QtWidgets.QAction(main_window_greenhouse_system)
        self.action_menu_producer_add.setObjectName("action_menu_producer_add")
        self.action_menu_producer_add.triggered.connect(self.show_producer_add_form)

        self.action_menu_producer_search = QtWidgets.QAction(main_window_greenhouse_system)
        self.action_menu_producer_search.setObjectName("action_menu_producer_search")
        
        self.action_menu_farm_add = QtWidgets.QAction(main_window_greenhouse_system)
        self.action_menu_farm_add.setObjectName("action_menu_farm_add")

        
        self.menu_producer.addAction(self.action_menu_producer_add)
        self.menu_producer.addAction(self.action_menu_producer_search)
        self.menu_farm.addAction(self.action_menu_farm_add)
        
        self.menubar.addAction(self.menu_producer.menuAction())
        self.menubar.addAction(self.menu_farm.menuAction())

        self.retranslateUi(main_window_greenhouse_system)
        QtCore.QMetaObject.connectSlotsByName(main_window_greenhouse_system)

    def retranslateUi(self, main_window_greenhouse_system):
        _translate = QtCore.QCoreApplication.translate
        main_window_greenhouse_system.setWindowTitle(_translate("main_window_greenhouse_system", "SISTEMA PARA LA ADMINISTRACIÓN DE VIVEROS "))
        
        self.menu_producer.setTitle(_translate("main_window_greenhouse_system", "Productor"))
        self.menu_farm.setTitle(_translate("main_window_greenhouse_system", "Finca"))
        
        
        self.action_menu_producer_add.setText(_translate("main_window_greenhouse_system", "Guardar"))
        self.action_menu_producer_search.setText(_translate("main_window_greenhouse_system", "Buscar"))
        
        self.action_menu_farm_add.setText(_translate("main_window_greenhouse_system", "Guardar"))

        # Esta sentencia permite captura trigger disparado por alguna opcion de QMenu
        #self.menubar.triggered[QAction].connect(self.actionClicked)

    
    # Muestra solamente el nombre de la opcion de menu que fue seleccionada
    def actionClicked(self,q):
        print(q.text()+ " is triggered" )
    
    # Se dispara cuando se selecciona la opcion Guardar Productor en el Menu
    def show_producer_add_form(self):
        print('Open call')
        # Permite que la ventana principal sea la que CREE la ventana secundaria
        # self.window = QtWidgets.QMainWindow()
        # self.ui_producer = producer_window.Ui_form_producter()
        # self.ui_producer.setupUi(self.window)
        # self.window.show()
        
        # Permite delegar la creacion de la ventana secundaria a la propia ventana secundaria
        # a traves del metodo show_window_producer
        self.ui_producer = producer_window.Ui_form_producter()
        self.ui_producer.show_window_producer()
      
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window_greenhouse_system = QtWidgets.QMainWindow()
    ui = Ui_main_window_greenhouse_system()
    ui.setupUi(main_window_greenhouse_system)
    main_window_greenhouse_system.show()
    sys.exit(app.exec_())
