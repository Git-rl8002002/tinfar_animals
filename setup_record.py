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
from fpdf import *

from sensor_setup import area_sensor_setup
from control.dao import * 
from gui.ui_login import *
from gui.ui_main_3 import *




##########################################################################################################################
# main
##########################################################################################################################
class m_content2():
    def show(self):
        print(s_lv)


class setup_record_main_content():
    def show(self):
        global s_lv
        s_lv = 1
    
        

def main():
    f = m_content2()
    f.show()

if __name__ == '__main__':
    main()

        
        

    