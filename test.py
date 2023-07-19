#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221129
# Update   : 20221208
# Function : new taipei animals department


import sys , time , pymysql , hashlib , minimalmodbus , re , threading
from threading import Thread , Lock
from pyModbusTCP.client import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCharts import *
from fpdf import *

from sensor_setup import area_sensor_setup
from control.dao import * 
from gui.ui_login import *
from gui.ui_main_3 import *
from gui.ui_test import *
from setup_record import m_content2 , setup_record_main_content


       
##########################################################################################################################
# login
##########################################################################################################################
class main_login(QMainWindow):
    
    #global s_user , s_lv , s_login_code

    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.login_init()

    ###############
    # init_login
    ###############
    def login_init(self):
        pass


#########
# main
#########
def main():
    app = QApplication(sys.argv)
    login = main_login()
    login.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    

