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
from gui.ui_login_2 import *
from gui.ui_main_3 import *
from setup_record import m_content2 , setup_record_main_content

#######################################################################################################################################
#
# main_content
#
#######################################################################################################################################
class main_content(QMainWindow):
    
    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_animals_main3()
        self.ui.setupUi(self)
        self.main_init()
    
    ##############
    # main_init
    ##############
    def main_init(self):
        
        ################
        #
        # tab welcome
        #
        ################
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2_welcome)

        ################
        #
        # tab account
        #
        ################
        ### click account manager
        self.ui.action_account.triggered.connect(self.page_1_account)
        ### normal manager account list
        self.normal_manager_account_list()
        ### normal user account list
        self.normal_user_account_list()
        ### logout
        self.ui.action_account_logout.triggered.connect(self.logout)

        #################
        #
        # tab realtime
        #
        #################
        self.ui.action_monitor.triggered.connect(self.page_2_realtime_monitor)

        ##############
        #
        # tab setup
        #
        ##############
        #######################
        # setup alarm A area
        #######################
        self.ui.action_setup_A_area.triggered.connect(self.page_3_setup_A_area)
        ### A area sensor 1 alter submit
        self.ui.btn_a_s_1_submit.clicked.connect(self.alter_setup_a_area_s_1_submit)
        ### A area sensor 2 alter submit
        self.ui.btn_a_s_2_submit.clicked.connect(self.alter_setup_a_area_s_2_submit)
        ### A area sensor 3 alter submit
        self.ui.btn_a_s_3_submit.clicked.connect(self.alter_setup_a_area_s_3_submit)
        ### A area sensor 4 alter submit
        self.ui.btn_a_s_4_submit.clicked.connect(self.alter_setup_a_area_s_4_submit)

        #######################
        # setup alarm B area
        #######################
        self.ui.action_setup_B_area.triggered.connect(self.page_3_setup_B_area)
        ### B area sensor 1 alter submit
        self.ui.btn_b_s_submit_1.clicked.connect(self.alter_setup_b_area_s_1_submit)
        ### B area sensor 2 alter submit
        self.ui.btn_b_s_submit_2.clicked.connect(self.alter_setup_b_area_s_2_submit)
        ### B area sensor 2 alter submit
        self.ui.btn_b_s_submit_3.clicked.connect(self.alter_setup_b_area_s_3_submit)

        #######################
        # setup alarm C area
        #######################
        self.ui.action_setup_C_area.triggered.connect(self.page_3_setup_C_area)
        ### C area sensor 1 alter submit
        self.ui.btn_c_s_submit_1.clicked.connect(self.alter_setup_c_area_s_1_submit)
        ### C area sensor 2 alter submit
        self.ui.btn_c_s_submit_2.clicked.connect(self.alter_setup_c_area_s_2_submit)
        ### C area sensor 3 alter submit
        self.ui.btn_c_s_submit_3.clicked.connect(self.alter_setup_c_area_s_3_submit)
        ### C area sensor 4 alter submit
        self.ui.btn_c_s_submit_4.clicked.connect(self.alter_setup_c_area_s_4_submit)
        ### C area sensor 5 alter submit
        self.ui.btn_c_s_submit_5.clicked.connect(self.alter_setup_c_area_s_5_submit)

        #######################
        # setup alarm D area
        #######################
        self.ui.action_setup_D_area.triggered.connect(self.page_3_setup_D_area)
        ### D area sensor 1 alter submit
        self.ui.btn_d_s_submit_1.clicked.connect(self.alter_setup_d_area_s_1_submit)
        ### D area sensor 2 alter submit
        self.ui.btn_d_s_submit_2.clicked.connect(self.alter_setup_d_area_s_2_submit)
        ### D area sensor 3 alter submit
        self.ui.btn_d_s_submit_3.clicked.connect(self.alter_setup_d_area_s_3_submit)
        ### D area sensor 4 alter submit
        self.ui.btn_d_s_submit_4.clicked.connect(self.alter_setup_d_area_s_4_submit)

        #######################
        # setup alarm E area
        #######################
        self.ui.action_setup_E_area.triggered.connect(self.page_3_setup_E_area)
        ### E area sensor 1 alter submit
        self.ui.btn_e_s_submit_1.clicked.connect(self.alter_setup_e_area_s_1_submit)
        ### E area sensor 2 alter submit
        self.ui.btn_e_s_submit_2.clicked.connect(self.alter_setup_e_area_s_2_submit)
        ### E area sensor 3 alter submit
        self.ui.btn_e_s_submit_3.clicked.connect(self.alter_setup_e_area_s_3_submit)

        ################
        #
        # tab history
        #
        ################
        self.ui.action_history_query.triggered.connect(self.page_4_history_record)
        ### ckick history query submit
        self.ui.btn_history_query_submit.clicked.connect(self.click_history_query_submit)

        ####################
        #
        # tab work record
        #
        ####################
        ### click work record
        self.ui.action_work_record.triggered.connect(self.page_2_work_record)
        ### work record normal manager account list
        self.work_record_normal_manager_account_list()
        ### work record normal user account list
        self.work_record_normal_user_account_list()
   

    ############################
    # page 2 realtime monitor
    ############################
    def page_2_realtime_monitor(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2_realtime_monitor_1)

        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' ,  即時待測參數顯示')

        ### A area
        self.a_area_realtime_monitor_timer()
        ### B area
        self.b_area_realtime_monitor_timer()
        ### C area
        self.c_area_realtime_monitor_timer()
        ### D area
        self.d_area_realtime_monitor_timer()
        ### E area
        self.e_area_realtime_monitor_timer()


    ##################################
    # e area realtime monitor timer
    ##################################
    def e_area_realtime_monitor_timer(self):
        try:
            ### sensor 17
            self.timer_17 = QTimer()
            self.timer_17.timeout.connect(self.e_area_realtime_monitor_s_17)
            self.timer_17.start(92000)

            ### sensor 18
            self.timer_18 = QTimer()
            self.timer_18.timeout.connect(self.e_area_realtime_monitor_s_18)
            self.timer_18.start(94000)

            ### sensor 19
            self.timer_19 = QTimer()
            self.timer_19.timeout.connect(self.e_area_realtime_monitor_s_19)
            self.timer_19.start(96000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area realtime monitor timer : ' + str(e))
        finally:
            pass

    ##################################
    # d area realtime monitor timer
    ##################################
    def d_area_realtime_monitor_timer(self):
        try:
            ### sensor 13
            self.timer_13 = QTimer()
            self.timer_13.timeout.connect(self.d_area_realtime_monitor_s_13)
            self.timer_13.start(84000)

            ### sensor 14
            self.timer_14 = QTimer()
            self.timer_14.timeout.connect(self.d_area_realtime_monitor_s_14)
            self.timer_14.start(86000)

            ### sensor 15
            self.timer_15 = QTimer()
            self.timer_15.timeout.connect(self.d_area_realtime_monitor_s_15)
            self.timer_15.start(88000)

            ### sensor 16
            self.timer_16 = QTimer()
            self.timer_16.timeout.connect(self.d_area_realtime_monitor_s_16)
            self.timer_16.start(90000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area realtime monitor timer : ' + str(e))
        finally:
            pass

    ##################################
    # c area realtime monitor timer
    ##################################
    def c_area_realtime_monitor_timer(self):
        try:
            ### sensor 8
            self.timer_8 = QTimer()
            self.timer_8.timeout.connect(self.c_area_realtime_monitor_s_8)
            self.timer_8.start(74000)

            ### sensor 9
            self.timer_9 = QTimer()
            self.timer_9.timeout.connect(self.c_area_realtime_monitor_s_9)
            self.timer_9.start(76000)

            ### sensor 10
            self.timer_10 = QTimer()
            self.timer_10.timeout.connect(self.c_area_realtime_monitor_s_10)
            self.timer_10.start(78000)

            ### sensor 11
            self.timer_11 = QTimer()
            self.timer_11.timeout.connect(self.c_area_realtime_monitor_s_11)
            self.timer_11.start(80000)

            ### sensor 12
            self.timer_12 = QTimer()
            self.timer_12.timeout.connect(self.c_area_realtime_monitor_s_12)
            self.timer_12.start(82000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area realtime monitor timer : ' + str(e))
        finally:
            pass

    ##################################
    # b area realtime monitor timer
    ##################################
    def b_area_realtime_monitor_timer(self):
        try:
            ### sensor 5
            self.timer_5 = QTimer()
            self.timer_5.timeout.connect(self.b_area_realtime_monitor_s_5)
            self.timer_5.start(68000)

            ### sensor 6
            self.timer_6 = QTimer()
            self.timer_6.timeout.connect(self.b_area_realtime_monitor_s_6)
            self.timer_6.start(70000)

            ### sensor 7
            self.timer_7 = QTimer()
            self.timer_7.timeout.connect(self.b_area_realtime_monitor_s_7)
            self.timer_7.start(72000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area realtime monitor timer : ' + str(e))
        finally:
            pass
    
    ##################################
    # a area realtime monitor timer
    ##################################
    def a_area_realtime_monitor_timer(self):
        try:
            ### sensor 1
            self.timer_1 = QTimer()
            self.timer_1.timeout.connect(self.a_area_realtime_monitor_s_1)
            self.timer_1.start(60000)

            ### sensor 2
            self.timer_2 = QTimer()
            self.timer_2.timeout.connect(self.a_area_realtime_monitor_s_2)
            self.timer_2.start(62000)

            ### sensor 3
            self.timer_3 = QTimer()
            self.timer_3.timeout.connect(self.a_area_realtime_monitor_s_3)
            self.timer_3.start(64000)
            
            ### sensor 4
            self.timer_4 = QTimer()
            self.timer_4.timeout.connect(self.a_area_realtime_monitor_s_4)
            self.timer_4.start(66000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area realtime monitor timer : ' + str(e))
        finally:
            pass
    
    ###################################
    # e area realtime monitor 19
    ###################################
    def e_area_realtime_monitor_s_19(self):
        
        ### variables
        self.s_area = 'E'
        self.s_id   = 19
        self.temp   = self.ui.E_19_r_temp
        self.rh     = self.ui.E_19_r_rh
        self.nh3    = self.ui.E_19_r_nh3
        self.h2s    = self.ui.E_19_r_h2s
        self.pr     = self.ui.E_19_r_pr
        self.r_time = self.ui.E_19_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # e area realtime monitor 18
    ###################################
    def e_area_realtime_monitor_s_18(self):
        
        ### variables
        self.s_area = 'E'
        self.s_id   = 18
        self.temp   = self.ui.E_18_r_temp
        self.rh     = self.ui.E_18_r_rh
        self.nh3    = self.ui.E_18_r_nh3
        self.h2s    = self.ui.E_18_r_h2s
        self.pr     = self.ui.E_18_r_pr
        self.r_time = self.ui.E_18_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # e area realtime monitor 17
    ###################################
    def e_area_realtime_monitor_s_17(self):
        
        ### variables
        self.s_area = 'E'
        self.s_id   = 17
        self.temp   = self.ui.E_17_r_temp
        self.rh     = self.ui.E_17_r_rh
        self.nh3    = self.ui.E_17_r_nh3
        self.h2s    = self.ui.E_17_r_h2s
        self.pr     = self.ui.E_17_r_pr
        self.r_time = self.ui.E_17_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # d area realtime monitor 16
    ###################################
    def d_area_realtime_monitor_s_16(self):
        
        ### variables
        self.s_area = 'D'
        self.s_id   = 16
        self.temp   = self.ui.D_16_r_temp
        self.rh     = self.ui.D_16_r_rh
        self.nh3    = self.ui.D_16_r_nh3
        self.h2s    = self.ui.D_16_r_h2s
        self.pr     = self.ui.D_16_r_pr
        self.r_time = self.ui.D_16_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # d area realtime monitor 15
    ###################################
    def d_area_realtime_monitor_s_15(self):
        
        ### variables
        self.s_area = 'D'
        self.s_id   = 15
        self.temp   = self.ui.D_15_r_temp
        self.rh     = self.ui.D_15_r_rh
        self.nh3    = self.ui.D_15_r_nh3
        self.h2s    = self.ui.D_15_r_h2s
        self.pr     = self.ui.D_15_r_pr
        self.r_time = self.ui.D_15_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # d area realtime monitor 14
    ###################################
    def d_area_realtime_monitor_s_14(self):
        
        ### variables
        self.s_area = 'D'
        self.s_id   = 14
        self.temp   = self.ui.D_14_r_temp
        self.rh     = self.ui.D_14_r_rh
        self.nh3    = self.ui.D_14_r_nh3
        self.h2s    = self.ui.D_14_r_h2s
        self.pr     = self.ui.D_14_r_pr
        self.r_time = self.ui.D_14_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # d area realtime monitor 13
    ###################################
    def d_area_realtime_monitor_s_13(self):
        
        ### variables
        self.s_area = 'D'
        self.s_id   = 13
        self.temp   = self.ui.D_13_r_temp
        self.rh     = self.ui.D_13_r_rh
        self.nh3    = self.ui.D_13_r_nh3
        self.h2s    = self.ui.D_13_r_h2s
        self.pr     = self.ui.D_13_r_pr
        self.r_time = self.ui.D_13_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # c area realtime monitor 12
    ###################################
    def c_area_realtime_monitor_s_12(self):
        
        ### variables
        self.s_area = 'C'
        self.s_id   = 12
        self.temp   = self.ui.C_12_r_temp
        self.rh     = self.ui.C_12_r_rh
        self.nh3    = self.ui.C_12_r_nh3
        self.h2s    = self.ui.C_12_r_h2s
        self.pr     = self.ui.C_12_r_pr
        self.r_time = self.ui.C_12_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # c area realtime monitor 11
    ###################################
    def c_area_realtime_monitor_s_11(self):
        
        ### variables
        self.s_area = 'C'
        self.s_id   = 11
        self.temp   = self.ui.C_11_r_temp
        self.rh     = self.ui.C_11_r_rh
        self.nh3    = self.ui.C_11_r_nh3
        self.h2s    = self.ui.C_11_r_h2s
        self.pr     = self.ui.C_11_r_pr
        self.r_time = self.ui.C_11_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # c area realtime monitor 10
    ###################################
    def c_area_realtime_monitor_s_10(self):
        
        ### variables
        self.s_area = 'C'
        self.s_id   = 10
        self.temp   = self.ui.C_10_r_temp
        self.rh     = self.ui.C_10_r_rh
        self.nh3    = self.ui.C_10_r_nh3
        self.h2s    = self.ui.C_10_r_h2s
        self.pr     = self.ui.C_10_r_pr
        self.r_time = self.ui.C_10_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # c area realtime monitor 9
    ###################################
    def c_area_realtime_monitor_s_9(self):
        
        ### variables
        self.s_area = 'C'
        self.s_id   = 9
        self.temp   = self.ui.C_9_r_temp
        self.rh     = self.ui.C_9_r_rh
        self.nh3    = self.ui.C_9_r_nh3
        self.h2s    = self.ui.C_9_r_h2s
        self.pr     = self.ui.C_9_r_pr
        self.r_time = self.ui.C_9_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # c area realtime monitor 8
    ###################################
    def c_area_realtime_monitor_s_8(self):
        
        ### variables
        self.s_area = 'C'
        self.s_id   = 8
        self.temp   = self.ui.C_8_r_temp
        self.rh     = self.ui.C_8_r_rh
        self.nh3    = self.ui.C_8_r_nh3
        self.h2s    = self.ui.C_8_r_h2s
        self.pr     = self.ui.C_8_r_pr
        self.r_time = self.ui.C_8_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # b area realtime monitor 7
    ###################################
    def b_area_realtime_monitor_s_7(self):
        
        ### variables
        self.s_area = 'B'
        self.s_id   = 7
        self.temp   = self.ui.B_7_r_temp
        self.rh     = self.ui.B_7_r_rh
        self.nh3    = self.ui.B_7_r_nh3
        self.h2s    = self.ui.B_7_r_h2s
        self.pr     = self.ui.B_7_r_pr
        self.r_time = self.ui.B_7_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # b area realtime monitor 6
    ###################################
    def b_area_realtime_monitor_s_6(self):
        
        ### variables
        self.s_area = 'B'
        self.s_id   = 6
        self.temp   = self.ui.B_6_r_temp
        self.rh     = self.ui.B_6_r_rh
        self.nh3    = self.ui.B_6_r_nh3
        self.h2s    = self.ui.B_6_r_h2s
        self.pr     = self.ui.B_6_r_pr
        self.r_time = self.ui.B_6_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)
    
    ###################################
    # b area realtime monitor 5
    ###################################
    def b_area_realtime_monitor_s_5(self):
        
        ### variables
        self.s_area = 'B'
        self.s_id   = 5
        self.temp   = self.ui.B_5_r_temp
        self.rh     = self.ui.B_5_r_rh
        self.nh3    = self.ui.B_5_r_nh3
        self.h2s    = self.ui.B_5_r_h2s
        self.pr     = self.ui.B_5_r_pr
        self.r_time = self.ui.B_5_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # a area realtime monitor 4
    ###################################
    def a_area_realtime_monitor_s_4(self):
        
        ### variables
        self.s_area = 'A'
        self.s_id   = 4
        self.temp   = self.ui.A_4_r_temp
        self.rh     = self.ui.A_4_r_rh
        self.nh3    = self.ui.A_4_r_nh3
        self.h2s    = self.ui.A_4_r_h2s
        self.pr     = self.ui.A_4_r_pr
        self.r_time = self.ui.A_4_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # a area realtime monitor 3
    ###################################
    def a_area_realtime_monitor_s_3(self):
        
        ### variables
        self.s_area = 'A'
        self.s_id   = 3
        self.temp   = self.ui.A_3_r_temp
        self.rh     = self.ui.A_3_r_rh
        self.nh3    = self.ui.A_3_r_nh3
        self.h2s    = self.ui.A_3_r_h2s
        self.pr     = self.ui.A_3_r_pr
        self.r_time = self.ui.A_3_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # a area realtime monitor 2
    ###################################
    def a_area_realtime_monitor_s_2(self):
        
        ### variables
        self.s_area = 'A'
        self.s_id   = 2
        self.temp   = self.ui.A_2_r_temp
        self.rh     = self.ui.A_2_r_rh
        self.nh3    = self.ui.A_2_r_nh3
        self.h2s    = self.ui.A_2_r_h2s
        self.pr     = self.ui.A_2_r_pr
        self.r_time = self.ui.A_2_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ###################################
    # a area realtime monitor 1
    ###################################
    def a_area_realtime_monitor_s_1(self):
        
        ### variables
        self.s_area = 'A'
        self.s_id   = 1
        self.temp   = self.ui.A_1_r_temp
        self.rh     = self.ui.A_1_r_rh
        self.nh3    = self.ui.A_1_r_nh3
        self.h2s    = self.ui.A_1_r_h2s
        self.pr     = self.ui.A_1_r_pr
        self.r_time = self.ui.A_1_r_time

        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.tb     = self.n_time.toString("yyyy_MM")
        
        ### realtime monitor db from sensor
        self.realtime_monitor_db(self.tb , self.s_area , self.s_id , self.temp , self.rh , self.nh3 , self.h2s , self.pr , self.r_time)

    ########################
    # realtime monitor db
    ########################
    def realtime_monitor_db(self , tb , area , id , temp , rh , nh3 , h2s , pr , r_time):
        try:
            
            self.tb     = tb
            self.s_area = area
            self.s_id   = id
            self.temp   = temp
            self.rh     = rh
            self.nh3    = nh3
            self.h2s    = h2s
            self.pr     = pr
            self.r_time = r_time

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            
            ##################
            #
            # temp
            #
            ##################
            self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.s_area , self.s_id)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                
                ### temp top value
                self.temp_top_sql    = "select s_alarm_top from setup_record where s_id='{0}' and s_item='{1}' and s_position='top'".format(self.s_id , 'temp')
                self.curr.execute(self.temp_top_sql)
                self.temp_top_val    = self.curr.fetchone()
                
                ### temp  bottom value
                self.temp_bottom_sql = "select s_alarm_bottom from setup_record where s_id='{0}' and s_item='{1}' and s_position='bottom'".format(self.s_id , 'temp')
                self.curr.execute(self.temp_bottom_sql)
                self.temp_bottom_val = self.curr.fetchone()
                
                ### realtime monitor record time
                self.r_time.setText(str(val[0]))

                self.temp_val        = val[1]
                self.temp_top_val    = self.temp_top_val[0]
                self.temp_bottom_val = self.temp_bottom_val[0]

            ### realtime monitor now value 
            if float(self.temp_val) > float(self.temp_top_val):
                    
                ### over top value device auto run 
                self.top_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'temp' , 'top')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.temp_t_d_status = val[0]
                    self.temp_t_d_device = val[1]
                
                if str(self.temp_t_d_status) == 'enable':
                    self.temp.setStyleSheet("color:red;")
                    self.temp.setText('溫度 ' + str(self.temp_val) + ' °C , 過高 ! ' + str(self.t_d[1])  + ' ( 自動啟動 )')
                else:
                    self.temp.setStyleSheet("color:red;")
                    self.temp.setText('溫度 ' + str(self.temp_val) + ' °C , 過高 ! ' + str(self.t_d[1])  + ' ( 手動啟動 )')
                

            elif float(self.temp_val) < float(self.temp_bottom_val):
                    
                ### low bottom value device auto run 
                self.bottom_device_sql = "select s_bottom_auto_run , s_alarm_bottom_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'temp' , 'bottom')
                self.curr.execute(self.top_device_sql)
                self.b_d = self.curr.fetchall()

                for val in self.t_d:
                    self.temp_b_d_status = val[0]
                    self.temp_b_d_device = val[1]

                if str(self.temp_b_d_status) == 'enable':
                    self.temp.setStyleSheet("color:blue;")
                    self.temp.setText('溫度 ' + str(self.temp_val) + ' °C , 過低 ! ' + str(self.b_d[1]) + ' ( 自動啟動 )')
                else:
                    self.temp.setStyleSheet("color:blue;")
                    self.temp.setText('溫度 ' + str(self.temp_val) + ' °C , 過低 ! ' + str(self.b_d[1]) + ' ( 手動啟動 )')
            else:
                self.temp.setStyleSheet("color:black;")
                self.temp.setText('溫度 ' + str(self.temp_val) + ' °C')

            ##############
            #
            # rh
            #
            ##############
            self.sql2 = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.s_area , self.s_id)
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                
                ### rh top value
                self.rh_top_sql    = "select s_alarm_top from setup_record where s_id='{0}' and s_item='{1}' and s_position='top'".format(self.s_id , 'rh')
                self.curr.execute(self.rh_top_sql)
                self.rh_top_val    = self.curr.fetchone()
                
                ### rh bottom value
                self.rh_bottom_sql = "select s_alarm_bottom from setup_record where s_id='{0}' and s_item='{1}' and s_position='bottom'".format(self.s_id , 'rh')
                self.curr.execute(self.rh_bottom_sql)
                self.rh_bottom_val = self.curr.fetchone()
                
                ### realtime monitor record time
                self.r_time.setText(str(val[0]))

                self.rh_val        = val[1]
                self.rh_top_val    = self.rh_top_val[0]
                self.rh_bottom_val = self.rh_bottom_val[0]

            ### realtime monitor now value , judge over top value or too low bottom value 
            if float(self.rh_val) > float(self.rh_top_val):
                    
                ### over top value device auto run 
                self.top_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'rh' , 'top')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.rh_t_d_status = val[0]
                    self.rh_t_d_device = val[1]
                
                if str(self.rh_t_d_status) == 'enable':
                    self.rh.setStyleSheet("color:red;")
                    self.rh.setText('濕度 ' + str(self.rh_val) + ' % , 過高 ! ' + str(self.rh_t_d_device) + ' ( 自動啟動 )')
                else:
                    self.rh.setStyleSheet("color:red;")
                    self.rh.setText('濕度 ' + str(self.rh_val) + ' % , 過高 ! ' + str(self.rh_t_d_device) + ' ( 手動啟動 )')

            elif float(self.rh_val) < float(self.rh_bottom_val):
                    
                ### low bottom value device auto run 
                self.bottom_device_sql = "select s_bottom_auto_run , s_alarm_bottom_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'rh' , 'bottom')
                self.curr.execute(self.top_device_sql)
                self.b_d = self.curr.fetchall()
                
                for val in self.b_d:
                    self.rh_b_d_status = val[0]
                    self.rh_b_d_device = val[1]

                if str(self.rh_b_d_status) == 'enable':
                    self.rh.setStyleSheet("color:blue;")
                    self.rh.setText('濕度 ' + str(self.rh_val) + ' % , 過低 !' + str(self.rh_b_d_device) + ' ( 自動啟動 )')
                else:
                    self.rh.setStyleSheet("color:blue;")
                    self.rh.setText('濕度 ' + str(self.rh_val) + ' % , 過低 !' + str(self.rh_b_d_device) + ' ( 手動啟動 )')
            else:
                self.rh.setStyleSheet("color:black;")
                self.rh.setText('濕度 ' + str(self.rh_val) + ' %')

                

            ################
            #
            # nh3
            #
            ################
            self.sql3 = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.s_area , self.s_id)
            self.curr.execute(self.sql3)
            self.res3 = self.curr.fetchall()
            
            for val in self.res3:

                ### nh3 top value
                self.nh3_top_sql = "select s_alarm_top from setup_record where s_id='{0}' and s_item='{1}' and s_position='top'".format(self.s_id , 'nh3')
                self.curr.execute(self.nh3_top_sql)
                self.nh3_top_val = self.curr.fetchone()
                
                ### nh3 bottom value
                self.nh3_bottom_sql = "select s_alarm_bottom from setup_record where s_id='{0}' and s_item='{1}' and s_position='bottom'".format(self.s_id , 'nh3')
                self.curr.execute(self.nh3_bottom_sql)
                self.nh3_bottom_val = self.curr.fetchone()

                self.nh3_val        = val[1]
                self.nh3_top_val    = self.nh3_top_val[0]
                self.nh3_bottom_val = self.nh3_bottom_val[0]

            ### realtime monitor now value , judge over top value or too low bottom value 
            if float(self.nh3_val) > float(self.nh3_top_val):
                    
                ### over top value device auto run 
                self.top_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'nh3' , 'top')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.nh3_t_d_status = val[0]
                    self.nh3_t_d_device = val[1]

                if str(self.nh3_t_d_status) == 'enable':
                    self.nh3.setStyleSheet("color:red;")
                    self.nh3.setText('氨氣 ' + str(self.nh3_val) + ' ppm , 過高 ! ' + str(self.nh3_t_d_device) + '( 自動啟動 )')
                else:
                    self.nh3.setStyleSheet("color:red;")
                    self.nh3.setText('氨氣 ' + str(self.nh3_val) + ' ppm , 過高 ! ' + str(self.nh3_t_d_device) + ' ( 手動啟動 )')

            elif float(self.nh3_val) < float(self.nh3_bottom_val):
                    
                ### low bottom value device auto run 
                self.bottom_device_sql = "select s_bottom_auto_run , s_alarm_bottom_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'nh3' , 'bottom')
                self.curr.execute(self.bottom_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.nh3_b_d_status = val[0]
                    self.nh3_b_d_device = val[1]
                
                if str(self.nh3_b_d_status) == 'enable':
                    self.nh3.setStyleSheet("color:blue;")
                    self.nh3.setText('氨氣 ' + str(self.nh3_val) + ' ppm , 過低 !' + str(self.nh3_b_d_device) + ' ( 自動啟動 )')
                else:
                    self.nh3.setStyleSheet("color:blue;")
                    self.nh3.setText('氨氣 ' + str(self.nh3_val) + ' ppm , 過低 !' + str(self.nh3_b_d_device) + ' ( 手動啟動 )')
            
            else:
                self.nh3.setStyleSheet("color:black;")
                self.nh3.setText('氨氣 ' + str(self.nh3_val) + ' ppm')

            ################
            #
            # h2s
            #
            ################
            self.sql4 = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.s_area , self.s_id)
            self.curr.execute(self.sql4)
            self.res4 = self.curr.fetchall()

            for val in self.res4:
                
                ### h2s top value
                self.h2s_top_sql    = "select s_alarm_top from setup_record where s_id='{0}' and s_item='{1}' and s_position='top'".format(self.s_id , 'h2s')
                self.curr.execute(self.h2s_top_sql)
                self.h2s_top_val    = self.curr.fetchone()
                
                ### h2s bottom value
                self.h2s_bottom_sql = "select s_alarm_bottom from setup_record where s_id='{0}' and s_item='{1}' and s_position='bottom'".format(self.s_id , 'h2s')
                self.curr.execute(self.h2s_bottom_sql)
                self.h2s_bottom_val = self.curr.fetchone()
                
                ### realtime monitor record time
                self.r_time.setText(str(val[0]))

                self.h2s_val        = val[1]
                self.h2s_top_val    = self.h2s_top_val[0]
                self.h2s_bottom_val = self.h2s_bottom_val[0]

            ### realtime monitor now value , judge over top value or too low bottom value 
            if float(self.h2s_val) > float(self.h2s_top_val):

                ### over top value device auto run 
                self.top_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'h2s' , 'top')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.h2s_t_d_status = val[0]
                    self.h2s_t_d_device = val[1]

                if str(self.h2s_t_d_status) == 'enable': 
                    self.h2s.setStyleSheet("color:red;")
                    self.h2s.setText('硫化氫 ' + str(self.h2s_val) + ' ppm , 過高 ! ' + str(self.h2s_t_d_device) + ' ( 自動啟動 )')
                else:
                    self.h2s.setStyleSheet("color:red;")
                    self.h2s.setText('硫化氫 ' + str(self.h2s_val) + ' ppm , 過高 ! ' + str(self.h2s_t_d_device) + ' ( 手動啟動 )')

            elif float(self.h2s_val) < float(self.h2s_bottom_val):
                    
                ### low bottom value device auto run 
                self.bottom_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'h2s' , 'bottom')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.h2s_b_d_status = val[0]
                    self.h2s_b_d_device = val[1]
                
                if str(self.h2s_b_d_status) == 'enable':
                    self.h2s.setStyleSheet("color:blue;")
                    self.h2s.setText('硫化氫 ' + str(self.h2s_val) + ' ppm , 過低 ! ' + self.h2s_b_d_device + ' ( 自動啟動 ) ')
                else:
                    self.h2s.setStyleSheet("color:blue;")
                    self.h2s.setText('硫化氫 ' + str(self.h2s_val) + ' ppm , 過低 ! ' + self.h2s_b_d_device + ' ( 手動啟動 ) ')

            else:
                self.h2s.setStyleSheet("color:black;")
                self.h2s.setText('硫化氫 ' + str(self.h2s_val) + ' ppm')

            ##############
            #
            # pr
            #
            ##############
            self.sql5 = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.s_area , self.s_id)
            self.curr.execute(self.sql5)
            self.res5 = self.curr.fetchall()

            for val in self.res5:
                
                ### pr top value
                self.pr_top_sql    = "select s_alarm_top from setup_record where s_id='{0}' and s_item='{1}' and s_position='top'".format(self.s_id , 'pr')
                self.curr.execute(self.pr_top_sql)
                self.pr_top_val    = self.curr.fetchone()
                
                ### pr bottom value
                self.pr_bottom_sql = "select s_alarm_bottom from setup_record where s_id='{0}' and s_item='{1}' and s_position='bottom'".format(self.s_id , 'pr')
                self.curr.execute(self.pr_bottom_sql)
                self.pr_bottom_val = self.curr.fetchone()
                
                ### realtime monitor record time
                self.r_time.setText(str(val[0]))

                self.pr_val        = val[1]
                self.pr_top_val    = self.pr_top_val[0]
                self.pr_bottom_val = self.pr_bottom_val[0]

            ### realtime monitor now value , judge over top value or too low bottom value 
            if float(self.pr_val) > float(self.pr_top_val):
                    
                ### over top value device auto run 
                self.top_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'pr' , 'top')
                self.curr.execute(self.top_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.pr_t_d_status = val[0]
                    self.pr_t_d_device = val[1]
                
                if str(self.pr_t_d_status) == 'enable':
                    self.pr.setStyleSheet("color:red;")
                    self.pr.setText('大氣壓力 ' + str(self.pr_val) + ' hPa , 過高 ! ' + str(self.pr_t_d_device) + ' ( 自動啟動 )')
                else:
                    self.pr.setStyleSheet("color:red;")
                    self.pr.setText('大氣壓力 ' + str(self.pr_val) + ' hPa , 過高 ! ' + str(self.pr_t_d_device) + ' ( 手動啟動 )')

            elif float(self.pr_val) < float(self.pr_bottom_val):

                ### low bottom value device auto run 
                self.bottom_device_sql = "select s_top_auto_run , s_alarm_top_device from setup_record where s_id='{0}' and s_item='{1}' and s_position='{2}'".format(self.s_id , 'pr' , 'bottom')
                self.curr.execute(self.bottom_device_sql)
                self.t_d = self.curr.fetchall()

                for val in self.t_d:
                    self.pr_b_d_status = val[0]
                    self.pr_b_d_device = val[1]    
                
                if str(self.pr_b_d_status) == 'enable':
                    self.pr.setStyleSheet("color:blue;")
                    self.pr.setText('大氣壓力 ' + str(self.pr_val) + ' hPa , 過低 ! ' + str(self.pr_b_d_device) + ' ( 自動啟動 )')
                else:
                    self.pr.setStyleSheet("color:blue;")
                    self.pr.setText('大氣壓力 ' + str(self.pr_val) + ' hPa , 過低 ! ' + str(self.pr_b_d_device) + ' ( 手動啟動 )')

            else:
                self.pr.setStyleSheet("color:black;")
                self.pr.setText('大氣壓力 ' + str(self.pr_val) + ' hPa')
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > ' + self.s_area + ' area realtime monitor sensor id = ' + self.s_id +  ' : ' + str(e))
        finally:
            pass

    ###############################
    # click history query submit
    ###############################
    def click_history_query_submit(self):

        try:
            ### clear 
            self.ui.history_query_result_list.clear()
            
            ### analysis string by date
            self.s_time = self.ui.history_query_start_time.text()
            self.data   = self.s_time.split(' ')
            self.data2  = self.data[0].split('-')
            
            ### month < 10 , add 0 , 1 ~ 9 month 
            if str(self.data2[1]) < '10':
                self.tb     = self.data2[0] + '_0' + self.data2[1]
            else:
                self.tb     = self.data2[0] + '_' + self.data2[1]
            
            self.e_time = self.ui.history_query_end_time.text()
            self.data3  = self.ui.history_query_area.currentText()
            self.q_area = self.data3[0:1]

            self.q_area = self.q_area.strip()

            self.q_id   = self.ui.history_query_id.currentText()
            self.q_item = self.ui.history_query_item.currentText()

            ### work record
            self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , 查詢 ' + str(self.s_time) + ' ~ ' +  str(self.e_time) + ' , ' + str(self.q_area)  + ' 區 , sensor ' + str(self.q_id) + ' , ' + self.q_item  + ' , 歷史記錄')

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            if self.q_item == '溫度':
                self.sql = "select r_daytime , val_1 from {0} where r_time>='{1}' and r_time<='{2}' and s_area='{3}' and s_kind='{4}' order by r_daytime desc limit 0,36".format(self.tb , self.s_time , self.e_time , self.q_area , self.q_id)
            elif self.q_item == '濕度':
                self.sql = "select r_daytime , val_2 from {0} where r_time>='{1}' and r_time<='{2}' and s_area='{3}' and s_kind='{4}' order by r_daytime desc limit 0,36".format(self.tb , self.s_time , self.e_time , self.q_area , self.q_id)
            elif self.q_item == '氨氣':
                self.sql = "select r_daytime , val_3 from {0} where r_time>='{1}' and r_time<='{2}' and s_area='{3}' and s_kind='{4}' order by r_daytime desc limit 0,36".format(self.tb , self.s_time , self.e_time , self.q_area , self.q_id)
            elif self.q_item == '硫化氫':
                self.sql = "select r_daytime , val_4 from {0} where r_time>='{1}' and r_time<='{2}' and s_area='{3}' and s_kind='{4}' order by r_daytime desc limit 0,36".format(self.tb , self.s_time , self.e_time , self.q_area , self.q_id)
            elif self.q_item == '大氣壓力':
                self.sql = "select r_daytime , val_5 from {0} where r_time>='{1}' and r_time<='{2}' and s_area='{3}' and s_kind='{4}' order by r_daytime desc limit 0,36".format(self.tb , self.s_time , self.e_time , self.q_area , self.q_id)

            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle(self.q_area + '區 , 偵測器 ' + self.q_id )
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### 曲線
            self.series0    = QLineSeries()
            ### 顯示點的值
            self.series1    = QScatterSeries()


            for val in self.res:
                if self.q_item == '溫度':
                    self.series0.setName('溫度線')
                    self.series1.setName('目前溫度值(°C)')
                    self.date_fmt = "HH:mm:ss"
                    self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                    self.y = float(val[1])
                    self.series0.append(self.x , self.y)
                    self.series1.append(self.x , self.y)
                    self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_temp)
                    self.ui.history_query_result_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' °C')

                elif self.q_item == '濕度':
                    self.series0.setName('濕度線')
                    self.series1.setName('目前濕度值(%)')
                    self.date_fmt = "HH:mm:ss"
                    self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                    self.y = float(val[1])
                    self.series0.append(self.x , self.y)
                    self.series1.append(self.x , self.y)
                    self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_rh)
                    self.ui.history_query_result_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' %')

                elif self.q_item == '氨氣':
                    self.series0.setName('氨氣線')
                    self.series1.setName('目前氨氣值(ppm)')
                    self.date_fmt = "HH:mm:ss"
                    self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                    self.y = float(val[1])
                    self.series0.append(self.x , self.y)
                    self.series1.append(self.x , self.y)
                    self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_nh3)
                    self.ui.history_query_result_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' ppm')

                elif self.q_item == '硫化氫':
                    self.series0.setName('硫化氫線')
                    self.series1.setName('目前硫化氫值(ppm)')
                    self.date_fmt = "HH:mm:ss"
                    self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                    self.y = float(val[1])
                    self.series0.append(self.x , self.y)
                    self.series1.append(self.x , self.y)
                    self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_h2s)
                    self.ui.history_query_result_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' ppm')

                elif self.q_item == '大氣壓力':
                    self.series0.setName('大氣壓力線')
                    self.series1.setName('目前大氣壓力值(hPa)')
                    self.date_fmt = "HH:mm:ss"
                    self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                    self.y = float(val[1])
                    self.series0.append(self.x , self.y)
                    self.series1.append(self.x , self.y)
                    self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_pr)
                    self.ui.history_query_result_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' hPa')

            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### Setting X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("HH:mm:ss")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### Setting Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%.1f")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### show history record chart
            self.form = QWidget()
            self.sub = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.form.setLayout(self.sub)
            self.form.setWindowTitle('歷史記錄查詢')
            self.form.resize(800,600)
            self.form.show()

            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > click history query submit : " + str(e))
        finally:
            pass

    ###########################################
    # history record to chart mouse hover pr 
    ###########################################
    def history_record_to_chart_mouse_hover_pr(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName(self.n_time + ' , 目前 大氣壓力 ' + str(point.y()) + ' hPa') 
    
    ############################################
    # history record to chart mouse hover h2s 
    ############################################
    def history_record_to_chart_mouse_hover_h2s(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 硫化氫 ' + str(point.y()) + ' ppm') 
    
    ############################################
    # history record to chart mouse hover nh3 
    ############################################
    def history_record_to_chart_mouse_hover_nh3(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 氨氣 ' + str(point.y()) + ' ppm') 
    
    ###########################################
    # history record to chart mouse hover rh 
    ###########################################
    def history_record_to_chart_mouse_hover_rh(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 濕度 ' + str(point.y()) + ' %') 

    #############################################
    # history record to chart mouse hover temp 
    #############################################
    def history_record_to_chart_mouse_hover_temp(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 溫度 ' + str(point.y()) + ' °C') 

    ############################
    # history record to chart 
    ############################
    def history_record_to_chart(self):
        pass

    ###################
    # history record
    ###################
    def page_4_history_record(self):
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4_history_record)
        ### start and end time
        self.ui.history_query_start_time.setDateTime(QDateTime.currentDateTime())
        self.ui.history_query_end_time.setDateTime(QDateTime.currentDateTime())

        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , 點選歷史記錄查詢')

        ### A area
        self.ui.history_query_result_list_A.clear()
        self.history_record_total_list_A('A', 1 , '溫度')
        self.history_record_total_list_A('A', 1 , '濕度')
        self.history_record_total_list_A('A', 1 , '氨氣')
        self.history_record_total_list_A('A', 1 , '硫化氫')
        self.history_record_total_list_A('A', 1 , '大氣壓力')
        self.history_record_total_list_A('A', 2 , '溫度')
        self.history_record_total_list_A('A', 2 , '濕度')
        self.history_record_total_list_A('A', 2 , '氨氣')
        self.history_record_total_list_A('A', 2 , '硫化氫')
        self.history_record_total_list_A('A', 2 , '大氣壓力')
        self.history_record_total_list_A('A', 3 , '溫度')
        self.history_record_total_list_A('A', 3 , '濕度')
        self.history_record_total_list_A('A', 3 , '氨氣')
        self.history_record_total_list_A('A', 3 , '硫化氫')
        self.history_record_total_list_A('A', 3 , '大氣壓力')
        self.history_record_total_list_A('A', 4 , '溫度')
        self.history_record_total_list_A('A', 4 , '濕度')
        self.history_record_total_list_A('A', 4 , '氨氣')
        self.history_record_total_list_A('A', 4 , '硫化氫')
        self.history_record_total_list_A('A', 4 , '大氣壓力')
        ### B area
        self.ui.history_query_result_list_B.clear()
        self.history_record_total_list_B('B', 5 , '溫度')
        self.history_record_total_list_B('B', 5 , '濕度')
        self.history_record_total_list_B('B', 5 , '氨氣')
        self.history_record_total_list_B('B', 5 , '硫化氫')
        self.history_record_total_list_B('B', 5 , '大氣壓力')
        self.history_record_total_list_B('B', 6 , '溫度')
        self.history_record_total_list_B('B', 6 , '濕度')
        self.history_record_total_list_B('B', 6 , '氨氣')
        self.history_record_total_list_B('B', 6 , '硫化氫')
        self.history_record_total_list_B('B', 6 , '大氣壓力')
        self.history_record_total_list_B('B', 7 , '溫度')
        self.history_record_total_list_B('B', 7 , '濕度')
        self.history_record_total_list_B('B', 7 , '氨氣')
        self.history_record_total_list_B('B', 7 , '硫化氫')
        self.history_record_total_list_B('B', 7 , '大氣壓力')
        ### C area
        self.ui.history_query_result_list_C.clear()
        self.history_record_total_list_C('C', 8 , '溫度')
        self.history_record_total_list_C('C', 8 , '濕度')
        self.history_record_total_list_C('C', 8 , '氨氣')
        self.history_record_total_list_C('C', 8 , '硫化氫')
        self.history_record_total_list_C('C', 8 , '大氣壓力')
        self.history_record_total_list_C('C', 9 , '溫度')
        self.history_record_total_list_C('C', 9 , '濕度')
        self.history_record_total_list_C('C', 9 , '氨氣')
        self.history_record_total_list_C('C', 9 , '硫化氫')
        self.history_record_total_list_C('C', 9 , '大氣壓力')
        self.history_record_total_list_C('C', 10 , '溫度')
        self.history_record_total_list_C('C', 10 , '濕度')
        self.history_record_total_list_C('C', 10, '氨氣')
        self.history_record_total_list_C('C', 10 , '硫化氫')
        self.history_record_total_list_C('C', 10 , '大氣壓力')
        self.history_record_total_list_C('C', 11 , '溫度')
        self.history_record_total_list_C('C', 11 , '濕度')
        self.history_record_total_list_C('C', 11 , '氨氣')
        self.history_record_total_list_C('C', 11 , '硫化氫')
        self.history_record_total_list_C('C', 11 , '大氣壓力')
        self.history_record_total_list_C('C', 12 , '溫度')
        self.history_record_total_list_C('C', 12 , '濕度')
        self.history_record_total_list_C('C', 12 , '氨氣')
        self.history_record_total_list_C('C', 12 , '硫化氫')
        self.history_record_total_list_C('C', 12 , '大氣壓力')
        ### D area
        self.ui.history_query_result_list_D.clear()
        self.history_record_total_list_D('D', 13 , '溫度')
        self.history_record_total_list_D('D', 13 , '濕度')
        self.history_record_total_list_D('D', 13 , '氨氣')
        self.history_record_total_list_D('D', 13 , '硫化氫')
        self.history_record_total_list_D('D', 13 , '大氣壓力')
        self.history_record_total_list_D('D', 14 , '溫度')
        self.history_record_total_list_D('D', 14 , '濕度')
        self.history_record_total_list_D('D', 14 , '氨氣')
        self.history_record_total_list_D('D', 14 , '硫化氫')
        self.history_record_total_list_D('D', 14 , '大氣壓力')
        self.history_record_total_list_D('D', 15 , '溫度')
        self.history_record_total_list_D('D', 15 , '濕度')
        self.history_record_total_list_D('D', 15 , '氨氣')
        self.history_record_total_list_D('D', 15 , '硫化氫')
        self.history_record_total_list_D('D', 15 , '大氣壓力')
        self.history_record_total_list_D('D', 16 , '溫度')
        self.history_record_total_list_D('D', 16 , '濕度')
        self.history_record_total_list_D('D', 16 , '氨氣')
        self.history_record_total_list_D('D', 16 , '硫化氫')
        self.history_record_total_list_D('D', 16 , '大氣壓力')
        ### E area
        self.ui.history_query_result_list_E.clear()
        self.history_record_total_list_E('E', 17 , '溫度')
        self.history_record_total_list_E('E', 17 , '濕度')
        self.history_record_total_list_E('E', 17 , '氨氣')
        self.history_record_total_list_E('E', 17 , '硫化氫')
        self.history_record_total_list_E('E', 17 , '大氣壓力')
        self.history_record_total_list_E('E', 18 , '溫度')
        self.history_record_total_list_E('E', 18 , '濕度')
        self.history_record_total_list_E('E', 18 , '氨氣')
        self.history_record_total_list_E('E', 18 , '硫化氫')
        self.history_record_total_list_E('E', 18 , '大氣壓力')
        self.history_record_total_list_E('E', 19 , '溫度')
        self.history_record_total_list_E('E', 19 , '濕度')
        self.history_record_total_list_E('E', 19 , '氨氣')
        self.history_record_total_list_E('E', 19 , '硫化氫')
        self.history_record_total_list_E('E', 19 , '大氣壓力')
        
    ################################
    # history record total list E
    ################################
    def history_record_total_list_E(self , area , id , item):
        
        try:

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb = self.n_time.toString("yyyy_MM")
            
            self.q_area = area
            self.q_id   = id
            self.q_item = item
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if self.q_item == '溫度':
                self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_E.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 溫度 ' + str(val[1]) + ' °C')
                
            elif self.q_item == '濕度':
                self.sql = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_E.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 濕度 ' + str(val[1]) + ' ％')
              
            elif self.q_item == '氨氣':
                self.sql = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_E.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 氨氣 ' + str(val[1]) + ' ppm')
             
            elif self.q_item == '硫化氫':
                self.sql = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_E.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 硫化氫 ' + str(val[1]) + ' ppm')
            
            elif self.q_item == '大氣壓力':
                self.sql = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_E.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 大氣壓力 ' + str(val[1]) + ' hPa')
                
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > history record total list E : ' + str(e))
        finally:
            pass
    
    ################################
    # history record total list D
    ################################
    def history_record_total_list_D(self , area , id , item):
        
        try:

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb = self.n_time.toString("yyyy_MM")
            
            self.q_area = area
            self.q_id   = id
            self.q_item = item
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if self.q_item == '溫度':
                self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_D.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 溫度 ' + str(val[1]) + ' °C')
                
            elif self.q_item == '濕度':
                self.sql = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_D.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 濕度 ' + str(val[1]) + ' ％')
              
            elif self.q_item == '氨氣':
                self.sql = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_D.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 氨氣 ' + str(val[1]) + ' ppm')
             
            elif self.q_item == '硫化氫':
                self.sql = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_D.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 硫化氫 ' + str(val[1]) + ' ppm')
            
            elif self.q_item == '大氣壓力':
                self.sql = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_D.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 大氣壓力 ' + str(val[1]) + ' hPa')
                
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > history record total list D : ' + str(e))
        finally:
            pass
    
    ################################
    # history record total list C
    ################################
    def history_record_total_list_C(self , area , id , item):
        try:

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb = self.n_time.toString("yyyy_MM")
            
            self.q_area = area
            self.q_id   = id
            self.q_item = item
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if self.q_item == '溫度':
                self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_C.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 溫度 ' + str(val[1]) + ' °C')
                
            elif self.q_item == '濕度':
                self.sql = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_C.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 濕度 ' + str(val[1]) + ' ％')
              
            elif self.q_item == '氨氣':
                self.sql = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_C.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 氨氣 ' + str(val[1]) + ' ppm')
             
            elif self.q_item == '硫化氫':
                self.sql = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_C.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 硫化氫 ' + str(val[1]) + ' ppm')
            
            elif self.q_item == '大氣壓力':
                self.sql = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_C.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 大氣壓力 ' + str(val[1]) + ' hPa')
                
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > history record total list C : ' + str(e))
        finally:
            pass

    ################################
    # history record total list B
    ################################
    def history_record_total_list_B(self , area , id , item):
        try:
            

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb = self.n_time.toString("yyyy_MM")
            
            self.q_area = area
            self.q_id   = id
            self.q_item = item
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if self.q_item == '溫度':
                self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_B.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 溫度 ' + str(val[1]) + ' °C')
                
            elif self.q_item == '濕度':
                self.sql = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_B.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 濕度 ' + str(val[1]) + ' ％')
              
            elif self.q_item == '氨氣':
                self.sql = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_B.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 氨氣 ' + str(val[1]) + ' ppm')
             
            elif self.q_item == '硫化氫':
                self.sql = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_B.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 硫化氫 ' + str(val[1]) + ' ppm')
            
            elif self.q_item == '大氣壓力':
                self.sql = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_B.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 大氣壓力 ' + str(val[1]) + ' hPa')
                
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > history record total list B : ' + str(e))
        finally:
            pass

    ################################
    # history record total list A
    ################################
    def history_record_total_list_A(self , area , id , item):
        try:
            
            
            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb = self.n_time.toString("yyyy_MM")
            
            self.q_area = area
            self.q_id   = id
            self.q_item = item
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if self.q_item == '溫度':
                self.sql = "select r_time , val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_A.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 溫度 ' + str(val[1]) + ' °C')
                
            elif self.q_item == '濕度':
                self.sql = "select r_time , val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_A.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 濕度 ' + str(val[1]) + ' ％')
              
            elif self.q_item == '氨氣':
                self.sql = "select r_time , val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_A.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 氨氣 ' + str(val[1]) + ' ppm')
             
            elif self.q_item == '硫化氫':
                self.sql = "select r_time , val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_A.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 硫化氫 ' + str(val[1]) + ' ppm')
            
            elif self.q_item == '大氣壓力':
                self.sql = "select r_time , val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.q_area , self.q_id)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.history_query_result_list_A.addItem(str(self.q_area) + ' 區 , sensor ' + str(self.q_id) + ' , ' + str(val[0]) + ' , 大氣壓力 ' + str(val[1]) + ' hPa')
                
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > history record total list A : ' + str(e))
        finally:
            pass

    #######################################
    # alter setup C area sensor 5 submit 
    #######################################
    def alter_setup_c_area_s_5_submit(self):
        
        ### variable
        self.area = 'c'
        self.id   = 12
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.c_s_temp_top_5.text()
        if self.ui.c_s_temp_top_manual_5.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.c_s_temp_top_auto_5.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.c_s_temp_top_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.c_s_temp_bottom_5.text()
        if self.ui.c_s_temp_bottom_manual_5.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.c_s_temp_bottom_auto_5.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.c_s_temp_bottom_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.c_s_rh_top_5.text()
        if self.ui.c_s_rh_top_manual_5.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.c_s_rh_top_auto_5.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.c_s_rh_top_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.c_s_rh_bottom_5.text()
        if self.ui.c_s_rh_bottom_manual_5.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.c_s_rh_bottom_auto_5.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.c_s_rh_bottom_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.c_s_nh3_top_5.text()
        if self.ui.c_s_nh3_top_manual_5.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.c_s_nh3_top_auto_5.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.c_s_nh3_top_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.c_s_nh3_bottom_5.text()
        if self.ui.c_s_nh3_bottom_manual_5.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.c_s_nh3_bottom_auto_5.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.c_s_nh3_bottom_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.c_s_h2s_top_5.text()
        if self.ui.c_s_h2s_top_manual_5.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.c_s_h2s_top_auto_5.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.c_s_h2s_top_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.c_s_h2s_bottom_5.text()
        if self.ui.c_s_h2s_bottom_manual_5.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.c_s_h2s_bottom_auto_5.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.c_s_h2s_bottom_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.c_s_pr_top_5.text()
        if self.ui.c_s_pr_top_manual_5.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.c_s_pr_top_auto_5.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.c_s_pr_top_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.c_s_pr_bottom_5.text()
        if self.ui.c_s_pr_bottom_manual_5.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.c_s_pr_bottom_auto_5.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.c_s_pr_bottom_device_5.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup D area sensor 4 submit 
    #######################################
    def alter_setup_d_area_s_4_submit(self):
        
        ### variable
        self.area = 'd'
        self.id   = 16
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.d_s_temp_top_4.text()
        if self.ui.d_s_temp_top_manual_4.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.d_s_temp_top_auto_4.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.d_s_temp_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.d_s_temp_bottom_4.text()
        if self.ui.d_s_temp_bottom_manual_4.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.d_s_temp_bottom_auto_4.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.d_s_temp_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.d_s_rh_top_4.text()
        if self.ui.d_s_rh_top_manual_4.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.d_s_rh_top_auto_4.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.d_s_rh_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.d_s_rh_bottom_4.text()
        if self.ui.d_s_rh_bottom_manual_4.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.d_s_rh_bottom_auto_4.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.d_s_rh_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.d_s_nh3_top_4.text()
        if self.ui.d_s_nh3_top_manual_4.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.d_s_nh3_top_auto_4.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.d_s_nh3_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.d_s_nh3_bottom_4.text()
        if self.ui.d_s_nh3_bottom_manual_4.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.d_s_nh3_bottom_auto_4.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.d_s_nh3_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.d_s_h2s_top_4.text()
        if self.ui.d_s_h2s_top_manual_4.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.d_s_h2s_top_auto_4.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.d_s_h2s_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.d_s_h2s_bottom_4.text()
        if self.ui.d_s_h2s_bottom_manual_4.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.d_s_h2s_bottom_auto_4.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.d_s_h2s_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.d_s_pr_top_4.text()
        if self.ui.d_s_pr_top_manual_4.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.d_s_pr_top_auto_4.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.d_s_pr_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.d_s_pr_bottom_4.text()
        if self.ui.d_s_pr_bottom_manual_4.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.d_s_pr_bottom_auto_4.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.d_s_pr_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup C area sensor 4 submit 
    #######################################
    def alter_setup_c_area_s_4_submit(self):
        
        ### variable
        self.area = 'c'
        self.id   = 11
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.c_s_temp_top_4.text()
        if self.ui.c_s_temp_top_manual_4.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.c_s_temp_top_auto_4.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.c_s_temp_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.c_s_temp_bottom_4.text()
        if self.ui.c_s_temp_bottom_manual_4.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.c_s_temp_bottom_auto_4.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.c_s_temp_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.c_s_rh_top_4.text()
        if self.ui.c_s_rh_top_manual_4.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.c_s_rh_top_auto_4.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.c_s_rh_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.c_s_rh_bottom_4.text()
        if self.ui.c_s_rh_bottom_manual_4.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.c_s_rh_bottom_auto_4.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.c_s_rh_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.c_s_nh3_top_4.text()
        if self.ui.c_s_nh3_top_manual_4.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.c_s_nh3_top_auto_4.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.c_s_nh3_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.c_s_nh3_bottom_4.text()
        if self.ui.c_s_nh3_bottom_manual_4.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.c_s_nh3_bottom_auto_4.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.c_s_nh3_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.c_s_h2s_top_4.text()
        if self.ui.c_s_h2s_top_manual_4.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.c_s_h2s_top_auto_4.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.c_s_h2s_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.c_s_h2s_bottom_4.text()
        if self.ui.c_s_h2s_bottom_manual_4.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.c_s_h2s_bottom_auto_4.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.c_s_h2s_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.c_s_pr_top_4.text()
        if self.ui.c_s_pr_top_manual_4.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.c_s_pr_top_auto_4.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.c_s_pr_top_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.c_s_pr_bottom_4.text()
        if self.ui.c_s_pr_bottom_manual_4.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.c_s_pr_bottom_auto_4.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.c_s_pr_bottom_device_4.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')


    #######################################
    # alter setup A area sensor 4 submit 
    #######################################
    def alter_setup_a_area_s_4_submit(self):
        
        ### variable
        self.area = 'a'
        self.id   = 4
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.a_s_4_temp_top.text()
        if self.ui.a_s_4_temp_top_manual.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.a_s_4_temp_top_auto.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.a_s_4_temp_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.a_s_4_temp_bottom.text()
        if self.ui.a_s_4_temp_bottom_manual.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.a_s_4_temp_bottom_auto.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.a_s_4_temp_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.a_s_4_rh_top.text()
        if self.ui.a_s_4_rh_top_manual.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.a_s_4_rh_top_auto.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.a_s_4_rh_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.a_s_4_rh_bottom.text()
        if self.ui.a_s_4_rh_bottom_manual.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.a_s_4_rh_bottom_auto.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.a_s_4_rh_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.a_s_4_nh3_top.text()
        if self.ui.a_s_4_nh3_top_manual.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.a_s_4_nh3_top_auto.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.a_s_4_nh3_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.a_s_4_nh3_bottom.text()
        if self.ui.a_s_4_nh3_bottom_manual.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.a_s_4_nh3_bottom_auto.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.a_s_4_nh3_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.a_s_4_h2s_top.text()
        if self.ui.a_s_4_h2s_top_manual.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.a_s_4_h2s_top_auto.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.a_s_4_h2s_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.a_s_4_h2s_bottom.text()
        if self.ui.a_s_4_h2s_bottom_manual.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.a_s_4_h2s_bottom_auto.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.a_s_4_h2s_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.a_s_4_pr_top.text()
        if self.ui.a_s_4_pr_top_manual.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.a_s_4_pr_top_auto.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.a_s_4_pr_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.a_s_4_pr_bottom.text()
        if self.ui.a_s_4_pr_bottom_manual.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.a_s_4_pr_bottom_auto.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.a_s_4_pr_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup E area sensor 3 submit 
    #######################################
    def alter_setup_e_area_s_3_submit(self):
        
        ### variable
        self.area = 'e'
        self.id   = 19
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.e_s_temp_top_3.text()
        if self.ui.e_s_temp_top_manual_3.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.e_s_temp_top_auto_3.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.e_s_temp_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.e_s_temp_bottom_3.text()
        if self.ui.e_s_temp_bottom_manual_3.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.e_s_temp_bottom_auto_3.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.e_s_temp_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.e_s_rh_top_3.text()
        if self.ui.e_s_rh_top_manual_3.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.e_s_rh_top_auto_3.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.e_s_rh_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.e_s_rh_bottom_3.text()
        if self.ui.e_s_rh_bottom_manual_3.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.e_s_rh_bottom_auto_3.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.e_s_rh_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.e_s_nh3_top_3.text()
        if self.ui.e_s_nh3_top_manual_3.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.e_s_nh3_top_auto_3.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.e_s_nh3_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.e_s_nh3_bottom_3.text()
        if self.ui.e_s_nh3_bottom_manual_3.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.e_s_nh3_bottom_auto_3.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.e_s_nh3_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.e_s_h2s_top_3.text()
        if self.ui.e_s_h2s_top_manual_3.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.e_s_h2s_top_auto_3.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.e_s_h2s_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.e_s_h2s_bottom_3.text()
        if self.ui.e_s_h2s_bottom_manual_3.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.e_s_h2s_bottom_auto_3.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.e_s_h2s_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.e_s_pr_top_3.text()
        if self.ui.e_s_pr_top_manual_3.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.e_s_pr_top_auto_3.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.e_s_pr_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.e_s_pr_bottom_3.text()
        if self.ui.e_s_pr_bottom_manual_3.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.e_s_pr_bottom_auto_3.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.e_s_pr_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup D area sensor 3 submit 
    #######################################
    def alter_setup_d_area_s_3_submit(self):
        
        ### variable
        self.area = 'd'
        self.id   = 15
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.d_s_temp_top_3.text()
        if self.ui.d_s_temp_top_manual_3.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.d_s_temp_top_auto_3.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.d_s_temp_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.d_s_temp_bottom_3.text()
        if self.ui.d_s_temp_bottom_manual_3.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.d_s_temp_bottom_auto_3.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.d_s_temp_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.d_s_rh_top_3.text()
        if self.ui.d_s_rh_top_manual_3.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.d_s_rh_top_auto_3.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.d_s_rh_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.d_s_rh_bottom_3.text()
        if self.ui.d_s_rh_bottom_manual_3.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.d_s_rh_bottom_auto_3.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.d_s_rh_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.d_s_nh3_top_3.text()
        if self.ui.d_s_nh3_top_manual_3.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.d_s_nh3_top_auto_3.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.d_s_nh3_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.d_s_nh3_bottom_3.text()
        if self.ui.d_s_nh3_bottom_manual_3.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.d_s_nh3_bottom_auto_3.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.d_s_nh3_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.d_s_h2s_top_3.text()
        if self.ui.d_s_h2s_top_manual_3.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.d_s_h2s_top_auto_3.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.d_s_h2s_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.d_s_h2s_bottom_3.text()
        if self.ui.d_s_h2s_bottom_manual_3.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.d_s_h2s_bottom_auto_3.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.d_s_h2s_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.d_s_pr_top_3.text()
        if self.ui.d_s_pr_top_manual_3.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.d_s_pr_top_auto_3.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.d_s_pr_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.d_s_pr_bottom_3.text()
        if self.ui.d_s_pr_bottom_manual_3.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.d_s_pr_bottom_auto_3.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.d_s_pr_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup C area sensor 3 submit 
    #######################################
    def alter_setup_c_area_s_3_submit(self):
        
        ### variable
        self.area = 'c'
        self.id   = 10
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.c_s_temp_top_3.text()
        if self.ui.c_s_temp_top_manual_3.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.c_s_temp_top_auto_3.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.c_s_temp_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.c_s_temp_bottom_3.text()
        if self.ui.c_s_temp_bottom_manual_3.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.c_s_temp_bottom_auto_3.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.c_s_temp_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.c_s_rh_top_3.text()
        if self.ui.c_s_rh_top_manual_3.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.c_s_rh_top_auto_3.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.c_s_rh_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.c_s_rh_bottom_3.text()
        if self.ui.c_s_rh_bottom_manual_3.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.c_s_rh_bottom_auto_3.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.c_s_rh_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.c_s_nh3_top_3.text()
        if self.ui.c_s_nh3_top_manual_3.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.c_s_nh3_top_auto_3.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.c_s_nh3_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.c_s_nh3_bottom_3.text()
        if self.ui.c_s_nh3_bottom_manual_3.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.c_s_nh3_bottom_auto_3.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.c_s_nh3_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.c_s_h2s_top_3.text()
        if self.ui.c_s_h2s_top_manual_3.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.c_s_h2s_top_auto_3.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.c_s_h2s_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.c_s_h2s_bottom_3.text()
        if self.ui.c_s_h2s_bottom_manual_3.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.c_s_h2s_bottom_auto_3.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.c_s_h2s_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.c_s_pr_top_3.text()
        if self.ui.c_s_pr_top_manual_3.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.c_s_pr_top_auto_3.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.c_s_pr_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.c_s_pr_bottom_3.text()
        if self.ui.c_s_pr_bottom_manual_3.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.c_s_pr_bottom_auto_3.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.c_s_pr_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')


    #######################################
    # alter setup B area sensor 3 submit 
    #######################################
    def alter_setup_b_area_s_3_submit(self):
        
        ### variable
        self.area = 'b'
        self.id   = 7
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.b_s_temp_top_3.text()
        if self.ui.b_s_temp_top_manual_3.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.b_s_temp_top_auto_3.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.b_s_temp_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.b_s_temp_bottom_3.text()
        if self.ui.b_s_temp_bottom_manual_3.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.b_s_temp_bottom_auto_3.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.b_s_temp_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.b_s_rh_top_3.text()
        if self.ui.b_s_rh_top_manual_3.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.b_s_rh_top_auto_3.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.b_s_rh_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.b_s_rh_bottom_3.text()
        if self.ui.b_s_rh_bottom_manual_3.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.b_s_rh_bottom_auto_3.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.b_s_rh_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.b_s_nh3_top_3.text()
        if self.ui.b_s_nh3_top_manual_3.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.b_s_nh3_top_auto_3.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.b_s_nh3_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.b_s_nh3_bottom_3.text()
        if self.ui.b_s_nh3_bottom_manual_3.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.b_s_nh3_bottom_auto_3.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.b_s_nh3_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.b_s_h2s_top_3.text()
        if self.ui.b_s_h2s_top_manual_3.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.b_s_h2s_top_auto_3.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.b_s_h2s_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.b_s_h2s_bottom_3.text()
        if self.ui.b_s_h2s_bottom_manual_3.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.b_s_h2s_bottom_auto_3.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.b_s_h2s_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.b_s_pr_top_3.text()
        if self.ui.b_s_pr_top_manual_3.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.b_s_pr_top_auto_3.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.b_s_pr_top_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.b_s_pr_bottom_3.text()
        if self.ui.b_s_pr_bottom_manual_3.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.b_s_pr_bottom_auto_3.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.b_s_pr_bottom_device_3.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup A area sensor 3 submit 
    #######################################
    def alter_setup_a_area_s_3_submit(self):
        
        ### variable
        self.area = 'a'
        self.id   = 3
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.a_s_3_temp_top.text()
        if self.ui.a_s_3_temp_top_manual.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.a_s_3_temp_top_auto.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.a_s_3_temp_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.a_s_3_temp_bottom.text()
        if self.ui.a_s_3_temp_bottom_manual.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.a_s_3_temp_bottom_auto.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.a_s_3_temp_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.a_s_3_rh_top.text()
        if self.ui.a_s_3_rh_top_manual.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.a_s_3_rh_top_auto.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.a_s_3_rh_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.a_s_3_rh_bottom.text()
        if self.ui.a_s_3_rh_bottom_manual.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.a_s_3_rh_bottom_auto.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.a_s_3_rh_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.a_s_3_nh3_top.text()
        if self.ui.a_s_3_nh3_top_manual.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.a_s_3_nh3_top_auto.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.a_s_3_nh3_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.a_s_3_nh3_bottom.text()
        if self.ui.a_s_3_nh3_bottom_manual.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.a_s_3_nh3_bottom_auto.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.a_s_3_nh3_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.a_s_3_h2s_top.text()
        if self.ui.a_s_3_h2s_top_manual.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.a_s_3_h2s_top_auto.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.a_s_3_h2s_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.a_s_3_h2s_bottom.text()
        if self.ui.a_s_3_h2s_bottom_manual.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.a_s_3_h2s_bottom_auto.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.a_s_3_h2s_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.a_s_3_pr_top.text()
        if self.ui.a_s_3_pr_top_manual.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.a_s_3_pr_top_auto.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.a_s_3_pr_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.a_s_3_pr_bottom.text()
        if self.ui.a_s_3_pr_bottom_manual.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.a_s_3_pr_bottom_auto.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.a_s_3_pr_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup E area sensor 2 submit 
    #######################################
    def alter_setup_e_area_s_2_submit(self):
        
        ### variable
        self.area = 'e'
        self.id   = 18
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.e_s_temp_top_2.text()
        if self.ui.e_s_temp_top_manual_2.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.e_s_temp_top_auto_2.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.e_s_temp_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.e_s_temp_bottom_2.text()
        if self.ui.e_s_temp_bottom_manual_2.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.e_s_temp_bottom_auto_2.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.e_s_temp_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.e_s_rh_top_2.text()
        if self.ui.e_s_rh_top_manual_2.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.e_s_rh_top_auto_2.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.e_s_rh_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.e_s_rh_bottom_2.text()
        if self.ui.e_s_rh_bottom_manual_2.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.e_s_rh_bottom_auto_2.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.e_s_rh_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.e_s_nh3_top_2.text()
        if self.ui.e_s_nh3_top_manual_2.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.e_s_nh3_top_auto_2.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.e_s_nh3_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.e_s_nh3_bottom_2.text()
        if self.ui.e_s_nh3_bottom_manual_2.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.e_s_nh3_bottom_auto_2.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.e_s_nh3_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.e_s_h2s_top_2.text()
        if self.ui.e_s_h2s_top_manual_2.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.e_s_h2s_top_auto_2.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.e_s_h2s_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.e_s_h2s_bottom_2.text()
        if self.ui.e_s_h2s_bottom_manual_2.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.e_s_h2s_bottom_auto_2.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.e_s_h2s_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.e_s_pr_top_2.text()
        if self.ui.e_s_pr_top_manual_2.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.e_s_pr_top_auto_2.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.e_s_pr_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.e_s_pr_bottom_2.text()
        if self.ui.e_s_pr_bottom_manual_2.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.e_s_pr_bottom_auto_2.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.e_s_pr_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup D area sensor 2 submit 
    #######################################
    def alter_setup_d_area_s_2_submit(self):
        
        ### variable
        self.area = 'd'
        self.id   = 14
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.d_s_temp_top_2.text()
        if self.ui.d_s_temp_top_manual_2.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.d_s_temp_top_auto_2.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.d_s_temp_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.d_s_temp_bottom_2.text()
        if self.ui.d_s_temp_bottom_manual_2.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.d_s_temp_bottom_auto_2.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.d_s_temp_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.d_s_rh_top_2.text()
        if self.ui.d_s_rh_top_manual_2.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.d_s_rh_top_auto_2.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.d_s_rh_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.d_s_rh_bottom_2.text()
        if self.ui.d_s_rh_bottom_manual_2.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.d_s_rh_bottom_auto_2.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.d_s_rh_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.d_s_nh3_top_2.text()
        if self.ui.d_s_nh3_top_manual_2.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.d_s_nh3_top_auto_2.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.d_s_nh3_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.d_s_nh3_bottom_2.text()
        if self.ui.d_s_nh3_bottom_manual_2.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.d_s_nh3_bottom_auto_2.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.d_s_nh3_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.d_s_h2s_top_2.text()
        if self.ui.d_s_h2s_top_manual_2.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.d_s_h2s_top_auto_2.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.d_s_h2s_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.d_s_h2s_bottom_2.text()
        if self.ui.d_s_h2s_bottom_manual_2.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.d_s_h2s_bottom_auto_2.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.d_s_h2s_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.d_s_pr_top_2.text()
        if self.ui.d_s_pr_top_manual_2.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.d_s_pr_top_auto_2.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.d_s_pr_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.d_s_pr_bottom_2.text()
        if self.ui.d_s_pr_bottom_manual_2.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.d_s_pr_bottom_auto_2.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.d_s_pr_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup C area sensor 2 submit 
    #######################################
    def alter_setup_c_area_s_2_submit(self):
        
        ### variable
        self.area = 'c'
        self.id   = 9
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.c_s_temp_top_2.text()
        if self.ui.c_s_temp_top_manual_2.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.c_s_temp_top_auto_2.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.c_s_temp_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.c_s_temp_bottom_2.text()
        if self.ui.c_s_temp_bottom_manual_2.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.c_s_temp_bottom_auto_2.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.c_s_temp_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.c_s_rh_top_2.text()
        if self.ui.c_s_rh_top_manual_2.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.c_s_rh_top_auto_2.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.c_s_rh_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.c_s_rh_bottom_2.text()
        if self.ui.c_s_rh_bottom_manual_2.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.c_s_rh_bottom_auto_2.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.c_s_rh_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.c_s_nh3_top_2.text()
        if self.ui.c_s_nh3_top_manual_2.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.c_s_nh3_top_auto_2.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.c_s_nh3_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.c_s_nh3_bottom_2.text()
        if self.ui.c_s_nh3_bottom_manual_2.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.c_s_nh3_bottom_auto_2.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.c_s_nh3_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.c_s_h2s_top_2.text()
        if self.ui.c_s_h2s_top_manual_2.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.c_s_h2s_top_auto_2.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.c_s_h2s_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.c_s_h2s_bottom_2.text()
        if self.ui.c_s_h2s_bottom_manual_2.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.c_s_h2s_bottom_auto_2.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.c_s_h2s_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.c_s_pr_top_2.text()
        if self.ui.c_s_pr_top_manual_2.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.c_s_pr_top_auto_2.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.c_s_pr_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.c_s_pr_bottom_2.text()
        if self.ui.c_s_pr_bottom_manual_2.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.c_s_pr_bottom_auto_2.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.c_s_pr_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup B area sensor 2 submit 
    #######################################
    def alter_setup_b_area_s_2_submit(self):
        
        ### variable
        self.area = 'b'
        self.id   = 6
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.b_s_temp_top_2.text()
        if self.ui.b_s_temp_top_manual_2.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.b_s_temp_top_auto_2.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.b_s_temp_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.b_s_temp_bottom_2.text()
        if self.ui.b_s_temp_bottom_manual_2.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.b_s_temp_bottom_auto_2.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.b_s_temp_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.b_s_rh_top_2.text()
        if self.ui.b_s_rh_top_manual_2.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.b_s_rh_top_auto_2.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.b_s_rh_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.b_s_rh_bottom_2.text()
        if self.ui.b_s_rh_bottom_manual_2.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.b_s_rh_bottom_auto_2.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.b_s_rh_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.b_s_nh3_top_2.text()
        if self.ui.b_s_nh3_top_manual_2.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.b_s_nh3_top_auto_2.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.b_s_nh3_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.b_s_nh3_bottom_2.text()
        if self.ui.b_s_nh3_bottom_manual_2.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.b_s_nh3_bottom_auto_2.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.b_s_nh3_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.b_s_h2s_top_2.text()
        if self.ui.b_s_h2s_top_manual_2.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.b_s_h2s_top_auto_2.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.b_s_h2s_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.b_s_h2s_bottom_2.text()
        if self.ui.b_s_h2s_bottom_manual_2.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.b_s_h2s_bottom_auto_2.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.b_s_h2s_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.b_s_pr_top_2.text()
        if self.ui.b_s_pr_top_manual_2.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.b_s_pr_top_auto_2.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.b_s_pr_top_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.b_s_pr_bottom_2.text()
        if self.ui.b_s_pr_bottom_manual_2.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.b_s_pr_bottom_auto_2.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.b_s_pr_bottom_device_2.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup A area sensor 2 submit 
    #######################################
    def alter_setup_a_area_s_2_submit(self):
        
        ### variable
        self.area = 'a'
        self.id   = 2
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.a_s_2_temp_top.text()
        if self.ui.a_s_2_temp_top_manual.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.a_s_2_temp_top_auto.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.a_s_2_temp_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.a_s_2_temp_bottom.text()
        if self.ui.a_s_2_temp_bottom_manual.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.a_s_2_temp_bottom_auto.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.a_s_2_temp_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.a_s_2_rh_top.text()
        if self.ui.a_s_2_rh_top_manual.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.a_s_2_rh_top_auto.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.a_s_2_rh_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.a_s_2_rh_bottom.text()
        if self.ui.a_s_2_rh_bottom_manual.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.a_s_2_rh_bottom_auto.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.a_s_2_rh_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.a_s_2_nh3_top.text()
        if self.ui.a_s_2_nh3_top_manual.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.a_s_2_nh3_top_auto.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.a_s_2_nh3_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.a_s_2_nh3_bottom.text()
        if self.ui.a_s_2_nh3_bottom_manual.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.a_s_2_nh3_bottom_auto.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.a_s_2_nh3_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.a_s_2_h2s_top.text()
        if self.ui.a_s_2_h2s_top_manual.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.a_s_2_h2s_top_auto.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.a_s_2_h2s_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.a_s_2_h2s_bottom.text()
        if self.ui.a_s_2_h2s_bottom_manual.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.a_s_2_h2s_bottom_auto.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.a_s_2_h2s_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.a_s_2_pr_top.text()
        if self.ui.a_s_2_pr_top_manual.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.a_s_2_pr_top_auto.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.a_s_2_pr_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.a_s_2_pr_bottom.text()
        if self.ui.a_s_2_pr_bottom_manual.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.a_s_2_pr_bottom_auto.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.a_s_2_pr_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup E area sensor 1 submit 
    #######################################
    def alter_setup_e_area_s_1_submit(self):
        
        ### variable
        self.area = 'e'
        self.id   = 17
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.e_s_temp_top_1.text()
        if self.ui.e_s_temp_top_manual_1.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.e_s_temp_top_auto_1.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.e_s_temp_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.e_s_temp_bottom_1.text()
        if self.ui.e_s_temp_bottom_manual_1.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.e_s_temp_bottom_auto_1.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.e_s_temp_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.e_s_rh_top_1.text()
        if self.ui.e_s_rh_top_manual_1.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.e_s_rh_top_auto_1.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.e_s_rh_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.e_s_rh_bottom_1.text()
        if self.ui.e_s_rh_bottom_manual_1.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.e_s_rh_bottom_auto_1.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.e_s_rh_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.e_s_nh3_top_1.text()
        if self.ui.e_s_nh3_top_manual_1.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.e_s_nh3_top_auto_1.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.e_s_nh3_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.e_s_nh3_bottom_1.text()
        if self.ui.e_s_nh3_bottom_manual_1.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.e_s_nh3_bottom_auto_1.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.e_s_nh3_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.e_s_h2s_top_1.text()
        if self.ui.e_s_h2s_top_manual_1.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.e_s_h2s_top_auto_1.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.e_s_h2s_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.e_s_h2s_bottom_1.text()
        if self.ui.e_s_h2s_bottom_manual_1.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.e_s_h2s_bottom_auto_1.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.e_s_h2s_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.e_s_pr_top_1.text()
        if self.ui.e_s_pr_top_manual_1.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.e_s_pr_top_auto_1.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.e_s_pr_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.e_s_pr_bottom_1.text()
        if self.ui.e_s_pr_bottom_manual_1.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.e_s_pr_bottom_auto_1.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.e_s_pr_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup D area sensor 1 submit 
    #######################################
    def alter_setup_d_area_s_1_submit(self):
        
        ### variable
        self.area = 'd'
        self.id   = 13
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.e_s_temp_top_1.text()
        if self.ui.e_s_temp_top_manual_1.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.e_s_temp_top_auto_1.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.e_s_temp_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.e_s_temp_bottom_1.text()
        if self.ui.e_s_temp_bottom_manual_1.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.e_s_temp_bottom_auto_1.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.e_s_temp_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.e_s_rh_top_1.text()
        if self.ui.e_s_rh_top_manual_1.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.e_s_rh_top_auto_1.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.e_s_rh_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.e_s_rh_bottom_1.text()
        if self.ui.e_s_rh_bottom_manual_1.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.e_s_rh_bottom_auto_1.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.e_s_rh_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.e_s_nh3_top_1.text()
        if self.ui.e_s_nh3_top_manual_1.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.e_s_nh3_top_auto_1.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.e_s_nh3_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.e_s_nh3_bottom_1.text()
        if self.ui.e_s_nh3_bottom_manual_1.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.e_s_nh3_bottom_auto_1.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.e_s_nh3_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.e_s_h2s_top_1.text()
        if self.ui.e_s_h2s_top_manual_1.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.e_s_h2s_top_auto_1.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.e_s_h2s_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.e_s_h2s_bottom_1.text()
        if self.ui.e_s_h2s_bottom_manual_1.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.e_s_h2s_bottom_auto_1.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.e_s_h2s_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.e_s_pr_top_1.text()
        if self.ui.e_s_pr_top_manual_1.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.e_s_pr_top_auto_1.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.e_s_pr_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.e_s_pr_bottom_1.text()
        if self.ui.e_s_pr_bottom_manual_1.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.e_s_pr_bottom_auto_1.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.e_s_pr_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup C area sensor 1 submit 
    #######################################
    def alter_setup_c_area_s_1_submit(self):
        
        ### variable
        self.area = 'c'
        self.id   = 8
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.c_s_temp_top_1.text()
        if self.ui.c_s_temp_top_manual_1.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.c_s_temp_top_auto_1.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.c_s_temp_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.c_s_temp_bottom_1.text()
        if self.ui.c_s_temp_bottom_manual_1.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.c_s_temp_bottom_auto_1.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.c_s_temp_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.c_s_rh_top_1.text()
        if self.ui.c_s_rh_top_manual_1.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.c_s_rh_top_auto_1.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.c_s_rh_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.c_s_rh_bottom_1.text()
        if self.ui.c_s_rh_bottom_manual_1.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.c_s_rh_bottom_auto_1.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.c_s_rh_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.c_s_nh3_top_1.text()
        if self.ui.c_s_nh3_top_manual_1.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.c_s_nh3_top_auto_1.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.c_s_nh3_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.c_s_nh3_bottom_1.text()
        if self.ui.c_s_nh3_bottom_manual_1.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.c_s_nh3_bottom_auto_1.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.c_s_nh3_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.c_s_h2s_top_1.text()
        if self.ui.c_s_h2s_top_manual_1.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.c_s_h2s_top_auto_1.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.c_s_h2s_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.c_s_h2s_bottom_1.text()
        if self.ui.c_s_h2s_bottom_manual_1.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.c_s_h2s_bottom_auto_1.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.c_s_h2s_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.c_s_pr_top_1.text()
        if self.ui.c_s_pr_top_manual_1.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.c_s_pr_top_auto_1.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.c_s_pr_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.c_s_pr_bottom_1.text()
        if self.ui.c_s_pr_bottom_manual_1.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.c_s_pr_bottom_auto_1.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.c_s_pr_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup B area sensor 1 submit 
    #######################################
    def alter_setup_b_area_s_1_submit(self):
        
        ### variable
        self.area = 'b'
        self.id   = 5
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.b_s_temp_top_1.text()
        if self.ui.b_s_temp_top_manual_1.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.b_s_temp_top_auto_1.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.b_s_temp_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.b_s_temp_bottom_1.text()
        if self.ui.b_s_temp_bottom_manual_1.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.b_s_temp_bottom_auto_1.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.b_s_temp_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.b_s_rh_top_1.text()
        if self.ui.b_s_rh_top_manual_1.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.b_s_rh_top_auto_1.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.b_s_rh_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.b_s_rh_bottom_1.text()
        if self.ui.b_s_rh_bottom_manual_1.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.b_s_rh_bottom_auto_1.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.b_s_rh_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.b_s_nh3_top_1.text()
        if self.ui.b_s_nh3_top_manual_1.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.b_s_nh3_top_auto_1.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.b_s_nh3_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.b_s_nh3_bottom_1.text()
        if self.ui.b_s_nh3_bottom_manual_1.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.b_s_nh3_bottom_auto_1.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.b_s_nh3_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.b_s_h2s_top_1.text()
        if self.ui.b_s_h2s_top_manual_1.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.b_s_h2s_top_auto_1.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.b_s_h2s_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.b_s_h2s_bottom_1.text()
        if self.ui.b_s_h2s_bottom_manual_1.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.b_s_h2s_bottom_auto_1.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.b_s_h2s_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.b_s_pr_top_1.text()
        if self.ui.b_s_pr_top_manual_1.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.b_s_pr_top_auto_1.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.b_s_pr_top_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.b_s_pr_bottom_1.text()
        if self.ui.b_s_pr_bottom_manual_1.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.b_s_pr_bottom_auto_1.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.b_s_pr_bottom_device_1.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')

    #######################################
    # alter setup A area sensor 1 submit 
    #######################################
    def alter_setup_a_area_s_1_submit(self):
        
        ### variable
        self.area = 'a'
        self.id   = 1
        
        ### record time
        self.n_time = QDateTime.currentDateTime()
        self.r_n_time = self.n_time.toString("yyyy-MM-dd HH:mm:ss")

        ###############
        # temp - top
        ###############
        self.temp_top = self.ui.a_s_1_temp_top.text()
        if self.ui.a_s_1_temp_top_manual.isChecked():
            self.temp_top_manual = 'enable'
            self.temp_top_auto = ''
        elif self.ui.a_s_1_temp_top_auto.isChecked():
            self.temp_top_manual = ''
            self.temp_top_auto = 'enable'
        self.temp_top_device = self.ui.a_s_1_temp_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'top' , self.r_n_time , s_user , self.temp_top , self.temp_top_auto , self.temp_top_manual , self.temp_top_device)

        ##################
        # temp - bottom
        ##################
        self.temp_bottom = self.ui.a_s_1_temp_bottom.text()
        if self.ui.a_s_1_temp_bottom_manual.isChecked():
            self.temp_bottom_manual = 'enable'
            self.temp_bottom_auto = ''
        elif self.ui.a_s_1_temp_bottom_auto.isChecked():
            self.temp_bottom_manual = ''
            self.temp_bottom_auto = 'enable'
        self.temp_bottom_device = self.ui.a_s_1_temp_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'temp' , 'bottom' , self.r_n_time , s_user , self.temp_bottom , self.temp_bottom_auto , self.temp_bottom_manual , self.temp_bottom_device)

        #############
        # rh - top
        #############
        self.rh_top = self.ui.a_s_1_rh_top.text()
        if self.ui.a_s_1_rh_top_manual.isChecked():
            self.rh_top_manual = 'enable'
            self.rh_top_auto = ''
        elif self.ui.a_s_1_rh_top_auto.isChecked():
            self.rh_top_manual = ''
            self.rh_top_auto = 'enable'
        self.rh_top_device = self.ui.a_s_1_rh_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'top' , self.r_n_time , s_user , self.rh_top , self.rh_top_auto , self.rh_top_manual , self.rh_top_device)
        
        ################
        # rh - bottom
        ################
        self.rh_bottom = self.ui.a_s_1_rh_bottom.text()
        if self.ui.a_s_1_rh_bottom_manual.isChecked():
            self.rh_bottom_manual = 'enable'
            self.rh_bottom_auto = ''
        elif self.ui.a_s_1_rh_bottom_auto.isChecked():
            self.rh_bottom_manual = ''
            self.rh_bottom_auto = 'enable'
        self.rh_bottom_device = self.ui.a_s_1_rh_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'rh' , 'bottom' , self.r_n_time , s_user , self.rh_bottom , self.rh_bottom_auto , self.rh_bottom_manual , self.rh_bottom_device)

        ##############
        # nh3 - top
        ##############
        self.nh3_top = self.ui.a_s_1_nh3_top.text()
        if self.ui.a_s_1_nh3_top_manual.isChecked():
            self.nh3_top_manual = 'enable'
            self.nh3_top_auto = ''
        elif self.ui.a_s_1_nh3_top_auto.isChecked():
            self.nh3_top_manual = ''
            self.nh3_top_auto = 'enable'
        self.nh3_top_device = self.ui.a_s_1_nh3_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'top' , self.r_n_time , s_user , self.nh3_top , self.nh3_top_auto , self.nh3_top_manual , self.nh3_top_device)

        #################
        # nh3 - bottom
        #################
        self.nh3_bottom = self.ui.a_s_1_nh3_bottom.text()
        if self.ui.a_s_1_nh3_bottom_manual.isChecked():
            self.nh3_bottom_manual = 'enable'
            self.nh3_bottom_auto = ''
        elif self.ui.a_s_1_nh3_bottom_auto.isChecked():
            self.nh3_bottom_manual = ''
            self.nh3_bottom_auto = 'enable'
        self.nh3_bottom_device = self.ui.a_s_1_nh3_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'nh3' , 'bottom' , self.r_n_time , s_user , self.nh3_bottom , self.nh3_bottom_auto , self.nh3_bottom_manual , self.nh3_bottom_device)

        ##############
        # h2s - top
        ##############
        self.h2s_top = self.ui.a_s_1_h2s_top.text()
        if self.ui.a_s_1_h2s_top_manual.isChecked():
            self.h2s_top_manual = 'enable'
            self.h2s_top_auto = ''
        elif self.ui.a_s_1_h2s_top_auto.isChecked():
            self.h2s_top_manual = ''
            self.h2s_top_auto = 'enable'
        self.h2s_top_device = self.ui.a_s_1_h2s_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'top' , self.r_n_time , s_user , self.h2s_top , self.h2s_top_auto , self.h2s_top_manual , self.h2s_top_device)
        #################
        # h2s - bottom
        #################
        self.h2s_bottom = self.ui.a_s_1_h2s_bottom.text()
        if self.ui.a_s_1_h2s_bottom_manual.isChecked():
            self.h2s_bottom_manual = 'enable'
            self.h2s_bottom_auto = ''
        elif self.ui.a_s_1_h2s_bottom_auto.isChecked():
            self.h2s_bottom_manual = ''
            self.h2s_bottom_auto = 'enable'
        self.h2s_bottom_device = self.ui.a_s_1_h2s_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'h2s' , 'bottom' , self.r_n_time , s_user , self.h2s_bottom , self.h2s_bottom_auto , self.h2s_bottom_manual , self.h2s_bottom_device)

        #############
        # pr - top
        #############
        self.pr_top = self.ui.a_s_1_pr_top.text()
        if self.ui.a_s_1_pr_top_manual.isChecked():
            self.pr_top_manual = 'enable'
            self.pr_top_auto = ''
        elif self.ui.a_s_1_pr_top_auto.isChecked():
            self.pr_top_manual = ''
            self.pr_top_auto = 'enable'
        self.pr_top_device = self.ui.a_s_1_pr_top_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'top' , self.r_n_time , s_user , self.pr_top , self.pr_top_auto , self.pr_top_manual , self.pr_top_device)
        ################
        # pr - bottom
        ################
        self.pr_bottom = self.ui.a_s_1_pr_bottom.text()
        if self.ui.a_s_1_pr_bottom_manual.isChecked():
            self.pr_bottom_manual = 'enable'
            self.pr_bottom_auto = ''
        elif self.ui.a_s_1_pr_bottom_auto.isChecked():
            self.pr_bottom_manual = ''
            self.pr_bottom_auto = 'enable'
        self.pr_bottom_device = self.ui.a_s_1_pr_bottom_device.text()
        
        self.update_setup_sensor_para(self.area , self.id , 'pr' , 'bottom' , self.r_n_time , s_user , self.pr_bottom , self.pr_bottom_auto , self.pr_bottom_manual , self.pr_bottom_device)
        
        ### work record
        self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , ' + str(self.area)  + ' 區 sensor ' + str(self.id) +  ' 更新設定成功')
        ### show message 
        QMessageBox.information(self , 'Msg' ,  str(self.area) + ' 區 sensor ' + str(self.id) + ' 更新設定成功')


    #############################
    # update setup sensor para
    #############################
    def update_setup_sensor_para(self , s_area , s_id , s_item , s_position , r_time , a_user , s_alarm_val , s_val_auto_run , s_val_manual_run , s_alarm_val_device):
        
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            if s_position == 'top':
                self.sql = "update setup_record set r_time='{0}' , a_user='{1}' , s_alarm_top='{2}' , s_top_auto_run='{3}' , s_top_manual_run='{4}' , s_alarm_top_device='{5}' where s_id='{6}' and s_item='{7}' and s_area='{8}' and s_position='{9}'".format(r_time , a_user , s_alarm_val , s_val_auto_run , s_val_manual_run , s_alarm_val_device , s_id , s_item , s_area , s_position)
            elif s_position == 'bottom':
                self.sql = "update setup_record set r_time='{0}' , a_user='{1}' , s_alarm_bottom='{2}' , s_bottom_auto_run='{3}' , s_bottom_manual_run='{4}' , s_alarm_bottom_device='{5}' where s_id='{6}' and s_item='{7}' and s_area='{8}' and s_position='{9}'".format(r_time , a_user , s_alarm_val , s_val_auto_run , s_val_manual_run , s_alarm_val_device , s_id , s_item , s_area , s_position)

            self.res = self.curr.execute(self.sql)
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > update setup sensor para : ' + str(e))
        finally:
            pass

    ###########
    # logout
    ###########
    def logout(self):
        try:
            self.logout = QDateTime.currentDateTime()
            self.logout_time = self.logout.toString("yyyy-MM-dd HH:mm:ss") 

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "update in_out_record set logout_time='{0}' where a_user='{1}' and login_code='{2}'".format(self.logout_time , s_user , s_login_code)
            self.res = self.curr.execute(self.sql)
            self.conn.commit()

            if self.res:

                ### work record
                self.work_record(s_user , '日誌 - 帳號 : ' + s_user + ' , 登出成功')

                QMessageBox.information(self , 'Msg' , '帳號 : ' + str(s_user) + ' , ' + str(self.logout_time) + ' 登出成功')
                QApplication.closeAllWindows()

        except Exception as e:
            self.conn.close()
            QMessageBox.information(self , 'Msg' , '< Error > logout : ' + str(e))
        finally:
            pass

    ########################
    # page 3 setup E area
    ########################
    def page_3_setup_E_area(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3_setup_E_area)
        if s_lv == '1':
            ### d area setup
            self.e_area_setup()

        elif s_lv == '2':
            ### d area setup
            self.e_area_setup()

        elif s_lv == '3':
            self.ui.tabWidget_5.setEnabled(False)
            self.ui.tabWidget_5.setCurrentIndex(0)
    
    ########################
    # page 3 setup D area
    ########################
    def page_3_setup_D_area(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3_setup_D_area)
        if s_lv == '1':
            ### d area setup
            self.d_area_setup()

        elif s_lv == '2':
            ### d area setup
            self.d_area_setup()

        elif s_lv == '3':
            self.ui.tabWidget_4.setEnabled(False)
            self.ui.tabWidget_4.setCurrentIndex(0)
    
    ########################
    # page 3 setup C area
    ########################
    def page_3_setup_C_area(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3_setup_C_area)
        if s_lv == '1':
            ### c area setup
            self.c_area_setup()

        elif s_lv == '2':
            ### c area setup
            self.c_area_setup()

        elif s_lv == '3':
            self.ui.tabWidget_3.setEnabled(False)
            self.ui.tabWidget_3.setCurrentIndex(0)

    ########################
    # page 3 setup B area
    ########################
    def page_3_setup_B_area(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3_setup_B_area)
        if s_lv == '1':
            ### b area setup
            self.b_area_setup()

        elif s_lv == '2':
            ### b area setup
            self.b_area_setup()
            
        elif s_lv == '3':
            self.ui.tabWidget_2.setEnabled(False)
            self.ui.tabWidget_2.setCurrentIndex(0)

    ########################
    # page 3 setup A area
    ########################
    def page_3_setup_A_area(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3_setup_A_area)

        if s_lv == '1':
            ### A area setup
            self.a_area_setup()

        elif s_lv == '2':
            ### A area setup
            self.a_area_setup()

        elif s_lv == '3':
            self.ui.tabWidget.setEnabled(False)
            self.ui.tabWidget.setCurrentIndex(0)

    #################
    # e area setup   
    ################# 
    def e_area_setup(self):
        
        ### select tabwidgets page 1
        self.ui.tabWidget.setCurrentIndex(0)

        ### e area setup sensor 1 button group
        self.e_area_setup_sensor_1_btn_group()
        ### e area setup sensor 2 button group
        self.e_area_setup_sensor_2_btn_group()
        ### e area setup sensor 3 button group
        self.e_area_setup_sensor_3_btn_group()
        
        ### e area sensor 1 load setup para
        self.e_area_sensor_1_load_setup()
        ### e area sensor 2 load setup para
        self.e_area_sensor_2_load_setup()
        ### e area sensor 3 load setup para
        self.e_area_sensor_3_load_setup()  
    
    #################
    # d area setup   
    ################# 
    def d_area_setup(self):
        
        ### select tabwidgets page 1
        self.ui.tabWidget.setCurrentIndex(0)

        ### d area setup sensor 1 button group
        self.d_area_setup_sensor_1_btn_group()
        ### d area setup sensor 2 button group
        self.d_area_setup_sensor_2_btn_group()
        ### d area setup sensor 3 button group
        self.d_area_setup_sensor_3_btn_group()
        ### d area setup sensor 4 button group
        self.d_area_setup_sensor_4_btn_group()
        
        ### d area sensor 1 load setup para
        self.d_area_sensor_1_load_setup()
        ### d area sensor 2 load setup para
        self.d_area_sensor_2_load_setup()
        ### d area sensor 3 load setup para
        self.d_area_sensor_3_load_setup()  
        ### d area sensor 4 load setup para
        self.d_area_sensor_4_load_setup()  

    #################
    # c area setup   
    ################# 
    def c_area_setup(self):
        
        ### select tabwidgets page 1
        self.ui.tabWidget.setCurrentIndex(0)

        ### c area setup sensor 1 button group
        self.c_area_setup_sensor_1_btn_group()
        ### c area setup sensor 2 button group
        self.c_area_setup_sensor_2_btn_group()
        ### c area setup sensor 3 button group
        self.c_area_setup_sensor_3_btn_group()
        ### c area setup sensor 4 button group
        self.c_area_setup_sensor_4_btn_group()
        ### c area setup sensor 5 button group
        self.c_area_setup_sensor_5_btn_group()
        
        ### c area sensor 1 load setup para
        self.c_area_sensor_1_load_setup()
        ### c area sensor 2 load setup para
        self.c_area_sensor_2_load_setup()
        ### c area sensor 3 load setup para
        self.c_area_sensor_3_load_setup()  
        ### c area sensor 4 load setup para
        self.c_area_sensor_4_load_setup()  
        ### c area sensor 5 load setup para
        self.c_area_sensor_5_load_setup()  

    #################
    # b area setup   
    ################# 
    def b_area_setup(self):
        
        ### select tabwidgets page 1
        self.ui.tabWidget.setCurrentIndex(0)

        ### b area setup sensor 1 button group
        self.b_area_setup_sensor_1_btn_group()
        ### b area setup sensor 2 button group
        self.b_area_setup_sensor_2_btn_group()
        ### b area setup sensor 3 button group
        self.b_area_setup_sensor_3_btn_group()
        
        ### b area sensor 1 load setup para
        self.b_area_sensor_1_load_setup()
        ### b area sensor 2 load setup para
        self.b_area_sensor_2_load_setup()
        ### b area sensor 3 load setup para
        self.b_area_sensor_3_load_setup()  

    #################
    # a area setup   
    ################# 
    def a_area_setup(self):
        
        ### select tabwidgets page 1
        self.ui.tabWidget.setCurrentIndex(0)

        ### a area setup sensor 1 button group
        self.a_area_setup_sensor_1_btn_group()
        ### a area setup sensor 2 button group
        self.a_area_setup_sensor_2_btn_group()
        ### a area setup sensor 3 button group
        self.a_area_setup_sensor_3_btn_group()
        ### a area setup sensor 4 button group
        self.a_area_setup_sensor_4_btn_group()
        
        ### a area sensor 1 load setup para
        self.a_area_sensor_1_load_setup()
        ### a area sensor 2 load setup para
        self.a_area_sensor_2_load_setup()
        ### a area sensor 3 load setup para
        self.a_area_sensor_3_load_setup()
        ### a area sensor 4 load setup para
        self.a_area_sensor_4_load_setup()
        

    #######################
    # page 2 work record 
    #######################
    def page_2_work_record(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2_work_record)

    ###################
    # page 1 account 
    ###################
    def page_1_account(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1_account)

    ###############################
    # C area sensor 5 load setup 
    ###############################
    def c_area_sensor_5_load_setup(self):
        
        ########################
        # sensor 5 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='12' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_pr_top_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_top_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_top_manual_5.setChecked(True)
                self.ui.c_s_pr_top_device_5.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='12' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_pr_bottom_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_bottom_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_bottom_manual_5.setChecked(True)
                self.ui.c_s_pr_bottom_device_5.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 5 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 5 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='12' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_h2s_top_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_top_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_top_manual_5.setChecked(True)
                self.ui.c_s_h2s_top_device_5.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='12' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_h2s_bottom_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_bottom_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_bottom_manual_5.setChecked(True)
                self.ui.c_s_h2s_bottom_device_5.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 5 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 5 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='12' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_nh3_top_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_top_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_top_manual_5.setChecked(True)
                self.ui.c_s_nh3_top_device_5.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='12' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_nh3_bottom_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_bottom_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_bottom_manual_5.setChecked(True)
                self.ui.c_s_nh3_bottom_device_5.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 5 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 5 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='12' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_rh_top_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_top_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_top_manual_5.setChecked(True)
                self.ui.c_s_rh_top_device_5.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='12' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_rh_bottom_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_bottom_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_bottom_manual_5.setChecked(True)
                self.ui.c_s_rh_bottom_device_5.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 5 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 5 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='12' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_temp_top_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_top_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_top_manual_5.setChecked(True)
                self.ui.c_s_temp_top_device_5.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='12' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_temp_bottom_5.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_bottom_auto_5.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_bottom_manual_5.setChecked(True)
                self.ui.c_s_temp_bottom_device_5.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 5 temp : ' + str(e))
        finally:
            pass
    
    ###############################
    # D area sensor 4 load setup 
    ###############################
    def d_area_sensor_4_load_setup(self):
        
        ########################
        # sensor 4 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='16' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_pr_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_top_manual_4.setChecked(True)
                self.ui.d_s_pr_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='16' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_pr_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_bottom_manual_4.setChecked(True)
                self.ui.d_s_pr_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 4 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='16' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_h2s_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_top_manual_4.setChecked(True)
                self.ui.d_s_h2s_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='16' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_h2s_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_bottom_manual_4.setChecked(True)
                self.ui.d_s_h2s_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 4 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='16' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_nh3_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_top_manual_4.setChecked(True)
                self.ui.d_s_nh3_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='16' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_nh3_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_bottom_manual_4.setChecked(True)
                self.ui.d_s_nh3_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 4 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='16' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_rh_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_top_manual_4.setChecked(True)
                self.ui.d_s_rh_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='16' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_rh_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_bottom_manual_4.setChecked(True)
                self.ui.d_s_rh_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 4 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 4 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='16' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_temp_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_top_manual_4.setChecked(True)
                self.ui.d_s_temp_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='16' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_temp_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_bottom_manual_4.setChecked(True)
                self.ui.d_s_temp_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 4 temp : ' + str(e))
        finally:
            pass

    ###############################
    # C area sensor 4 load setup 
    ###############################
    def c_area_sensor_4_load_setup(self):
        
        ########################
        # sensor 4 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='11' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_pr_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_top_manual_4.setChecked(True)
                self.ui.c_s_pr_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='11' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_pr_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_bottom_manual_4.setChecked(True)
                self.ui.c_s_pr_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 4 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='11' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_h2s_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_top_manual_4.setChecked(True)
                self.ui.c_s_h2s_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='11' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_h2s_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_bottom_manual_4.setChecked(True)
                self.ui.c_s_h2s_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 4 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='11' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_nh3_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_top_manual_4.setChecked(True)
                self.ui.c_s_nh3_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='11' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_nh3_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_bottom_manual_4.setChecked(True)
                self.ui.c_s_nh3_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 4 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='11' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_rh_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_top_manual_4.setChecked(True)
                self.ui.c_s_rh_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='11' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_rh_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_bottom_manual_4.setChecked(True)
                self.ui.c_s_rh_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 4 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 4 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='11' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_temp_top_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_top_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_top_manual_4.setChecked(True)
                self.ui.c_s_temp_top_device_4.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='11' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_temp_bottom_4.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_bottom_auto_4.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_bottom_manual_4.setChecked(True)
                self.ui.c_s_temp_bottom_device_4.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 4 temp : ' + str(e))
        finally:
            pass 
    

    ###############################
    # E area sensor 3 load setup 
    ###############################
    def e_area_sensor_3_load_setup(self):
        
        ########################
        # sensor 3 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='19' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_pr_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_top_manual_3.setChecked(True)
                self.ui.e_s_pr_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='19' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_pr_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_bottom_manual_3.setChecked(True)
                self.ui.e_s_pr_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 3 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='19' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_h2s_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_top_manual_3.setChecked(True)
                self.ui.e_s_h2s_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='19' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_h2s_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_bottom_manual_3.setChecked(True)
                self.ui.e_s_h2s_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 3 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='19' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_nh3_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_top_manual_3.setChecked(True)
                self.ui.e_s_nh3_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='19' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_nh3_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_bottom_manual_3.setChecked(True)
                self.ui.e_s_nh3_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 3 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='19' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_rh_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_top_manual_3.setChecked(True)
                self.ui.e_s_rh_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='19' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_rh_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_bottom_manual_3.setChecked(True)
                self.ui.e_s_rh_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 3 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 3 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='19' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_temp_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_top_manual_3.setChecked(True)
                self.ui.e_s_temp_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='19' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_temp_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_bottom_manual_3.setChecked(True)
                self.ui.e_s_temp_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 3 temp : ' + str(e))
        finally:
            pass

    ###############################
    # D area sensor 3 load setup 
    ###############################
    def d_area_sensor_3_load_setup(self):
        
        ########################
        # sensor 3 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='15' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_pr_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_top_manual_3.setChecked(True)
                self.ui.d_s_pr_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='15' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_pr_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_bottom_manual_3.setChecked(True)
                self.ui.d_s_pr_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 3 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='15' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_h2s_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_top_manual_3.setChecked(True)
                self.ui.d_s_h2s_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='15' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_h2s_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_bottom_manual_3.setChecked(True)
                self.ui.d_s_h2s_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 3 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='15' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_nh3_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_top_manual_3.setChecked(True)
                self.ui.d_s_nh3_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='15' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_nh3_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_bottom_manual_3.setChecked(True)
                self.ui.d_s_nh3_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 3 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='15' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_rh_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_top_manual_3.setChecked(True)
                self.ui.d_s_rh_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='15' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_rh_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_bottom_manual_3.setChecked(True)
                self.ui.d_s_rh_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 3 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 3 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='15' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_temp_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_top_manual_3.setChecked(True)
                self.ui.d_s_temp_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='15' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_temp_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_bottom_manual_3.setChecked(True)
                self.ui.d_s_temp_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 3 temp : ' + str(e))
        finally:
            pass

    
    ###############################
    # C area sensor 3 load setup 
    ###############################
    def c_area_sensor_3_load_setup(self):
        
        ########################
        # sensor 3 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='10' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_pr_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_top_manual_3.setChecked(True)
                self.ui.c_s_pr_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='10' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_pr_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_bottom_manual_3.setChecked(True)
                self.ui.c_s_pr_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 3 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='10' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_h2s_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_top_manual_3.setChecked(True)
                self.ui.c_s_h2s_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='10' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_h2s_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_bottom_manual_3.setChecked(True)
                self.ui.c_s_h2s_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 3 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='10' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_nh3_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_top_manual_3.setChecked(True)
                self.ui.c_s_nh3_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='10' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_nh3_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_bottom_manual_3.setChecked(True)
                self.ui.c_s_nh3_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 3 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='10' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_rh_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_top_manual_3.setChecked(True)
                self.ui.c_s_rh_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='10' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_rh_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_bottom_manual_3.setChecked(True)
                self.ui.c_s_rh_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 3 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='10' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_temp_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_top_manual_3.setChecked(True)
                self.ui.c_s_temp_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='10' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_temp_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_bottom_manual_3.setChecked(True)
                self.ui.c_s_temp_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 3 temp : ' + str(e))
        finally:
            pass  


    ###############################
    # B area sensor 3 load setup 
    ###############################
    def b_area_sensor_3_load_setup(self):
        
        ########################
        # sensor 3 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='7' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_pr_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_top_manual_3.setChecked(True)
                self.ui.b_s_pr_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='7' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_pr_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_bottom_manual_3.setChecked(True)
                self.ui.b_s_pr_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 3 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='7' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_h2s_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_top_manual_3.setChecked(True)
                self.ui.b_s_h2s_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='7' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_h2s_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_bottom_manual_3.setChecked(True)
                self.ui.b_s_h2s_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 3 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='7' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_nh3_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_top_manual_3.setChecked(True)
                self.ui.b_s_nh3_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='7' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_nh3_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_bottom_manual_3.setChecked(True)
                self.ui.b_s_nh3_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 3 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='7' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_rh_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_top_manual_3.setChecked(True)
                self.ui.b_s_rh_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='7' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_rh_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_bottom_manual_3.setChecked(True)
                self.ui.b_s_rh_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 3 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 3 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='7' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_temp_top_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_top_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_top_manual_3.setChecked(True)
                self.ui.b_s_temp_top_device_3.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='7' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_temp_bottom_3.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_bottom_auto_3.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_bottom_manual_3.setChecked(True)
                self.ui.b_s_temp_bottom_device_3.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 3 temp : ' + str(e))
        finally:
            pass

    ###############################
    # E area sensor 2 load setup 
    ###############################
    def e_area_sensor_2_load_setup(self):
        
        ########################
        # sensor 2 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='18' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_pr_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_top_manual_2.setChecked(True)
                self.ui.e_s_pr_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='18' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_pr_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_bottom_manual_2.setChecked(True)
                self.ui.e_s_pr_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 2 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='18' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_h2s_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_top_manual_2.setChecked(True)
                self.ui.e_s_h2s_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='18' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_h2s_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_bottom_manual_2.setChecked(True)
                self.ui.e_s_h2s_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 2 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='18' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_nh3_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_top_manual_2.setChecked(True)
                self.ui.e_s_nh3_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='18' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_nh3_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_bottom_manual_2.setChecked(True)
                self.ui.e_s_nh3_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='18' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_rh_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_top_manual_2.setChecked(True)
                self.ui.e_s_rh_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='18' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_rh_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_bottom_manual_2.setChecked(True)
                self.ui.e_s_rh_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 2 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='18' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_temp_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_top_manual_2.setChecked(True)
                self.ui.e_s_temp_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='18' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_temp_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_bottom_manual_2.setChecked(True)
                self.ui.e_s_temp_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 2 temp : ' + str(e))
        finally:
            pass

    ###############################
    # D area sensor 2 load setup 
    ###############################
    def d_area_sensor_2_load_setup(self):
        
        ########################
        # sensor 2 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='14' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_pr_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_top_manual_2.setChecked(True)
                self.ui.d_s_pr_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='14' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_pr_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_bottom_manual_2.setChecked(True)
                self.ui.d_s_pr_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 2 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='14' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_h2s_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_top_manual_2.setChecked(True)
                self.ui.d_s_h2s_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='14' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_h2s_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_bottom_manual_2.setChecked(True)
                self.ui.d_s_h2s_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 2 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='14' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_nh3_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_top_manual_2.setChecked(True)
                self.ui.d_s_nh3_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='14' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_nh3_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_bottom_manual_2.setChecked(True)
                self.ui.d_s_nh3_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='14' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_rh_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_top_manual_2.setChecked(True)
                self.ui.d_s_rh_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='14' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_rh_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_bottom_manual_2.setChecked(True)
                self.ui.d_s_rh_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 2 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='14' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_temp_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_top_manual_2.setChecked(True)
                self.ui.d_s_temp_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='14' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_temp_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_bottom_manual_2.setChecked(True)
                self.ui.d_s_temp_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 2 temp : ' + str(e))
        finally:
            pass

    ###############################
    # C area sensor 2 load setup 
    ###############################
    def c_area_sensor_2_load_setup(self):
        
        ########################
        # sensor 2 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='9' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_pr_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_top_manual_2.setChecked(True)
                self.ui.c_s_pr_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='9' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_pr_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_bottom_manual_2.setChecked(True)
                self.ui.c_s_pr_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 2 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='9' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_h2s_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_top_manual_2.setChecked(True)
                self.ui.c_s_h2s_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='9' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_h2s_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_bottom_manual_2.setChecked(True)
                self.ui.c_s_h2s_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 2 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='9' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_nh3_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_top_manual_2.setChecked(True)
                self.ui.c_s_nh3_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='9' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_nh3_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_bottom_manual_2.setChecked(True)
                self.ui.c_s_nh3_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='9' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_rh_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_top_manual_2.setChecked(True)
                self.ui.c_s_rh_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='9' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_rh_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_bottom_manual_2.setChecked(True)
                self.ui.c_s_rh_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 2 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='9' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_temp_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_top_manual_2.setChecked(True)
                self.ui.c_s_temp_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='9' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_temp_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_bottom_manual_2.setChecked(True)
                self.ui.c_s_temp_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 2 temp : ' + str(e))
        finally:
            pass   


    ###############################
    # B area sensor 2 load setup 
    ###############################
    def b_area_sensor_2_load_setup(self):
        
        ########################
        # sensor 2 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='6' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_pr_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_top_manual_2.setChecked(True)
                self.ui.b_s_pr_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='6' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_pr_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_bottom_manual_2.setChecked(True)
                self.ui.b_s_pr_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 2 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='6' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_h2s_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_top_manual_2.setChecked(True)
                self.ui.b_s_h2s_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='6' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_h2s_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_bottom_manual_2.setChecked(True)
                self.ui.b_s_h2s_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 2 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='6' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_nh3_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_top_manual_2.setChecked(True)
                self.ui.b_s_nh3_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='6' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_nh3_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_bottom_manual_2.setChecked(True)
                self.ui.b_s_nh3_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='6' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_rh_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_top_manual_2.setChecked(True)
                self.ui.b_s_rh_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='6' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_rh_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_bottom_manual_2.setChecked(True)
                self.ui.b_s_rh_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 2 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='6' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_temp_top_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_top_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_top_manual_2.setChecked(True)
                self.ui.b_s_temp_top_device_2.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='6' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_temp_bottom_2.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_bottom_auto_2.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_bottom_manual_2.setChecked(True)
                self.ui.b_s_temp_bottom_device_2.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 2 temp : ' + str(e))
        finally:
            pass   

    ###############################
    # E area sensor 1 load setup 
    ###############################
    def e_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='17' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_pr_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_top_manual_1.setChecked(True)
                self.ui.e_s_pr_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='17' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_pr_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_pr_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_pr_bottom_manual_1.setChecked(True)
                self.ui.e_s_pr_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 1 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='17' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_h2s_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_top_manual_1.setChecked(True)
                self.ui.e_s_h2s_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='17' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_h2s_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_h2s_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_h2s_bottom_manual_1.setChecked(True)
                self.ui.e_s_h2s_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='17' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_nh3_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_top_manual_1.setChecked(True)
                self.ui.e_s_nh3_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='17' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_nh3_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_nh3_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_nh3_bottom_manual_1.setChecked(True)
                self.ui.e_s_nh3_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='17' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_rh_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_top_manual_1.setChecked(True)
                self.ui.e_s_rh_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='17' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_rh_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_rh_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_rh_bottom_manual_1.setChecked(True)
                self.ui.e_s_rh_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='e' and s_id='17' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.e_s_temp_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_top_manual_1.setChecked(True)
                self.ui.e_s_temp_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='e' and s_id='17' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.e_s_temp_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.e_s_temp_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.e_s_temp_bottom_manual_1.setChecked(True)
                self.ui.e_s_temp_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > e area sensor 1 temp : ' + str(e))
        finally:
            pass   

    ###############################
    # D area sensor 1 load setup 
    ###############################
    def d_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='13' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_pr_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_top_manual_1.setChecked(True)
                self.ui.d_s_pr_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='13' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_pr_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_pr_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_pr_bottom_manual_1.setChecked(True)
                self.ui.d_s_pr_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 1 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='13' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_h2s_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_top_manual_1.setChecked(True)
                self.ui.d_s_h2s_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='13' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_h2s_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_h2s_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_h2s_bottom_manual_1.setChecked(True)
                self.ui.d_s_h2s_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='13' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_nh3_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_top_manual_1.setChecked(True)
                self.ui.d_s_nh3_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='13' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_nh3_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_nh3_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_nh3_bottom_manual_1.setChecked(True)
                self.ui.d_s_nh3_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='13' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_rh_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_top_manual_1.setChecked(True)
                self.ui.d_s_rh_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='13' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_rh_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_rh_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_rh_bottom_manual_1.setChecked(True)
                self.ui.d_s_rh_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='d' and s_id='13' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.d_s_temp_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_top_manual_1.setChecked(True)
                self.ui.d_s_temp_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='d' and s_id='13' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.d_s_temp_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.d_s_temp_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.d_s_temp_bottom_manual_1.setChecked(True)
                self.ui.d_s_temp_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > d area sensor 1 temp : ' + str(e))
        finally:
            pass   

    ###############################
    # C area sensor 1 load setup 
    ###############################
    def c_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='8' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_pr_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_top_manual_1.setChecked(True)
                self.ui.c_s_pr_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='8' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_pr_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_pr_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_pr_bottom_manual_1.setChecked(True)
                self.ui.c_s_pr_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 1 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='8' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_h2s_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_top_manual_1.setChecked(True)
                self.ui.c_s_h2s_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='8' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_h2s_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_h2s_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_h2s_bottom_manual_1.setChecked(True)
                self.ui.c_s_h2s_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='8' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_nh3_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_top_manual_1.setChecked(True)
                self.ui.c_s_nh3_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='8' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_nh3_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_nh3_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_nh3_bottom_manual_1.setChecked(True)
                self.ui.c_s_nh3_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='8' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_rh_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_top_manual_1.setChecked(True)
                self.ui.c_s_rh_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='8' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_rh_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_rh_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_rh_bottom_manual_1.setChecked(True)
                self.ui.c_s_rh_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='c' and s_id='8' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.c_s_temp_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_top_manual_1.setChecked(True)
                self.ui.c_s_temp_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='c' and s_id='8' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.c_s_temp_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.c_s_temp_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.c_s_temp_bottom_manual_1.setChecked(True)
                self.ui.c_s_temp_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > c area sensor 1 temp : ' + str(e))
        finally:
            pass   

    ###############################
    # B area sensor 1 load setup 
    ###############################
    def b_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='5' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_pr_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_top_manual_1.setChecked(True)
                self.ui.b_s_pr_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='5' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_pr_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_pr_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_pr_bottom_manual_1.setChecked(True)
                self.ui.b_s_pr_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 1 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='5' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_h2s_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_top_manual_1.setChecked(True)
                self.ui.b_s_h2s_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='5' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_h2s_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_h2s_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_h2s_bottom_manual_1.setChecked(True)
                self.ui.b_s_h2s_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='5' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_nh3_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_top_manual_1.setChecked(True)
                self.ui.b_s_nh3_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='5' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_nh3_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_nh3_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_nh3_bottom_manual_1.setChecked(True)
                self.ui.b_s_nh3_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='5' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_rh_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_top_manual_1.setChecked(True)
                self.ui.b_s_rh_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='5' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_rh_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_rh_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_rh_bottom_manual_1.setChecked(True)
                self.ui.b_s_rh_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='b' and s_id='5' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.b_s_temp_top_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_top_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_top_manual_1.setChecked(True)
                self.ui.b_s_temp_top_device_1.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='b' and s_id='5' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.b_s_temp_bottom_1.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.b_s_temp_bottom_auto_1.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.b_s_temp_bottom_manual_1.setChecked(True)
                self.ui.b_s_temp_bottom_device_1.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > b area sensor 1 temp : ' + str(e))
        finally:
            pass   


    ###############################
    # A area sensor 1 load setup 
    ###############################
    def a_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_pr_top.setText(str(val[0]))
                if val[1] == 'enable':
                    self.ui.a_s_1_pr_top_auto.setChecked(True)
                elif val[2] == 'enable':
                    self.ui.a_s_1_pr_top_manual.setChecked(True)
                self.ui.a_s_1_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_pr_bottom.setText(str(val[0]))
                if val[1] == 'enable':
                    self.ui.a_s_1_pr_bottom_auto.setChecked(True)
                elif val[2] == 'enable':
                    self.ui.a_s_1_pr_bottom_manual.setChecked(True)
                self.ui.a_s_1_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_top_manual.setChecked(True)
                self.ui.a_s_1_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_1_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_top_manual.setChecked(True)
                self.ui.a_s_1_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_1_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_top_manual.setChecked(True)
                self.ui.a_s_1_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_bottom_manual.setChecked(True)
                self.ui.a_s_1_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()

            ### top temp value
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                
                self.ui.a_s_1_temp_top.setText(str(val[0]))
                if len(val[1]) > 0:
                    self.ui.a_s_1_temp_top_auto.setChecked(True)
                elif len(val[2]) > 0:
                    self.ui.a_s_1_temp_top_manual.setChecked(True)
                self.ui.a_s_1_temp_top_device.setText(str(val[3]))

            ### bottom temp value
            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                
                self.ui.a_s_1_temp_bottom.setText(str(val[0]))
                if len(val[1]) > 0:
                    self.ui.a_s_1_temp_bottom_auto.setChecked(True)
                elif len(val[2]) > 0:
                    self.ui.a_s_1_temp_bottom_manual.setChecked(True)
                self.ui.a_s_1_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 temp : ' + str(e))
        finally:
            pass   

    ###############################
    # A area sensor 4 load setup 
    ###############################
    def a_area_sensor_4_load_setup(self):
        
        ########################
        # sensor 4 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='4' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_4_pr_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_pr_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_pr_top_manual.setChecked(True)
                self.ui.a_s_4_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='4' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_4_pr_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_pr_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_pr_bottom_manual.setChecked(True)
                self.ui.a_s_4_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 4 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='4' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_4_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_h2s_top_manual.setChecked(True)
                self.ui.a_s_4_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='4' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_4_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_4_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 4 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='4' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_4_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_nh3_top_manual.setChecked(True)
                self.ui.a_s_4_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='4' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_4_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_4_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 4 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 4 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='4' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_4_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_rh_top_manual.setChecked(True)
                self.ui.a_s_4_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='4' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_4_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_rh_bottom_manual.setChecked(True)
                self.ui.a_s_4_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 4 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 4 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='4' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_4_temp_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_temp_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_temp_top_manual.setChecked(True)
                self.ui.a_s_4_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='4' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_4_temp_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_4_temp_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_4_temp_bottom_manual.setChecked(True)
                self.ui.a_s_4_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 4 temp : ' + str(e))
        finally:
            pass    

    ###############################
    # A area sensor 3 load setup 
    ###############################
    def a_area_sensor_3_load_setup(self):
        
        ########################
        # sensor 3 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='3' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_3_pr_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_pr_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_pr_top_manual.setChecked(True)
                self.ui.a_s_3_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='3' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_3_pr_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_pr_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_pr_bottom_manual.setChecked(True)
                self.ui.a_s_3_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 3 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='3' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_3_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_h2s_top_manual.setChecked(True)
                self.ui.a_s_3_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='3' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_3_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_3_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 3 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 3 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='3' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_3_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_nh3_top_manual.setChecked(True)
                self.ui.a_s_3_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='3' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_3_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_3_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_3_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_rh_top_manual.setChecked(True)
                self.ui.a_s_3_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_3_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_rh_bottom_manual.setChecked(True)
                self.ui.a_s_3_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 3 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 3 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='3' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_3_temp_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_temp_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_temp_top_manual.setChecked(True)
                self.ui.a_s_3_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='3' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_3_temp_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_3_temp_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_3_temp_bottom_manual.setChecked(True)
                self.ui.a_s_3_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 3 temp : ' + str(e))
        finally:
            pass    


    ###############################
    # A area sensor 2 load setup 
    ###############################
    def a_area_sensor_2_load_setup(self):
        
        ########################
        # sensor 2 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_2_pr_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_pr_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_pr_top_manual.setChecked(True)
                self.ui.a_s_2_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_2_pr_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_pr_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_pr_bottom_manual.setChecked(True)
                self.ui.a_s_2_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 pr : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_2_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_h2s_top_manual.setChecked(True)
                self.ui.a_s_2_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_2_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_2_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_2_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_nh3_top_manual.setChecked(True)
                self.ui.a_s_2_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_2_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_2_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 2 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_2_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_rh_top_manual.setChecked(True)
                self.ui.a_s_2_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_2_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_rh_bottom_manual.setChecked(True)
                self.ui.a_s_2_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 2 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='2' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_2_temp_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_temp_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_temp_top_manual.setChecked(True)
                self.ui.a_s_2_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='2' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_2_temp_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_2_temp_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_2_temp_bottom_manual.setChecked(True)
                self.ui.a_s_2_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 2 temp : ' + str(e))
        finally:
            pass    


    ###############################
    # A area sensor 1 load setup 
    ###############################
    def a_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_pr_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_pr_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_pr_top_manual.setChecked(True)
                self.ui.a_s_1_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_pr_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_pr_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_pr_bottom_manual.setChecked(True)
                self.ui.a_s_1_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_top_manual.setChecked(True)
                self.ui.a_s_1_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_1_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_top_manual.setChecked(True)
                self.ui.a_s_1_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_1_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_top_manual.setChecked(True)
                self.ui.a_s_1_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_bottom_manual.setChecked(True)
                self.ui.a_s_1_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_temp_top.setText(str(val[0]))
                if val[1] == 'enable':
                    self.ui.a_s_1_temp_top_auto.setChecked(True)
                elif val[2] == 'enable':
                    self.ui.a_s_1_temp_top_manual.setChecked(True)
                self.ui.a_s_1_temp_top_device.setText(str(val[3]))

            #QMessageBox.information(self , 'Msg' , str(val[1] + ' / ' + val[2]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_temp_bottom.setText(str(val[0]))
                if val[1] == 'enable':
                    self.ui.a_s_1_temp_bottom_auto.setChecked(True)
                elif val[2] == 'enable':
                    self.ui.a_s_1_temp_bottom_manual.setChecked(True)
                self.ui.a_s_1_temp_bottom_device.setText(str(val[3]))
            
            #QMessageBox.information(self , 'Msg' , str(val[1] + ' / ' + val[2]))

            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 temp : ' + str(e))
        finally:
            pass    


    ###############################
    # A area sensor 1 load setup 
    ###############################
    def a_area_sensor_1_load_setup(self):
        
        ########################
        # sensor 1 pr value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_pr_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_pr_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_pr_top_manual.setChecked(True)
                self.ui.a_s_1_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_pr_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_pr_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_pr_bottom_manual.setChecked(True)
                self.ui.a_s_1_pr_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 h2s value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_h2s_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_top_manual.setChecked(True)
                self.ui.a_s_1_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_h2s_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_h2s_bottom_manual.setChecked(True)
                self.ui.a_s_1_h2s_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 h2s : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 nh3 value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_nh3_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_top_manual.setChecked(True)
                self.ui.a_s_1_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_nh3_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_nh3_bottom_manual.setChecked(True)
                self.ui.a_s_1_nh3_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 nh3 : ' + str(e))
        finally:
            pass

        ########################
        # sensor 1 rh value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_rh_top.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_top_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_top_manual.setChecked(True)
                self.ui.a_s_1_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_rh_bottom.setText(str(val[0]))
                if str(val[1])  == 'enable':
                    self.ui.a_s_1_rh_bottom_auto.setChecked(True)
                elif str(val[2])  == 'enable':
                    self.ui.a_s_1_rh_bottom_manual.setChecked(True)
                self.ui.a_s_1_rh_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 rh : ' + str(e))
        finally:
            pass 

        ########################
        # sensor 1 temp value
        ########################
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select s_alarm_top , s_top_auto_run , s_top_manual_run , s_alarm_top_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 0,1"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                ### top value
                self.ui.a_s_1_temp_top.setText(str(val[0]))
                if str(val[1]) == 'enable':
                    self.ui.a_s_1_temp_top_auto.setChecked(True)
                elif str(val[2]) == 'enable':
                    self.ui.a_s_1_temp_top_manual.setChecked(True)
                self.ui.a_s_1_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_temp_bottom.setText(str(val[0]))
                if str(val[1]) == 'enable':
                    self.ui.a_s_1_temp_bottom_auto.setChecked(True)
                elif str(val[2]) == 'enable':
                    self.ui.a_s_1_temp_bottom_manual.setChecked(True)
                self.ui.a_s_1_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 temp : ' + str(e))
        finally:
            pass    
    
    #######################################
    # C area setup sensor 5 button group
    #######################################
    def c_area_setup_sensor_5_btn_group(self):
        
            ### c area sensor 5 temp , rh , nh3 , h2s , pr now value
            self.c_area_sensor_now_value_s_5()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.c_s_r_time_5.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 5 button group temp 
            self.c_s_temp_top_5_g = QButtonGroup()
            self.c_s_temp_top_5_g.addButton(self.ui.c_s_temp_top_manual_5)
            self.c_s_temp_top_5_g.addButton(self.ui.c_s_temp_top_auto_5)
            
            self.c_s_temp_bottom_5_g = QButtonGroup()
            self.c_s_temp_bottom_5_g.addButton(self.ui.c_s_temp_bottom_manual_5)
            self.c_s_temp_bottom_5_g.addButton(self.ui.c_s_temp_bottom_auto_5)

            ### sensor 5 button group rh 
            self.c_s_rh_top_5_g = QButtonGroup()
            self.c_s_rh_top_5_g.addButton(self.ui.c_s_rh_top_manual_5)
            self.c_s_rh_top_5_g.addButton(self.ui.c_s_rh_top_auto_5)
            
            self.c_s_rh_bottom_5_g = QButtonGroup()
            self.c_s_rh_bottom_5_g.addButton(self.ui.c_s_rh_bottom_manual_5)
            self.c_s_rh_bottom_5_g.addButton(self.ui.c_s_rh_bottom_auto_5)
            
            ### sensor 5 button group nh3 
            self.c_s_nh3_top_5_g = QButtonGroup()
            self.c_s_nh3_top_5_g.addButton(self.ui.c_s_nh3_top_manual_5)
            self.c_s_nh3_top_5_g.addButton(self.ui.c_s_nh3_top_auto_5)
            
            self.c_s_nh3_bottom_5_g = QButtonGroup()
            self.c_s_nh3_bottom_5_g.addButton(self.ui.c_s_nh3_bottom_manual_5)
            self.c_s_nh3_bottom_5_g.addButton(self.ui.c_s_nh3_bottom_auto_5)

            ### sensor 5 button group h2s 
            self.c_s_h2s_top_5_g = QButtonGroup()
            self.c_s_h2s_top_5_g.addButton(self.ui.c_s_h2s_top_manual_5)
            self.c_s_h2s_top_5_g.addButton(self.ui.c_s_h2s_top_auto_5)
            
            self.c_s_h2s_bottom_5_g = QButtonGroup()
            self.c_s_h2s_bottom_5_g.addButton(self.ui.c_s_h2s_bottom_manual_5)
            self.c_s_h2s_bottom_5_g.addButton(self.ui.c_s_h2s_bottom_auto_5)

            ### sensor 5 button group pr 
            self.c_s_pr_top_5_g = QButtonGroup()
            self.c_s_pr_top_5_g.addButton(self.ui.c_s_pr_top_manual_5)
            self.c_s_pr_top_5_g.addButton(self.ui.c_s_pr_top_auto_5)
            
            self.c_s_pr_bottom_5_g = QButtonGroup()
            self.c_s_pr_bottom_5_g.addButton(self.ui.c_s_pr_bottom_manual_5)
            self.c_s_pr_bottom_5_g.addButton(self.ui.c_s_pr_bottom_auto_5)
    
    #######################################
    # D area setup sensor 4 button group
    #######################################
    def d_area_setup_sensor_4_btn_group(self):
        
            ### d area sensor 4 temp , rh , nh3 , h2s , pr now value
            self.d_area_sensor_now_value_s_4()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.d_s_r_time_4.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 4 button group temp 
            self.d_s_temp_top_4_g = QButtonGroup()
            self.d_s_temp_top_4_g.addButton(self.ui.d_s_temp_top_manual_4)
            self.d_s_temp_top_4_g.addButton(self.ui.d_s_temp_top_auto_4)
            
            self.d_s_temp_bottom_4_g = QButtonGroup()
            self.d_s_temp_bottom_4_g.addButton(self.ui.d_s_temp_bottom_manual_4)
            self.d_s_temp_bottom_4_g.addButton(self.ui.d_s_temp_bottom_auto_4)

            ### sensor 4 button group rh 
            self.d_s_rh_top_4_g = QButtonGroup()
            self.d_s_rh_top_4_g.addButton(self.ui.d_s_rh_top_manual_4)
            self.d_s_rh_top_4_g.addButton(self.ui.d_s_rh_top_auto_4)
            
            self.d_s_rh_bottom_4_g = QButtonGroup()
            self.d_s_rh_bottom_4_g.addButton(self.ui.d_s_rh_bottom_manual_4)
            self.d_s_rh_bottom_4_g.addButton(self.ui.d_s_rh_bottom_auto_4)
            
            ### sensor 4 button group nh3 
            self.d_s_nh3_top_4_g = QButtonGroup()
            self.d_s_nh3_top_4_g.addButton(self.ui.d_s_nh3_top_manual_4)
            self.d_s_nh3_top_4_g.addButton(self.ui.d_s_nh3_top_auto_4)
            
            self.d_s_nh3_bottom_4_g = QButtonGroup()
            self.d_s_nh3_bottom_4_g.addButton(self.ui.d_s_nh3_bottom_manual_4)
            self.d_s_nh3_bottom_4_g.addButton(self.ui.d_s_nh3_bottom_auto_4)

            ### sensor 4 button group h2s 
            self.d_s_h2s_top_4_g = QButtonGroup()
            self.d_s_h2s_top_4_g.addButton(self.ui.d_s_h2s_top_manual_4)
            self.d_s_h2s_top_4_g.addButton(self.ui.d_s_h2s_top_auto_4)
            
            self.d_s_h2s_bottom_4_g = QButtonGroup()
            self.d_s_h2s_bottom_4_g.addButton(self.ui.d_s_h2s_bottom_manual_4)
            self.d_s_h2s_bottom_4_g.addButton(self.ui.d_s_h2s_bottom_auto_4)

            ### sensor 4 button group pr 
            self.d_s_pr_top_4_g = QButtonGroup()
            self.d_s_pr_top_4_g.addButton(self.ui.d_s_pr_top_manual_4)
            self.d_s_pr_top_4_g.addButton(self.ui.d_s_pr_top_auto_4)
            
            self.d_s_pr_bottom_4_g = QButtonGroup()
            self.d_s_pr_bottom_4_g.addButton(self.ui.d_s_pr_bottom_manual_4)
            self.d_s_pr_bottom_4_g.addButton(self.ui.d_s_pr_bottom_auto_4)

    #######################################
    # C area setup sensor 4 button group
    #######################################
    def c_area_setup_sensor_4_btn_group(self):
        
            ### c area sensor 4 temp , rh , nh3 , h2s , pr now value
            self.c_area_sensor_now_value_s_4()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.c_s_r_time_4.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 4 button group temp 
            self.c_s_temp_top_4_g = QButtonGroup()
            self.c_s_temp_top_4_g.addButton(self.ui.c_s_temp_top_manual_4)
            self.c_s_temp_top_4_g.addButton(self.ui.c_s_temp_top_auto_4)
            
            self.c_s_temp_bottom_4_g = QButtonGroup()
            self.c_s_temp_bottom_4_g.addButton(self.ui.c_s_temp_bottom_manual_4)
            self.c_s_temp_bottom_4_g.addButton(self.ui.c_s_temp_bottom_auto_4)

            ### sensor 4 button group rh 
            self.c_s_rh_top_4_g = QButtonGroup()
            self.c_s_rh_top_4_g.addButton(self.ui.c_s_rh_top_manual_4)
            self.c_s_rh_top_4_g.addButton(self.ui.c_s_rh_top_auto_4)
            
            self.c_s_rh_bottom_4_g = QButtonGroup()
            self.c_s_rh_bottom_4_g.addButton(self.ui.c_s_rh_bottom_manual_4)
            self.c_s_rh_bottom_4_g.addButton(self.ui.c_s_rh_bottom_auto_4)
            
            ### sensor 4 button group nh3 
            self.c_s_nh3_top_4_g = QButtonGroup()
            self.c_s_nh3_top_4_g.addButton(self.ui.c_s_nh3_top_manual_4)
            self.c_s_nh3_top_4_g.addButton(self.ui.c_s_nh3_top_auto_4)
            
            self.c_s_nh3_bottom_4_g = QButtonGroup()
            self.c_s_nh3_bottom_4_g.addButton(self.ui.c_s_nh3_bottom_manual_4)
            self.c_s_nh3_bottom_4_g.addButton(self.ui.c_s_nh3_bottom_auto_4)

            ### sensor 4 button group h2s 
            self.c_s_h2s_top_4_g = QButtonGroup()
            self.c_s_h2s_top_4_g.addButton(self.ui.c_s_h2s_top_manual_4)
            self.c_s_h2s_top_4_g.addButton(self.ui.c_s_h2s_top_auto_4)
            
            self.c_s_h2s_bottom_4_g = QButtonGroup()
            self.c_s_h2s_bottom_4_g.addButton(self.ui.c_s_h2s_bottom_manual_4)
            self.c_s_h2s_bottom_4_g.addButton(self.ui.c_s_h2s_bottom_auto_4)

            ### sensor 4 button group pr 
            self.c_s_pr_top_4_g = QButtonGroup()
            self.c_s_pr_top_4_g.addButton(self.ui.c_s_pr_top_manual_4)
            self.c_s_pr_top_4_g.addButton(self.ui.c_s_pr_top_auto_4)
            
            self.c_s_pr_bottom_4_g = QButtonGroup()
            self.c_s_pr_bottom_4_g.addButton(self.ui.c_s_pr_bottom_manual_4)
            self.c_s_pr_bottom_4_g.addButton(self.ui.c_s_pr_bottom_auto_4)

    #######################################
    # A area setup sensor 4 button group
    #######################################
    def a_area_setup_sensor_4_btn_group(self):
        
            ### a area sensor 4 temp , rh , nh3 , h2s , pr now value
            self.area_sensor_now_value_s_4()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.a_s_4_r_time.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 4 button group temp 
            self.a_s_4_temp_top_g = QButtonGroup()
            self.a_s_4_temp_top_g.addButton(self.ui.a_s_4_temp_top_manual)
            self.a_s_4_temp_top_g.addButton(self.ui.a_s_4_temp_top_auto)
            
            self.a_s_4_temp_bottom_g = QButtonGroup()
            self.a_s_4_temp_bottom_g.addButton(self.ui.a_s_4_temp_bottom_manual)
            self.a_s_4_temp_bottom_g.addButton(self.ui.a_s_4_temp_bottom_auto)

            ### sensor 4 button group rh 
            self.a_s_4_rh_top_g = QButtonGroup()
            self.a_s_4_rh_top_g.addButton(self.ui.a_s_4_rh_top_manual)
            self.a_s_4_rh_top_g.addButton(self.ui.a_s_4_rh_top_auto)
            
            self.a_s_4_rh_bottom_g = QButtonGroup()
            self.a_s_4_rh_bottom_g.addButton(self.ui.a_s_4_rh_bottom_manual)
            self.a_s_4_rh_bottom_g.addButton(self.ui.a_s_4_rh_bottom_auto)
            
            ### sensor 4 button group nh3 
            self.a_s_4_nh3_top_g = QButtonGroup()
            self.a_s_4_nh3_top_g.addButton(self.ui.a_s_4_nh3_top_manual)
            self.a_s_4_nh3_top_g.addButton(self.ui.a_s_4_nh3_top_auto)
            
            self.a_s_4_nh3_bottom_g = QButtonGroup()
            self.a_s_4_nh3_bottom_g.addButton(self.ui.a_s_4_nh3_bottom_manual)
            self.a_s_4_nh3_bottom_g.addButton(self.ui.a_s_4_nh3_bottom_auto)

            ### sensor 4 button group h2s 
            self.a_s_4_h2s_top_g = QButtonGroup()
            self.a_s_4_h2s_top_g.addButton(self.ui.a_s_4_h2s_top_manual)
            self.a_s_4_h2s_top_g.addButton(self.ui.a_s_4_h2s_top_auto)
            
            self.a_s_4_h2s_bottom_g = QButtonGroup()
            self.a_s_4_h2s_bottom_g.addButton(self.ui.a_s_4_h2s_bottom_manual)
            self.a_s_4_h2s_bottom_g.addButton(self.ui.a_s_4_h2s_bottom_auto)

            ### sensor 4 button group pr 
            self.a_s_4_pr_top_g = QButtonGroup()
            self.a_s_4_pr_top_g.addButton(self.ui.a_s_4_pr_top_manual)
            self.a_s_4_pr_top_g.addButton(self.ui.a_s_4_pr_top_auto)
            
            self.a_s_4_pr_bottom_g = QButtonGroup()
            self.a_s_4_pr_bottom_g.addButton(self.ui.a_s_4_pr_bottom_manual)
            self.a_s_4_pr_bottom_g.addButton(self.ui.a_s_4_pr_bottom_auto)
    
    #######################################
    # E area setup sensor 3 button group
    #######################################
    def e_area_setup_sensor_3_btn_group(self):
        
            ### e area sensor 3 temp , rh , nh3 , h2s , pr now value
            self.e_area_sensor_now_value_s_3()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.e_s_r_time_3.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 3 button group temp 
            self.e_s_temp_top_3_g = QButtonGroup()
            self.e_s_temp_top_3_g.addButton(self.ui.e_s_temp_top_manual_3)
            self.e_s_temp_top_3_g.addButton(self.ui.e_s_temp_top_auto_3)
            
            self.e_s_temp_bottom_3_g = QButtonGroup()
            self.e_s_temp_bottom_3_g.addButton(self.ui.e_s_temp_bottom_manual_3)
            self.e_s_temp_bottom_3_g.addButton(self.ui.e_s_temp_bottom_auto_3)

            ### sensor 3 button group rh 
            self.e_s_rh_top_3_g = QButtonGroup()
            self.e_s_rh_top_3_g.addButton(self.ui.e_s_rh_top_manual_3)
            self.e_s_rh_top_3_g.addButton(self.ui.e_s_rh_top_auto_3)
            
            self.e_s_rh_bottom_3_g = QButtonGroup()
            self.e_s_rh_bottom_3_g.addButton(self.ui.e_s_rh_bottom_manual_3)
            self.e_s_rh_bottom_3_g.addButton(self.ui.e_s_rh_bottom_auto_3)
            
            ### sensor 3 button group nh3 
            self.e_s_nh3_top_3_g = QButtonGroup()
            self.e_s_nh3_top_3_g.addButton(self.ui.e_s_nh3_top_manual_3)
            self.e_s_nh3_top_3_g.addButton(self.ui.e_s_nh3_top_auto_3)
            
            self.e_s_nh3_bottom_3_g = QButtonGroup()
            self.e_s_nh3_bottom_3_g.addButton(self.ui.e_s_nh3_bottom_manual_3)
            self.e_s_nh3_bottom_3_g.addButton(self.ui.e_s_nh3_bottom_auto_3)

            ### sensor 3 button group h2s 
            self.e_s_h2s_top_3_g = QButtonGroup()
            self.e_s_h2s_top_3_g.addButton(self.ui.e_s_h2s_top_manual_3)
            self.e_s_h2s_top_3_g.addButton(self.ui.e_s_h2s_top_auto_3)
            
            self.e_s_h2s_bottom_3_g = QButtonGroup()
            self.e_s_h2s_bottom_3_g.addButton(self.ui.e_s_h2s_bottom_manual_3)
            self.e_s_h2s_bottom_3_g.addButton(self.ui.e_s_h2s_bottom_auto_3)

            ### sensor 3 button group pr 
            self.e_s_pr_top_3_g = QButtonGroup()
            self.e_s_pr_top_3_g.addButton(self.ui.e_s_pr_top_manual_3)
            self.e_s_pr_top_3_g.addButton(self.ui.e_s_pr_top_auto_3)
            
            self.e_s_pr_bottom_3_g = QButtonGroup()
            self.e_s_pr_bottom_3_g.addButton(self.ui.e_s_pr_bottom_manual_3)
            self.e_s_pr_bottom_3_g.addButton(self.ui.e_s_pr_bottom_auto_3)

    #######################################
    # D area setup sensor 3 button group
    #######################################
    def d_area_setup_sensor_3_btn_group(self):
        
            ### d area sensor 3 temp , rh , nh3 , h2s , pr now value
            self.d_area_sensor_now_value_s_3()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.d_s_r_time_3.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 3 button group temp 
            self.d_s_temp_top_3_g = QButtonGroup()
            self.d_s_temp_top_3_g.addButton(self.ui.d_s_temp_top_manual_3)
            self.d_s_temp_top_3_g.addButton(self.ui.d_s_temp_top_auto_3)
            
            self.d_s_temp_bottom_3_g = QButtonGroup()
            self.d_s_temp_bottom_3_g.addButton(self.ui.d_s_temp_bottom_manual_3)
            self.d_s_temp_bottom_3_g.addButton(self.ui.d_s_temp_bottom_auto_3)

            ### sensor 3 button group rh 
            self.d_s_rh_top_3_g = QButtonGroup()
            self.d_s_rh_top_3_g.addButton(self.ui.d_s_rh_top_manual_3)
            self.d_s_rh_top_3_g.addButton(self.ui.d_s_rh_top_auto_3)
            
            self.d_s_rh_bottom_3_g = QButtonGroup()
            self.d_s_rh_bottom_3_g.addButton(self.ui.d_s_rh_bottom_manual_3)
            self.d_s_rh_bottom_3_g.addButton(self.ui.d_s_rh_bottom_auto_3)
            
            ### sensor 3 button group nh3 
            self.d_s_nh3_top_3_g = QButtonGroup()
            self.d_s_nh3_top_3_g.addButton(self.ui.d_s_nh3_top_manual_3)
            self.d_s_nh3_top_3_g.addButton(self.ui.d_s_nh3_top_auto_3)
            
            self.d_s_nh3_bottom_3_g = QButtonGroup()
            self.d_s_nh3_bottom_3_g.addButton(self.ui.d_s_nh3_bottom_manual_3)
            self.d_s_nh3_bottom_3_g.addButton(self.ui.d_s_nh3_bottom_auto_3)

            ### sensor 3 button group h2s 
            self.d_s_h2s_top_3_g = QButtonGroup()
            self.d_s_h2s_top_3_g.addButton(self.ui.d_s_h2s_top_manual_3)
            self.d_s_h2s_top_3_g.addButton(self.ui.d_s_h2s_top_auto_3)
            
            self.d_s_h2s_bottom_3_g = QButtonGroup()
            self.d_s_h2s_bottom_3_g.addButton(self.ui.d_s_h2s_bottom_manual_3)
            self.d_s_h2s_bottom_3_g.addButton(self.ui.d_s_h2s_bottom_auto_3)

            ### sensor 3 button group pr 
            self.d_s_pr_top_3_g = QButtonGroup()
            self.d_s_pr_top_3_g.addButton(self.ui.d_s_pr_top_manual_3)
            self.d_s_pr_top_3_g.addButton(self.ui.d_s_pr_top_auto_3)
            
            self.d_s_pr_bottom_3_g = QButtonGroup()
            self.d_s_pr_bottom_3_g.addButton(self.ui.d_s_pr_bottom_manual_3)
            self.d_s_pr_bottom_3_g.addButton(self.ui.d_s_pr_bottom_auto_3)

    #######################################
    # C area setup sensor 3 button group
    #######################################
    def c_area_setup_sensor_3_btn_group(self):
        
            ### c area sensor 3 temp , rh , nh3 , h2s , pr now value
            self.c_area_sensor_now_value_s_3()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.c_s_r_time_3.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 3 button group temp 
            self.c_s_temp_top_3_g = QButtonGroup()
            self.c_s_temp_top_3_g.addButton(self.ui.c_s_temp_top_manual_3)
            self.c_s_temp_top_3_g.addButton(self.ui.c_s_temp_top_auto_3)
            
            self.c_s_temp_bottom_3_g = QButtonGroup()
            self.c_s_temp_bottom_3_g.addButton(self.ui.c_s_temp_bottom_manual_3)
            self.c_s_temp_bottom_3_g.addButton(self.ui.c_s_temp_bottom_auto_3)

            ### sensor 3 button group rh 
            self.c_s_rh_top_3_g = QButtonGroup()
            self.c_s_rh_top_3_g.addButton(self.ui.c_s_rh_top_manual_3)
            self.c_s_rh_top_3_g.addButton(self.ui.c_s_rh_top_auto_3)
            
            self.c_s_rh_bottom_3_g = QButtonGroup()
            self.c_s_rh_bottom_3_g.addButton(self.ui.c_s_rh_bottom_manual_3)
            self.c_s_rh_bottom_3_g.addButton(self.ui.c_s_rh_bottom_auto_3)
            
            ### sensor 3 button group nh3 
            self.c_s_nh3_top_3_g = QButtonGroup()
            self.c_s_nh3_top_3_g.addButton(self.ui.c_s_nh3_top_manual_3)
            self.c_s_nh3_top_3_g.addButton(self.ui.c_s_nh3_top_auto_3)
            
            self.c_s_nh3_bottom_3_g = QButtonGroup()
            self.c_s_nh3_bottom_3_g.addButton(self.ui.c_s_nh3_bottom_manual_3)
            self.c_s_nh3_bottom_3_g.addButton(self.ui.c_s_nh3_bottom_auto_3)

            ### sensor 3 button group h2s 
            self.c_s_h2s_top_3_g = QButtonGroup()
            self.c_s_h2s_top_3_g.addButton(self.ui.c_s_h2s_top_manual_3)
            self.c_s_h2s_top_3_g.addButton(self.ui.c_s_h2s_top_auto_3)
            
            self.c_s_h2s_bottom_3_g = QButtonGroup()
            self.c_s_h2s_bottom_3_g.addButton(self.ui.c_s_h2s_bottom_manual_3)
            self.c_s_h2s_bottom_3_g.addButton(self.ui.c_s_h2s_bottom_auto_3)

            ### sensor 3 button group pr 
            self.c_s_pr_top_3_g = QButtonGroup()
            self.c_s_pr_top_3_g.addButton(self.ui.c_s_pr_top_manual_3)
            self.c_s_pr_top_3_g.addButton(self.ui.c_s_pr_top_auto_3)
            
            self.c_s_pr_bottom_3_g = QButtonGroup()
            self.c_s_pr_bottom_3_g.addButton(self.ui.c_s_pr_bottom_manual_3)
            self.c_s_pr_bottom_3_g.addButton(self.ui.c_s_pr_bottom_auto_3)

    
    #######################################
    # B area setup sensor 3 button group
    #######################################
    def b_area_setup_sensor_3_btn_group(self):
        
            ### b area sensor 3 temp , rh , nh3 , h2s , pr now value
            self.b_area_sensor_now_value_s_3()
            
            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.b_s_r_time_3.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 3 button group temp 
            self.b_s_temp_top_3_g = QButtonGroup()
            self.b_s_temp_top_3_g.addButton(self.ui.b_s_temp_top_manual_3)
            self.b_s_temp_top_3_g.addButton(self.ui.b_s_temp_top_auto_3)
            
            self.b_s_temp_bottom_3_g = QButtonGroup()
            self.b_s_temp_bottom_3_g.addButton(self.ui.b_s_temp_bottom_manual_3)
            self.b_s_temp_bottom_3_g.addButton(self.ui.b_s_temp_bottom_auto_3)

            ### sensor 3 button group rh 
            self.b_s_rh_top_3_g = QButtonGroup()
            self.b_s_rh_top_3_g.addButton(self.ui.b_s_rh_top_manual_3)
            self.b_s_rh_top_3_g.addButton(self.ui.b_s_rh_top_auto_3)
            
            self.b_s_rh_bottom_3_g = QButtonGroup()
            self.b_s_rh_bottom_3_g.addButton(self.ui.b_s_rh_bottom_manual_3)
            self.b_s_rh_bottom_3_g.addButton(self.ui.b_s_rh_bottom_auto_3)
            
            ### sensor 3 button group nh3 
            self.b_s_nh3_top_3_g = QButtonGroup()
            self.b_s_nh3_top_3_g.addButton(self.ui.b_s_nh3_top_manual_3)
            self.b_s_nh3_top_3_g.addButton(self.ui.b_s_nh3_top_auto_3)
            
            self.b_s_nh3_bottom_3_g = QButtonGroup()
            self.b_s_nh3_bottom_3_g.addButton(self.ui.b_s_nh3_bottom_manual_3)
            self.b_s_nh3_bottom_3_g.addButton(self.ui.b_s_nh3_bottom_auto_3)

            ### sensor 3 button group h2s 
            self.b_s_h2s_top_3_g = QButtonGroup()
            self.b_s_h2s_top_3_g.addButton(self.ui.b_s_h2s_top_manual_3)
            self.b_s_h2s_top_3_g.addButton(self.ui.b_s_h2s_top_auto_3)
            
            self.b_s_h2s_bottom_3_g = QButtonGroup()
            self.b_s_h2s_bottom_3_g.addButton(self.ui.b_s_h2s_bottom_manual_3)
            self.b_s_h2s_bottom_3_g.addButton(self.ui.b_s_h2s_bottom_auto_3)

            ### sensor 3 button group pr 
            self.b_s_pr_top_3_g = QButtonGroup()
            self.b_s_pr_top_3_g.addButton(self.ui.b_s_pr_top_manual_3)
            self.b_s_pr_top_3_g.addButton(self.ui.b_s_pr_top_auto_3)
            
            self.b_s_pr_bottom_3_g = QButtonGroup()
            self.b_s_pr_bottom_3_g.addButton(self.ui.b_s_pr_bottom_manual_3)
            self.b_s_pr_bottom_3_g.addButton(self.ui.b_s_pr_bottom_auto_3)
    
    #######################################
    # A area setup sensor 3 button group
    #######################################
    def a_area_setup_sensor_3_btn_group(self):
        
            ### a area sensor 3 temp , rh , nh3 , h2s , pr now value
            self.area_sensor_now_value_s_3()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.a_s_3_r_time.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 3 button group temp 
            self.a_s_3_temp_top_g = QButtonGroup()
            self.a_s_3_temp_top_g.addButton(self.ui.a_s_3_temp_top_manual)
            self.a_s_3_temp_top_g.addButton(self.ui.a_s_3_temp_top_auto)
            
            self.a_s_3_temp_bottom_g = QButtonGroup()
            self.a_s_3_temp_bottom_g.addButton(self.ui.a_s_3_temp_bottom_manual)
            self.a_s_3_temp_bottom_g.addButton(self.ui.a_s_3_temp_bottom_auto)

            ### sensor 3 button group rh 
            self.a_s_3_rh_top_g = QButtonGroup()
            self.a_s_3_rh_top_g.addButton(self.ui.a_s_3_rh_top_manual)
            self.a_s_3_rh_top_g.addButton(self.ui.a_s_3_rh_top_auto)
            
            self.a_s_3_rh_bottom_g = QButtonGroup()
            self.a_s_3_rh_bottom_g.addButton(self.ui.a_s_3_rh_bottom_manual)
            self.a_s_3_rh_bottom_g.addButton(self.ui.a_s_3_rh_bottom_auto)
            
            ### sensor 3 button group nh3 
            self.a_s_3_nh3_top_g = QButtonGroup()
            self.a_s_3_nh3_top_g.addButton(self.ui.a_s_3_nh3_top_manual)
            self.a_s_3_nh3_top_g.addButton(self.ui.a_s_3_nh3_top_auto)
            
            self.a_s_3_nh3_bottom_g = QButtonGroup()
            self.a_s_3_nh3_bottom_g.addButton(self.ui.a_s_3_nh3_bottom_manual)
            self.a_s_3_nh3_bottom_g.addButton(self.ui.a_s_3_nh3_bottom_auto)

            ### sensor 3 button group h2s 
            self.a_s_3_h2s_top_g = QButtonGroup()
            self.a_s_3_h2s_top_g.addButton(self.ui.a_s_3_h2s_top_manual)
            self.a_s_3_h2s_top_g.addButton(self.ui.a_s_3_h2s_top_auto)
            
            self.a_s_3_h2s_bottom_g = QButtonGroup()
            self.a_s_3_h2s_bottom_g.addButton(self.ui.a_s_3_h2s_bottom_manual)
            self.a_s_3_h2s_bottom_g.addButton(self.ui.a_s_3_h2s_bottom_auto)

            ### sensor 3 button group pr 
            self.a_s_3_pr_top_g = QButtonGroup()
            self.a_s_3_pr_top_g.addButton(self.ui.a_s_3_pr_top_manual)
            self.a_s_3_pr_top_g.addButton(self.ui.a_s_3_pr_top_auto)
            
            self.a_s_3_pr_bottom_g = QButtonGroup()
            self.a_s_3_pr_bottom_g.addButton(self.ui.a_s_3_pr_bottom_manual)
            self.a_s_3_pr_bottom_g.addButton(self.ui.a_s_3_pr_bottom_auto)

    #######################################
    # E area setup sensor 2 button group
    #######################################
    def e_area_setup_sensor_2_btn_group(self):
        
            ### e area sensor 2 temp , rh , nh3 , h2s , pr now value
            self.e_area_sensor_now_value_s_2()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.e_s_r_time_2.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 2 button group temp 
            self.e_s_temp_top_2_g = QButtonGroup()
            self.e_s_temp_top_2_g.addButton(self.ui.e_s_temp_top_manual_2)
            self.e_s_temp_top_2_g.addButton(self.ui.e_s_temp_top_auto_2)
            
            self.e_s_temp_bottom_2_g = QButtonGroup()
            self.e_s_temp_bottom_2_g.addButton(self.ui.e_s_temp_bottom_manual_2)
            self.e_s_temp_bottom_2_g.addButton(self.ui.e_s_temp_bottom_auto_2)

            ### sensor 2 button group rh 
            self.e_s_rh_top_2_g = QButtonGroup()
            self.e_s_rh_top_2_g.addButton(self.ui.e_s_rh_top_manual_2)
            self.e_s_rh_top_2_g.addButton(self.ui.e_s_rh_top_auto_2)
            
            self.e_s_rh_bottom_2_g = QButtonGroup()
            self.e_s_rh_bottom_2_g.addButton(self.ui.e_s_rh_bottom_manual_2)
            self.e_s_rh_bottom_2_g.addButton(self.ui.e_s_rh_bottom_auto_2)
            
            ### sensor 2 button group nh3 
            self.e_s_nh3_top_2_g = QButtonGroup()
            self.e_s_nh3_top_2_g.addButton(self.ui.e_s_nh3_top_manual_2)
            self.e_s_nh3_top_2_g.addButton(self.ui.e_s_nh3_top_auto_2)
            
            self.e_s_nh3_bottom_2_g = QButtonGroup()
            self.e_s_nh3_bottom_2_g.addButton(self.ui.e_s_nh3_bottom_manual_2)
            self.e_s_nh3_bottom_2_g.addButton(self.ui.e_s_nh3_bottom_auto_2)

            ### sensor 2 button group h2s 
            self.e_s_h2s_top_2_g = QButtonGroup()
            self.e_s_h2s_top_2_g.addButton(self.ui.e_s_h2s_top_manual_2)
            self.e_s_h2s_top_2_g.addButton(self.ui.e_s_h2s_top_auto_2)
            
            self.e_s_h2s_bottom_2_g = QButtonGroup()
            self.e_s_h2s_bottom_2_g.addButton(self.ui.e_s_h2s_bottom_manual_2)
            self.e_s_h2s_bottom_2_g.addButton(self.ui.e_s_h2s_bottom_auto_2)

            ### sensor 2 button group pr 
            self.e_s_pr_top_2_g = QButtonGroup()
            self.e_s_pr_top_2_g.addButton(self.ui.e_s_pr_top_manual_2)
            self.e_s_pr_top_2_g.addButton(self.ui.e_s_pr_top_auto_2)
            
            self.e_s_pr_bottom_2_g = QButtonGroup()
            self.e_s_pr_bottom_2_g.addButton(self.ui.e_s_pr_bottom_manual_2)
            self.e_s_pr_bottom_2_g.addButton(self.ui.e_s_pr_bottom_auto_2)

    
    #######################################
    # D area setup sensor 2 button group
    #######################################
    def d_area_setup_sensor_2_btn_group(self):
        
            ### d area sensor 2 temp , rh , nh3 , h2s , pr now value
            self.d_area_sensor_now_value_s_2()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.d_s_r_time_2.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 2 button group temp 
            self.d_s_temp_top_2_g = QButtonGroup()
            self.d_s_temp_top_2_g.addButton(self.ui.d_s_temp_top_manual_2)
            self.d_s_temp_top_2_g.addButton(self.ui.d_s_temp_top_auto_2)
            
            self.d_s_temp_bottom_2_g = QButtonGroup()
            self.d_s_temp_bottom_2_g.addButton(self.ui.d_s_temp_bottom_manual_2)
            self.d_s_temp_bottom_2_g.addButton(self.ui.d_s_temp_bottom_auto_2)

            ### sensor 2 button group rh 
            self.d_s_rh_top_2_g = QButtonGroup()
            self.d_s_rh_top_2_g.addButton(self.ui.d_s_rh_top_manual_2)
            self.d_s_rh_top_2_g.addButton(self.ui.d_s_rh_top_auto_2)
            
            self.d_s_rh_bottom_2_g = QButtonGroup()
            self.d_s_rh_bottom_2_g.addButton(self.ui.d_s_rh_bottom_manual_2)
            self.d_s_rh_bottom_2_g.addButton(self.ui.d_s_rh_bottom_auto_2)
            
            ### sensor 2 button group nh3 
            self.d_s_nh3_top_2_g = QButtonGroup()
            self.d_s_nh3_top_2_g.addButton(self.ui.d_s_nh3_top_manual_2)
            self.d_s_nh3_top_2_g.addButton(self.ui.d_s_nh3_top_auto_2)
            
            self.d_s_nh3_bottom_2_g = QButtonGroup()
            self.d_s_nh3_bottom_2_g.addButton(self.ui.d_s_nh3_bottom_manual_2)
            self.d_s_nh3_bottom_2_g.addButton(self.ui.d_s_nh3_bottom_auto_2)

            ### sensor 2 button group h2s 
            self.d_s_h2s_top_2_g = QButtonGroup()
            self.d_s_h2s_top_2_g.addButton(self.ui.d_s_h2s_top_manual_2)
            self.d_s_h2s_top_2_g.addButton(self.ui.d_s_h2s_top_auto_2)
            
            self.d_s_h2s_bottom_2_g = QButtonGroup()
            self.d_s_h2s_bottom_2_g.addButton(self.ui.d_s_h2s_bottom_manual_2)
            self.d_s_h2s_bottom_2_g.addButton(self.ui.d_s_h2s_bottom_auto_2)

            ### sensor 2 button group pr 
            self.d_s_pr_top_2_g = QButtonGroup()
            self.d_s_pr_top_2_g.addButton(self.ui.d_s_pr_top_manual_2)
            self.d_s_pr_top_2_g.addButton(self.ui.d_s_pr_top_auto_2)
            
            self.d_s_pr_bottom_2_g = QButtonGroup()
            self.d_s_pr_bottom_2_g.addButton(self.ui.d_s_pr_bottom_manual_2)
            self.d_s_pr_bottom_2_g.addButton(self.ui.d_s_pr_bottom_auto_2)


    #######################################
    # C area setup sensor 2 button group
    #######################################
    def c_area_setup_sensor_2_btn_group(self):
        
            ### c area sensor 2 temp , rh , nh3 , h2s , pr now value
            self.c_area_sensor_now_value_s_2()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.c_s_r_time_2.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 2 button group temp 
            self.c_s_temp_top_2_g = QButtonGroup()
            self.c_s_temp_top_2_g.addButton(self.ui.c_s_temp_top_manual_2)
            self.c_s_temp_top_2_g.addButton(self.ui.c_s_temp_top_auto_2)
            
            self.c_s_temp_bottom_2_g = QButtonGroup()
            self.c_s_temp_bottom_2_g.addButton(self.ui.c_s_temp_bottom_manual_2)
            self.c_s_temp_bottom_2_g.addButton(self.ui.c_s_temp_bottom_auto_2)

            ### sensor 2 button group rh 
            self.c_s_rh_top_2_g = QButtonGroup()
            self.c_s_rh_top_2_g.addButton(self.ui.c_s_rh_top_manual_2)
            self.c_s_rh_top_2_g.addButton(self.ui.c_s_rh_top_auto_2)
            
            self.c_s_rh_bottom_2_g = QButtonGroup()
            self.c_s_rh_bottom_2_g.addButton(self.ui.c_s_rh_bottom_manual_2)
            self.c_s_rh_bottom_2_g.addButton(self.ui.c_s_rh_bottom_auto_2)
            
            ### sensor 2 button group nh3 
            self.c_s_nh3_top_2_g = QButtonGroup()
            self.c_s_nh3_top_2_g.addButton(self.ui.c_s_nh3_top_manual_2)
            self.c_s_nh3_top_2_g.addButton(self.ui.c_s_nh3_top_auto_2)
            
            self.c_s_nh3_bottom_2_g = QButtonGroup()
            self.c_s_nh3_bottom_2_g.addButton(self.ui.c_s_nh3_bottom_manual_2)
            self.c_s_nh3_bottom_2_g.addButton(self.ui.c_s_nh3_bottom_auto_2)

            ### sensor 2 button group h2s 
            self.c_s_h2s_top_2_g = QButtonGroup()
            self.c_s_h2s_top_2_g.addButton(self.ui.c_s_h2s_top_manual_2)
            self.c_s_h2s_top_2_g.addButton(self.ui.c_s_h2s_top_auto_2)
            
            self.c_s_h2s_bottom_2_g = QButtonGroup()
            self.c_s_h2s_bottom_2_g.addButton(self.ui.c_s_h2s_bottom_manual_2)
            self.c_s_h2s_bottom_2_g.addButton(self.ui.c_s_h2s_bottom_auto_2)

            ### sensor 2 button group pr 
            self.c_s_pr_top_2_g = QButtonGroup()
            self.c_s_pr_top_2_g.addButton(self.ui.c_s_pr_top_manual_2)
            self.c_s_pr_top_2_g.addButton(self.ui.c_s_pr_top_auto_2)
            
            self.c_s_pr_bottom_2_g = QButtonGroup()
            self.c_s_pr_bottom_2_g.addButton(self.ui.c_s_pr_bottom_manual_2)
            self.c_s_pr_bottom_2_g.addButton(self.ui.c_s_pr_bottom_auto_2)
    
    #######################################
    # B area setup sensor 2 button group
    #######################################
    def b_area_setup_sensor_2_btn_group(self):
        
            ### b area sensor 2 temp , rh , nh3 , h2s , pr now value
            self.b_area_sensor_now_value_s_2()
            
            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.b_s_r_time_2.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 2 button group temp 
            self.b_s_temp_top_2_g = QButtonGroup()
            self.b_s_temp_top_2_g.addButton(self.ui.b_s_temp_top_manual_2)
            self.b_s_temp_top_2_g.addButton(self.ui.b_s_temp_top_auto_2)
            
            self.b_s_temp_bottom_2_g = QButtonGroup()
            self.b_s_temp_bottom_2_g.addButton(self.ui.b_s_temp_bottom_manual_2)
            self.b_s_temp_bottom_2_g.addButton(self.ui.b_s_temp_bottom_auto_2)

            ### sensor 2 button group rh 
            self.b_s_rh_top_2_g = QButtonGroup()
            self.b_s_rh_top_2_g.addButton(self.ui.b_s_rh_top_manual_2)
            self.b_s_rh_top_2_g.addButton(self.ui.b_s_rh_top_auto_2)
            
            self.b_s_rh_bottom_2_g = QButtonGroup()
            self.b_s_rh_bottom_2_g.addButton(self.ui.b_s_rh_bottom_manual_2)
            self.b_s_rh_bottom_2_g.addButton(self.ui.b_s_rh_bottom_auto_2)
            
            ### sensor 2 button group nh3 
            self.b_s_nh3_top_2_g = QButtonGroup()
            self.b_s_nh3_top_2_g.addButton(self.ui.b_s_nh3_top_manual_2)
            self.b_s_nh3_top_2_g.addButton(self.ui.b_s_nh3_top_auto_2)
            
            self.b_s_nh3_bottom_2_g = QButtonGroup()
            self.b_s_nh3_bottom_2_g.addButton(self.ui.b_s_nh3_bottom_manual_2)
            self.b_s_nh3_bottom_2_g.addButton(self.ui.b_s_nh3_bottom_auto_2)

            ### sensor 2 button group h2s 
            self.b_s_h2s_top_2_g = QButtonGroup()
            self.b_s_h2s_top_2_g.addButton(self.ui.b_s_h2s_top_manual_2)
            self.b_s_h2s_top_2_g.addButton(self.ui.b_s_h2s_top_auto_2)
            
            self.b_s_h2s_bottom_2_g = QButtonGroup()
            self.b_s_h2s_bottom_2_g.addButton(self.ui.b_s_h2s_bottom_manual_2)
            self.b_s_h2s_bottom_2_g.addButton(self.ui.b_s_h2s_bottom_auto_2)

            ### sensor 2 button group pr 
            self.b_s_pr_top_2_g = QButtonGroup()
            self.b_s_pr_top_2_g.addButton(self.ui.b_s_pr_top_manual_2)
            self.b_s_pr_top_2_g.addButton(self.ui.b_s_pr_top_auto_2)
            
            self.b_s_pr_bottom_2_g = QButtonGroup()
            self.b_s_pr_bottom_2_g.addButton(self.ui.b_s_pr_bottom_manual_2)
            self.b_s_pr_bottom_2_g.addButton(self.ui.b_s_pr_bottom_auto_2)
    
    #######################################
    # A area setup sensor 2 button group
    #######################################
    def a_area_setup_sensor_2_btn_group(self):
        
            ### a area sensor 2 temp , rh , nh3 , h2s , pr now value
            self.area_sensor_now_value_s_2()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.a_s_2_r_time.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 2 button group temp 
            self.a_s_2_temp_top_g = QButtonGroup()
            self.a_s_2_temp_top_g.addButton(self.ui.a_s_2_temp_top_manual)
            self.a_s_2_temp_top_g.addButton(self.ui.a_s_2_temp_top_auto)
            
            self.a_s_2_temp_bottom_g = QButtonGroup()
            self.a_s_2_temp_bottom_g.addButton(self.ui.a_s_2_temp_bottom_manual)
            self.a_s_2_temp_bottom_g.addButton(self.ui.a_s_2_temp_bottom_auto)

            ### sensor 2 button group rh 
            self.a_s_2_rh_top_g = QButtonGroup()
            self.a_s_2_rh_top_g.addButton(self.ui.a_s_2_rh_top_manual)
            self.a_s_2_rh_top_g.addButton(self.ui.a_s_2_rh_top_auto)
            
            self.a_s_2_rh_bottom_g = QButtonGroup()
            self.a_s_2_rh_bottom_g.addButton(self.ui.a_s_2_rh_bottom_manual)
            self.a_s_2_rh_bottom_g.addButton(self.ui.a_s_2_rh_bottom_auto)
            
            ### sensor 2 button group nh3 
            self.a_s_2_nh3_top_g = QButtonGroup()
            self.a_s_2_nh3_top_g.addButton(self.ui.a_s_2_nh3_top_manual)
            self.a_s_2_nh3_top_g.addButton(self.ui.a_s_2_nh3_top_auto)
            
            self.a_s_2_nh3_bottom_g = QButtonGroup()
            self.a_s_2_nh3_bottom_g.addButton(self.ui.a_s_2_nh3_bottom_manual)
            self.a_s_2_nh3_bottom_g.addButton(self.ui.a_s_2_nh3_bottom_auto)

            ### sensor 2 button group h2s 
            self.a_s_2_h2s_top_g = QButtonGroup()
            self.a_s_2_h2s_top_g.addButton(self.ui.a_s_2_h2s_top_manual)
            self.a_s_2_h2s_top_g.addButton(self.ui.a_s_2_h2s_top_auto)
            
            self.a_s_2_h2s_bottom_g = QButtonGroup()
            self.a_s_2_h2s_bottom_g.addButton(self.ui.a_s_2_h2s_bottom_manual)
            self.a_s_2_h2s_bottom_g.addButton(self.ui.a_s_2_h2s_bottom_auto)

            ### sensor 2 button group pr 
            self.a_s_2_pr_top_g = QButtonGroup()
            self.a_s_2_pr_top_g.addButton(self.ui.a_s_2_pr_top_manual)
            self.a_s_2_pr_top_g.addButton(self.ui.a_s_2_pr_top_auto)
            
            self.a_s_2_pr_bottom_g = QButtonGroup()
            self.a_s_2_pr_bottom_g.addButton(self.ui.a_s_2_pr_bottom_manual)
            self.a_s_2_pr_bottom_g.addButton(self.ui.a_s_2_pr_bottom_auto)
    
    #######################################
    # E area setup sensor 1 button group
    #######################################
    def e_area_setup_sensor_1_btn_group(self):
        
            ### e area sensor 1 temp , rh , nh3 , h2s , pr now value
            self.e_area_sensor_now_value_s_1()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.e_s_r_time_1.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 1 button group temp 
            self.e_s_temp_top_1_g = QButtonGroup()
            self.e_s_temp_top_1_g.addButton(self.ui.e_s_temp_top_manual_1)
            self.e_s_temp_top_1_g.addButton(self.ui.e_s_temp_top_auto_1)
            
            self.e_s_temp_bottom_1_g = QButtonGroup()
            self.e_s_temp_bottom_1_g.addButton(self.ui.e_s_temp_bottom_manual_1)
            self.e_s_temp_bottom_1_g.addButton(self.ui.e_s_temp_bottom_auto_1)

            ### sensor 1 button group rh 
            self.e_s_rh_top_1_g = QButtonGroup()
            self.e_s_rh_top_1_g.addButton(self.ui.e_s_rh_top_manual_1)
            self.e_s_rh_top_1_g.addButton(self.ui.e_s_rh_top_auto_1)
            
            self.e_s_rh_bottom_1_g = QButtonGroup()
            self.e_s_rh_bottom_1_g.addButton(self.ui.e_s_rh_bottom_manual_1)
            self.e_s_rh_bottom_1_g.addButton(self.ui.e_s_rh_bottom_auto_1)
            
            ### sensor 1 button group nh3 
            self.e_s_nh3_top_1_g = QButtonGroup()
            self.e_s_nh3_top_1_g.addButton(self.ui.e_s_nh3_top_manual_1)
            self.e_s_nh3_top_1_g.addButton(self.ui.e_s_nh3_top_auto_1)
            
            self.e_s_nh3_bottom_1_g = QButtonGroup()
            self.e_s_nh3_bottom_1_g.addButton(self.ui.e_s_nh3_bottom_manual_1)
            self.e_s_nh3_bottom_1_g.addButton(self.ui.e_s_nh3_bottom_auto_1)

            ### sensor 1 button group h2s 
            self.e_s_h2s_top_1_g = QButtonGroup()
            self.e_s_h2s_top_1_g.addButton(self.ui.e_s_h2s_top_manual_1)
            self.e_s_h2s_top_1_g.addButton(self.ui.e_s_h2s_top_auto_1)
            
            self.e_s_h2s_bottom_1_g = QButtonGroup()
            self.e_s_h2s_bottom_1_g.addButton(self.ui.e_s_h2s_bottom_manual_1)
            self.e_s_h2s_bottom_1_g.addButton(self.ui.e_s_h2s_bottom_auto_1)

            ### sensor 1 button group pr 
            self.e_s_pr_top_1_g = QButtonGroup()
            self.e_s_pr_top_1_g.addButton(self.ui.e_s_pr_top_manual_1)
            self.e_s_pr_top_1_g.addButton(self.ui.e_s_pr_top_auto_1)
            
            self.e_s_pr_bottom_1_g = QButtonGroup()
            self.e_s_pr_bottom_1_g.addButton(self.ui.e_s_pr_bottom_manual_1)
            self.e_s_pr_bottom_1_g.addButton(self.ui.e_s_pr_bottom_auto_1)
    
    #######################################
    # D area setup sensor 1 button group
    #######################################
    def d_area_setup_sensor_1_btn_group(self):
        
            ### d area sensor 1 temp , rh , nh3 , h2s , pr now value
            self.d_area_sensor_now_value_s_1()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.d_s_r_time_1.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 1 button group temp 
            self.d_s_temp_top_1_g = QButtonGroup()
            self.d_s_temp_top_1_g.addButton(self.ui.d_s_temp_top_manual_1)
            self.d_s_temp_top_1_g.addButton(self.ui.d_s_temp_top_auto_1)
            
            self.d_s_temp_bottom_1_g = QButtonGroup()
            self.d_s_temp_bottom_1_g.addButton(self.ui.d_s_temp_bottom_manual_1)
            self.d_s_temp_bottom_1_g.addButton(self.ui.d_s_temp_bottom_auto_1)

            ### sensor 1 button group rh 
            self.d_s_rh_top_1_g = QButtonGroup()
            self.d_s_rh_top_1_g.addButton(self.ui.d_s_rh_top_manual_1)
            self.d_s_rh_top_1_g.addButton(self.ui.d_s_rh_top_auto_1)
            
            self.d_s_rh_bottom_1_g = QButtonGroup()
            self.d_s_rh_bottom_1_g.addButton(self.ui.d_s_rh_bottom_manual_1)
            self.d_s_rh_bottom_1_g.addButton(self.ui.d_s_rh_bottom_auto_1)
            
            ### sensor 1 button group nh3 
            self.d_s_nh3_top_1_g = QButtonGroup()
            self.d_s_nh3_top_1_g.addButton(self.ui.d_s_nh3_top_manual_1)
            self.d_s_nh3_top_1_g.addButton(self.ui.d_s_nh3_top_auto_1)
            
            self.d_s_nh3_bottom_1_g = QButtonGroup()
            self.d_s_nh3_bottom_1_g.addButton(self.ui.d_s_nh3_bottom_manual_1)
            self.d_s_nh3_bottom_1_g.addButton(self.ui.d_s_nh3_bottom_auto_1)

            ### sensor 1 button group h2s 
            self.d_s_h2s_top_1_g = QButtonGroup()
            self.d_s_h2s_top_1_g.addButton(self.ui.d_s_h2s_top_manual_1)
            self.d_s_h2s_top_1_g.addButton(self.ui.d_s_h2s_top_auto_1)
            
            self.d_s_h2s_bottom_1_g = QButtonGroup()
            self.d_s_h2s_bottom_1_g.addButton(self.ui.d_s_h2s_bottom_manual_1)
            self.d_s_h2s_bottom_1_g.addButton(self.ui.d_s_h2s_bottom_auto_1)

            ### sensor 1 button group pr 
            self.d_s_pr_top_1_g = QButtonGroup()
            self.d_s_pr_top_1_g.addButton(self.ui.d_s_pr_top_manual_1)
            self.d_s_pr_top_1_g.addButton(self.ui.d_s_pr_top_auto_1)
            
            self.d_s_pr_bottom_1_g = QButtonGroup()
            self.d_s_pr_bottom_1_g.addButton(self.ui.d_s_pr_bottom_manual_1)
            self.d_s_pr_bottom_1_g.addButton(self.ui.d_s_pr_bottom_auto_1)
    
    #######################################
    # C area setup sensor 1 button group
    #######################################
    def c_area_setup_sensor_1_btn_group(self):
        
            ### c area sensor 1 temp , rh , nh3 , h2s , pr now value
            self.c_area_sensor_now_value_s_1()

            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.c_s_r_time_1.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 1 button group temp 
            self.c_s_temp_top_1_g = QButtonGroup()
            self.c_s_temp_top_1_g.addButton(self.ui.c_s_temp_top_manual_1)
            self.c_s_temp_top_1_g.addButton(self.ui.c_s_temp_top_auto_1)
            
            self.c_s_temp_bottom_1_g = QButtonGroup()
            self.c_s_temp_bottom_1_g.addButton(self.ui.c_s_temp_bottom_manual_1)
            self.c_s_temp_bottom_1_g.addButton(self.ui.c_s_temp_bottom_auto_1)

            ### sensor 1 button group rh 
            self.c_s_rh_top_1_g = QButtonGroup()
            self.c_s_rh_top_1_g.addButton(self.ui.c_s_rh_top_manual_1)
            self.c_s_rh_top_1_g.addButton(self.ui.c_s_rh_top_auto_1)
            
            self.c_s_rh_bottom_1_g = QButtonGroup()
            self.c_s_rh_bottom_1_g.addButton(self.ui.c_s_rh_bottom_manual_1)
            self.c_s_rh_bottom_1_g.addButton(self.ui.c_s_rh_bottom_auto_1)
            
            ### sensor 1 button group nh3 
            self.c_s_nh3_top_1_g = QButtonGroup()
            self.c_s_nh3_top_1_g.addButton(self.ui.c_s_nh3_top_manual_1)
            self.c_s_nh3_top_1_g.addButton(self.ui.c_s_nh3_top_auto_1)
            
            self.c_s_nh3_bottom_1_g = QButtonGroup()
            self.c_s_nh3_bottom_1_g.addButton(self.ui.c_s_nh3_bottom_manual_1)
            self.c_s_nh3_bottom_1_g.addButton(self.ui.c_s_nh3_bottom_auto_1)

            ### sensor 1 button group h2s 
            self.c_s_h2s_top_1_g = QButtonGroup()
            self.c_s_h2s_top_1_g.addButton(self.ui.c_s_h2s_top_manual_1)
            self.c_s_h2s_top_1_g.addButton(self.ui.c_s_h2s_top_auto_1)
            
            self.c_s_h2s_bottom_1_g = QButtonGroup()
            self.c_s_h2s_bottom_1_g.addButton(self.ui.c_s_h2s_bottom_manual_1)
            self.c_s_h2s_bottom_1_g.addButton(self.ui.c_s_h2s_bottom_auto_1)

            ### sensor 1 button group pr 
            self.c_s_pr_top_1_g = QButtonGroup()
            self.c_s_pr_top_1_g.addButton(self.ui.c_s_pr_top_manual_1)
            self.c_s_pr_top_1_g.addButton(self.ui.c_s_pr_top_auto_1)
            
            self.c_s_pr_bottom_1_g = QButtonGroup()
            self.c_s_pr_bottom_1_g.addButton(self.ui.c_s_pr_bottom_manual_1)
            self.c_s_pr_bottom_1_g.addButton(self.ui.c_s_pr_bottom_auto_1)
    
    #######################################
    # B area setup sensor 1 button group
    #######################################
    def b_area_setup_sensor_1_btn_group(self):
        
            ### b area sensor 1 temp , rh , nh3 , h2s , pr now value
            self.b_area_sensor_now_value_s_1()
            
            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.b_s_r_time_1.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 1 button group temp 
            self.b_s_temp_top_1_g = QButtonGroup()
            self.b_s_temp_top_1_g.addButton(self.ui.b_s_temp_top_manual_1)
            self.b_s_temp_top_1_g.addButton(self.ui.b_s_temp_top_auto_1)
            
            self.b_s_temp_bottom_1_g = QButtonGroup()
            self.b_s_temp_bottom_1_g.addButton(self.ui.b_s_temp_bottom_manual_1)
            self.b_s_temp_bottom_1_g.addButton(self.ui.b_s_temp_bottom_auto_1)

            ### sensor 1 button group rh 
            self.b_s_rh_top_1_g = QButtonGroup()
            self.b_s_rh_top_1_g.addButton(self.ui.b_s_rh_top_manual_1)
            self.b_s_rh_top_1_g.addButton(self.ui.b_s_rh_top_auto_1)
            
            self.b_s_rh_bottom_1_g = QButtonGroup()
            self.b_s_rh_bottom_1_g.addButton(self.ui.b_s_rh_bottom_manual_1)
            self.b_s_rh_bottom_1_g.addButton(self.ui.b_s_rh_bottom_auto_1)
            
            ### sensor 1 button group nh3 
            self.b_s_nh3_top_1_g = QButtonGroup()
            self.b_s_nh3_top_1_g.addButton(self.ui.b_s_nh3_top_manual_1)
            self.b_s_nh3_top_1_g.addButton(self.ui.b_s_nh3_top_auto_1)
            
            self.b_s_nh3_bottom_1_g = QButtonGroup()
            self.b_s_nh3_bottom_1_g.addButton(self.ui.b_s_nh3_bottom_manual_1)
            self.b_s_nh3_bottom_1_g.addButton(self.ui.b_s_nh3_bottom_auto_1)

            ### sensor 1 button group h2s 
            self.b_s_h2s_top_1_g = QButtonGroup()
            self.b_s_h2s_top_1_g.addButton(self.ui.b_s_h2s_top_manual_1)
            self.b_s_h2s_top_1_g.addButton(self.ui.b_s_h2s_top_auto_1)
            
            self.b_s_h2s_bottom_1_g = QButtonGroup()
            self.b_s_h2s_bottom_1_g.addButton(self.ui.b_s_h2s_bottom_manual_1)
            self.b_s_h2s_bottom_1_g.addButton(self.ui.b_s_h2s_bottom_auto_1)

            ### sensor 1 button group pr 
            self.b_s_pr_top_1_g = QButtonGroup()
            self.b_s_pr_top_1_g.addButton(self.ui.b_s_pr_top_manual_1)
            self.b_s_pr_top_1_g.addButton(self.ui.b_s_pr_top_auto_1)
            
            self.b_s_pr_bottom_1_g = QButtonGroup()
            self.b_s_pr_bottom_1_g.addButton(self.ui.b_s_pr_bottom_manual_1)
            self.b_s_pr_bottom_1_g.addButton(self.ui.b_s_pr_bottom_auto_1)

    #######################################
    # A area setup sensor 1 button group
    #######################################
    def a_area_setup_sensor_1_btn_group(self):
        
            ### a area sensor 1 temp , rh , nh3 , h2s , pr now value
            self.area_sensor_now_value_s_1()
            
            ### record time
            self.n_t = QDateTime.currentDateTime()
            self.r_n_t = self.n_t.toString("yyyy-MM-dd HH:mm:ss")
            self.ui.a_s_1_r_time.setText('更新時間 ' + str(self.r_n_t))

            ### sensor 1 button group temp 
            self.a_s_1_temp_top_g = QButtonGroup()
            self.a_s_1_temp_top_g.addButton(self.ui.a_s_1_temp_top_manual)
            self.a_s_1_temp_top_g.addButton(self.ui.a_s_1_temp_top_auto)
            
            self.a_s_1_temp_bottom_g = QButtonGroup()
            self.a_s_1_temp_bottom_g.addButton(self.ui.a_s_1_temp_bottom_manual)
            self.a_s_1_temp_bottom_g.addButton(self.ui.a_s_1_temp_bottom_auto)

            ### sensor 1 button group rh 
            self.a_s_1_rh_top_g = QButtonGroup()
            self.a_s_1_rh_top_g.addButton(self.ui.a_s_1_rh_top_manual)
            self.a_s_1_rh_top_g.addButton(self.ui.a_s_1_rh_top_auto)
            
            self.a_s_1_rh_bottom_g = QButtonGroup()
            self.a_s_1_rh_bottom_g.addButton(self.ui.a_s_1_rh_bottom_manual)
            self.a_s_1_rh_bottom_g.addButton(self.ui.a_s_1_rh_bottom_auto)
            
            ### sensor 1 button group nh3 
            self.a_s_1_nh3_top_g = QButtonGroup()
            self.a_s_1_nh3_top_g.addButton(self.ui.a_s_1_nh3_top_manual)
            self.a_s_1_nh3_top_g.addButton(self.ui.a_s_1_nh3_top_auto)
            
            self.a_s_1_nh3_bottom_g = QButtonGroup()
            self.a_s_1_nh3_bottom_g.addButton(self.ui.a_s_1_nh3_bottom_manual)
            self.a_s_1_nh3_bottom_g.addButton(self.ui.a_s_1_nh3_bottom_auto)

            ### sensor 1 button group h2s 
            self.a_s_1_h2s_top_g = QButtonGroup()
            self.a_s_1_h2s_top_g.addButton(self.ui.a_s_1_h2s_top_manual)
            self.a_s_1_h2s_top_g.addButton(self.ui.a_s_1_h2s_top_auto)
            
            self.a_s_1_h2s_bottom_g = QButtonGroup()
            self.a_s_1_h2s_bottom_g.addButton(self.ui.a_s_1_h2s_bottom_manual)
            self.a_s_1_h2s_bottom_g.addButton(self.ui.a_s_1_h2s_bottom_auto)

            ### sensor 1 button group pr 
            self.a_s_1_pr_top_g = QButtonGroup()
            self.a_s_1_pr_top_g.addButton(self.ui.a_s_1_pr_top_manual)
            self.a_s_1_pr_top_g.addButton(self.ui.a_s_1_pr_top_auto)
            
            self.a_s_1_pr_bottom_g = QButtonGroup()
            self.a_s_1_pr_bottom_g.addButton(self.ui.a_s_1_pr_bottom_manual)
            self.a_s_1_pr_bottom_g.addButton(self.ui.a_s_1_pr_bottom_auto)

    #####################################
    # e area sensor now value sensor 3
    #####################################
    def e_area_sensor_now_value_s_3(self):
            ### variables
            self.area = 'E'
            self.id   = 19

            self.temp = self.ui.e_s_temp_3
            self.rh   = self.ui.e_s_rh_3
            self.nh3  = self.ui.e_s_nh3_3
            self.h2s  = self.ui.e_s_h2s_3
            self.pr   = self.ui.e_s_pr_3

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > e area setup sensor 3 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # e area sensor now value sensor 2
    #####################################
    def e_area_sensor_now_value_s_2(self):
            ### variables
            self.area = 'E'
            self.id   = 18

            self.temp = self.ui.e_s_temp_2
            self.rh   = self.ui.e_s_rh_2
            self.nh3  = self.ui.e_s_nh3_2
            self.h2s  = self.ui.e_s_h2s_2
            self.pr   = self.ui.e_s_pr_2

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > e area setup sensor 2 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # e area sensor now value sensor 1
    #####################################
    def e_area_sensor_now_value_s_1(self):
            ### variables
            self.area = 'E'
            self.id   = 17

            self.temp = self.ui.e_s_temp_1
            self.rh   = self.ui.e_s_rh_1
            self.nh3  = self.ui.e_s_nh3_1
            self.h2s  = self.ui.e_s_h2s_1
            self.pr   = self.ui.e_s_pr_1

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > e area setup sensor 1 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # d area sensor now value sensor 4
    #####################################
    def d_area_sensor_now_value_s_4(self):
            ### variables
            self.area = 'D'
            self.id   = 16

            self.temp = self.ui.d_s_temp_4
            self.rh   = self.ui.d_s_rh_4
            self.nh3  = self.ui.d_s_nh3_4
            self.h2s  = self.ui.d_s_h2s_4
            self.pr   = self.ui.d_s_pr_4

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > d area setup sensor 4 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # d area sensor now value sensor 3
    #####################################
    def d_area_sensor_now_value_s_3(self):
            ### variables
            self.area = 'D'
            self.id   = 15

            self.temp = self.ui.d_s_temp_3
            self.rh   = self.ui.d_s_rh_3
            self.nh3  = self.ui.d_s_nh3_3
            self.h2s  = self.ui.d_s_h2s_3
            self.pr   = self.ui.d_s_pr_3

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > d area setup sensor 3 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # d area sensor now value sensor 2
    #####################################
    def d_area_sensor_now_value_s_2(self):
            ### variables
            self.area = 'D'
            self.id   = 14

            self.temp = self.ui.d_s_temp_2
            self.rh   = self.ui.d_s_rh_2
            self.nh3  = self.ui.d_s_nh3_2
            self.h2s  = self.ui.d_s_h2s_2
            self.pr   = self.ui.d_s_pr_2

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > d area setup sensor 2 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # d area sensor now value sensor 1
    #####################################
    def d_area_sensor_now_value_s_1(self):
            ### variables
            self.area = 'D'
            self.id   = 13

            self.temp = self.ui.d_s_temp_1
            self.rh   = self.ui.d_s_rh_1
            self.nh3  = self.ui.d_s_nh3_1
            self.h2s  = self.ui.d_s_h2s_1
            self.pr   = self.ui.d_s_pr_1

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > d area setup sensor 1 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # c area sensor now value sensor 5
    #####################################
    def c_area_sensor_now_value_s_5(self):
            ### variables
            self.area = 'C'
            self.id   = 12

            self.temp = self.ui.c_s_temp_5
            self.rh   = self.ui.c_s_rh_5
            self.nh3  = self.ui.c_s_nh3_5
            self.h2s  = self.ui.c_s_h2s_5
            self.pr   = self.ui.c_s_pr_5

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > c area setup sensor 5 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # c area sensor now value sensor 4
    #####################################
    def c_area_sensor_now_value_s_4(self):
            ### variables
            self.area = 'C'
            self.id   = 11

            self.temp = self.ui.c_s_temp_4
            self.rh   = self.ui.c_s_rh_4
            self.nh3  = self.ui.c_s_nh3_4
            self.h2s  = self.ui.c_s_h2s_4
            self.pr   = self.ui.c_s_pr_4

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > c area setup sensor 4 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # c area sensor now value sensor 3
    #####################################
    def c_area_sensor_now_value_s_3(self):
            ### variables
            self.area = 'C'
            self.id   = 10

            self.temp = self.ui.c_s_temp_3
            self.rh   = self.ui.c_s_rh_3
            self.nh3  = self.ui.c_s_nh3_3
            self.h2s  = self.ui.c_s_h2s_3
            self.pr   = self.ui.c_s_pr_3

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > c area setup sensor 3 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # c area sensor now value sensor 2
    #####################################
    def c_area_sensor_now_value_s_2(self):
            ### variables
            self.area = 'C'
            self.id   = 9

            self.temp = self.ui.c_s_temp_2
            self.rh   = self.ui.c_s_rh_2
            self.nh3  = self.ui.c_s_nh3_2
            self.h2s  = self.ui.c_s_h2s_2
            self.pr   = self.ui.c_s_pr_2

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > c area setup sensor 2 btn group : ' + str(e))
            finally:
                pass
    
    #####################################
    # c area sensor now value sensor 1
    #####################################
    def c_area_sensor_now_value_s_1(self):
            ### variables
            self.area = 'C'
            self.id   = 8

            self.temp = self.ui.c_s_temp_1
            self.rh   = self.ui.c_s_rh_1
            self.nh3  = self.ui.c_s_nh3_1
            self.h2s  = self.ui.c_s_h2s_1
            self.pr   = self.ui.c_s_pr_1

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > c area setup sensor 8 btn group : ' + str(e))
            finally:
                pass

    ###################################
    # b area sensor now value sensor 3
    ###################################
    def b_area_sensor_now_value_s_3(self):
            ### variables
            self.area = 'B'
            self.id   = 7

            self.temp = self.ui.b_s_temp_3
            self.rh   = self.ui.b_s_rh_3
            self.nh3  = self.ui.b_s_nh3_3
            self.h2s  = self.ui.b_s_h2s_3
            self.pr   = self.ui.b_s_pr_3

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > b area setup sensor 7 btn group : ' + str(e))
            finally:
                pass
    
    ###################################
    # b area sensor now value sensor 2
    ###################################
    def b_area_sensor_now_value_s_2(self):
            ### variables
            self.area = 'B'
            self.id   = 6

            self.temp = self.ui.b_s_temp_2
            self.rh   = self.ui.b_s_rh_2
            self.nh3  = self.ui.b_s_nh3_2
            self.h2s  = self.ui.b_s_h2s_2
            self.pr   = self.ui.b_s_pr_2

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass

    ###################################
    # b area sensor now value sensor 1
    ###################################
    def b_area_sensor_now_value_s_1(self):
            ### variables
            self.area = 'B'
            self.id   = 5

            self.temp = self.ui.b_s_temp_1
            self.rh   = self.ui.b_s_rh_1
            self.nh3  = self.ui.b_s_nh3_1
            self.h2s  = self.ui.b_s_h2s_1
            self.pr   = self.ui.b_s_pr_1

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass
    
    ###################################
    # area sensor now value sensor 4
    ###################################
    def area_sensor_now_value_s_4(self):
            ### variables
            self.area = 'A'
            self.id   = 4

            self.temp = self.ui.a_s_4_temp
            self.rh   = self.ui.a_s_4_rh
            self.nh3  = self.ui.a_s_4_nh3
            self.h2s  = self.ui.a_s_4_h2s
            self.pr   = self.ui.a_s_4_pr

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass

    ###################################
    # area sensor now value sensor 3
    ###################################
    def area_sensor_now_value_s_3(self):
            ### variables
            self.area = 'A'
            self.id   = 3

            self.temp = self.ui.a_s_3_temp
            self.rh   = self.ui.a_s_3_rh
            self.nh3  = self.ui.a_s_3_nh3
            self.h2s  = self.ui.a_s_3_h2s
            self.pr   = self.ui.a_s_3_pr

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass

    ###################################
    # area sensor now value sensor 2
    ###################################
    def area_sensor_now_value_s_2(self):
            ### variables
            self.area = 'A'
            self.id   = 2

            self.temp = self.ui.a_s_2_temp
            self.rh   = self.ui.a_s_2_rh
            self.nh3  = self.ui.a_s_2_nh3
            self.h2s  = self.ui.a_s_2_h2s
            self.pr   = self.ui.a_s_2_pr

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass
    
    ###################################
    # area sensor now value sensor 1
    ###################################
    def area_sensor_now_value_s_1(self):
            ### variables
            self.area = 'A'
            self.id   = 1

            self.temp = self.ui.a_s_1_temp
            self.rh   = self.ui.a_s_1_rh
            self.nh3  = self.ui.a_s_1_nh3
            self.h2s  = self.ui.a_s_1_h2s
            self.pr   = self.ui.a_s_1_pr

            ### record time
            self.n_time = QDateTime.currentDateTime()
            self.tb     = self.n_time.toString("yyyy_MM")
            
            try:
                
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()

                ### now temp value
                self.now_temp_sql = "select val_1 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_temp_sql)
                self.res = self.curr.fetchone()
                self.temp.setText(str(self.res[0]))

                ### now rh value
                self.now_rh_sql = "select val_2 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_rh_sql)
                self.res = self.curr.fetchone()
                self.rh.setText(str(self.res[0]))

                ### now nh3 value
                self.now_nh3_sql = "select val_3 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_nh3_sql)
                self.res = self.curr.fetchone()
                self.nh3.setText(str(self.res[0]))

                ### now h2s value
                self.now_h2s_sql = "select val_4 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_h2s_sql)
                self.res = self.curr.fetchone()
                self.h2s.setText(str(self.res[0]))

                ### now pr value
                self.now_pr_sql = "select val_5 from {0} where s_area='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.tb , self.area , self.id)
                self.curr.execute(self.now_pr_sql)
                self.res = self.curr.fetchone()
                self.pr.setText(str(self.res[0]))
                
                self.conn.commit()
                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , '< Error > a area setup sensor 1 btn group : ' + str(e))
            finally:
                pass
    
    #########################################
    # work record normal user account list
    #########################################
    def work_record_normal_user_account_list(self):
        try:
            #################
            # admin lv = 1
            #################
            if s_lv == '1':
                ### work record
                self.work_record(s_user , '日誌 - 載入一般使用者帳號清單')

                ### clear
                self.ui.n_u_work_record_account_list.clear()

                ### start time , stop time
                self.ui.n_m_work_record_start_time.setDateTime(QDateTime.currentDateTime())
                self.ui.n_m_work_record_end_time.setDateTime(QDateTime.currentDateTime())
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='3' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.n_u_work_record_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
            
                ### click normal account detail
                self.ui.n_u_work_record_account_list.itemClicked.connect(self.work_record_select_normal_user_account_detail)
                ### double click normal account detail
                self.ui.n_u_work_record_account_list.itemDoubleClicked.connect(self.work_record_query_by_normal_manager_user_account)

                self.conn.commit()
                self.conn.close()    
            
            ########################
            # normal admin lv = 2
            ########################
            elif s_lv == '2':
                
                ### work record
                self.work_record(s_user , '日誌 - 載入一般使用者帳號清單')
                
                ### clear
                self.ui.n_u_work_record_account_list.clear()

                ### enable
                self.ui.n_m_work_record_start_time.setEnabled(True)
                self.ui.n_m_work_record_end_time.setEnabled(True)

                ### start time , stop time
                self.ui.n_m_work_record_start_time.setDateTime(QDateTime.currentDateTime())
                self.ui.n_m_work_record_end_time.setDateTime(QDateTime.currentDateTime())
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='3' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.n_u_work_record_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
            
                ### click normal account detail
                self.ui.n_u_work_record_account_list.itemClicked.connect(self.work_record_select_normal_user_account_detail)
                ### double click normal account detail
                self.ui.n_u_work_record_account_list.itemDoubleClicked.connect(self.work_record_query_by_normal_manager_user_account)

                self.conn.commit()
                self.conn.close()    
                
            #######################
            # normal user lv = 3   
            ########################             
            elif s_lv == '3':
                
                ### work record
                self.work_record(s_user , '日誌 - 載入一般使用者帳號清單 , 無使用權限')

                ### clear
                self.ui.n_u_work_record_account_list.clear()
                ### show message
                self.ui.n_u_work_record_account_list.addItem(str('無使用權限'))
                ### disable
                self.ui.n_m_work_record_start_time.setEnabled(False)
                self.ui.n_m_work_record_end_time.setEnabled(False)
                self.ui.page_2_work_record.setEnabled(False)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work record normal user account list : ' + str(e))
        finally:
            pass


    #############################
    # normal user account list
    #############################
    def normal_user_account_list(self):
        try:
            #################
            # admin lv = 1
            #################
            if s_lv == '1':
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般使用者帳號清單')

                ### clear
                self.ui.normal_user_account_list.clear()

                ### disable / enable
                self.ui.n_user_combox_lv.setEnabled(False)
                self.ui.n_user_combox_status.setEnabled(False)
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='3' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.normal_user_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
            
                ### click normal account detail
                self.ui.normal_user_account_list.itemDoubleClicked.connect(self.select_normal_user_account_detail)

                self.conn.commit()
                self.conn.close()    
            
            ########################
            # normal admin lv = 2
            ########################
            elif s_lv == '2':
                
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般使用者帳號清單')
                
                ### clear
                self.ui.normal_user_account_list.clear()

                ### disable / enable
                self.ui.n_user_combox_lv.setEnabled(False)
                self.ui.n_user_combox_status.setEnabled(False)
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='3' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                    self.ui.normal_user_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
            
                ### click normal account detail
                self.ui.normal_user_account_list.itemDoubleClicked.connect(self.select_normal_user_account_detail)

                self.conn.commit()
                self.conn.close()    
                
            #######################
            # normal user lv = 3   
            ########################             
            elif s_lv == '3':
                
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般使用者帳號清單 , 無使用權限')

                ### clear
                self.ui.normal_user_account_list.clear()
                ### show message
                self.ui.normal_user_account_list.addItem(str('無使用權限'))
                ### disable
                self.ui.n_user_user.setEnabled(False)
                self.ui.n_user_pwd.setEnabled(False)
                self.ui.n_user_lv.setEnabled(False)
                self.ui.n_user_combox_lv.setEnabled(False)
                self.ui.n_user_status.setEnabled(False)
                self.ui.n_user_combox_status.setEnabled(False)
                self.ui.page_1_account.setEnabled(False)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > normal user account list : ' + str(e))
        finally:
            pass

    ###############################################################
    # work record query by normal manager user account
    ###############################################################
    def work_record_query_by_normal_manager_user_account(self , item):
        try:
            ### normal user
            self.data = item.text().split(',')
            self.data2 = self.data[1].split('(') 
            self.user = self.data2[0]
            self.user = self.user.strip()

            ### query start time and stop time
            self.start_time = self.ui.n_m_work_record_start_time.text()
            self.stop_time = self.ui.n_m_work_record_end_time.text()

            ### work record
            self.work_record(s_user , '點擊日誌 , ' + self.start_time + ' ~ ' + self.stop_time  + ' ,  查詢帳號 : ' + self.user + ' 使用記錄')

            ### clear
            self.ui.query_work_record_list.clear()

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select r_time , o_item from work_record where a_user='{0}' and r_time>='{1}' and r_time<='{2}' order by r_time desc".format(self.user , self.start_time , self.stop_time)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            self.conn.commit()

            for val in self.res:
                self.ui.query_work_record_list.addItem(str(val[0]) + ' , ' + str(val[1]))

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work record query by normal manager user account : ' + str(e))
        finally:
            self.conn.close()        


    ##################################################
    # work record select normal user account detail
    ##################################################
    def work_record_select_normal_user_account_detail(self , item):
        try:
            ### normal user
            self.data = item.text().split(',')
            self.data2 = self.data[1].split('(') 
            self.user = self.data2[0]
            self.user = self.user.strip()

            ### work record
            self.work_record(s_user , '點擊日誌 , 查詢帳號 : ' + self.user + ' 使用記錄')

            ### clear
            self.ui.final_work_record_list.clear()

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select r_time , o_item from work_record where a_user='{0}' order by r_time desc limit 0,50".format(self.user)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                self.ui.final_work_record_list.addItem(str(val[0]) + ' , ' + str(val[1]))

            self.conn.commit()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > normal manager account list : ' + str(e))
        finally:
            self.conn.close()        
    
    ######################################
    # select normal user account detail
    ######################################
    def select_normal_user_account_detail(self , item):
        try:
            ### disable / enable
            self.ui.n_user_user.setEnabled(False)
            self.ui.n_user_lv.setEnabled(False)
            self.ui.n_user_status.setEnabled(False)
            
            if s_lv == '1':
                self.ui.n_user_combox_lv.setEnabled(True)
            elif s_lv == '2':
                self.ui.n_user_combox_lv.setEnabled(False)

            self.ui.n_user_combox_status.setEnabled(True)
            
            ### normal user
            self.data = item.text().split(',')
            self.data2 = self.data[1].split('(') 
            self.user = self.data2[0]
            self.user = self.user.lstrip()
            self.user = self.user.rstrip()

            ### work record
            self.work_record(s_user , '點擊人員管理 , 帳號 : ' + self.user)
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select a_user , a_pwd , a_lv , a_status from account where a_user='{0}'".format(self.user)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                self.ui.n_user_user.setText(str(val[0]))
                self.ui.n_user_pwd.setText(str(val[1]))
                self.ui.n_user_lv.setText(str(val[2]))
                self.ui.n_user_status.setText(str(val[3]))

            ### click normal combox lv
            self.ui.n_user_combox_lv.currentIndexChanged.connect(self.normal_user_combox_lv)
            ### click normal combox status
            self.ui.n_user_combox_status.currentIndexChanged.connect(self.normal_user_combox_status)
            ### click alter account submit
            self.ui.btn_n_user_alter_submit.clicked.connect(self.click_alter_account_submit)

            self.conn.commit()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > normal manager account list : ' + str(e))
        finally:
            self.conn.close()
    
    ###############################
    # click_alter_account_submit
    ###############################
    def click_alter_account_submit(self):
        try:
            ### disable / enable
            self.a_user = self.ui.n_user_user.text()
            self.a_pwd = self.ui.n_user_pwd.text()
            self.a_lv = self.ui.n_user_lv.text()
            self.a_status = self.ui.n_user_status.text()

            ### work record
            self.work_record(s_user , '修改人員管理 , 帳號 : ' + self.a_user + ' , 密碼 : ' + self.a_pwd + ' , 等級 : ' + self.a_lv + ' , 狀態 : ' + self.a_status)
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "update account set a_pwd='{0}' , a_lv='{1}' , a_status='{2}' where a_user='{3}'".format(self.a_pwd , self.a_lv , self.a_status , self.a_user)
            self.res = self.curr.execute(self.sql)
            self.conn.commit()

            if self.res:
                QMessageBox.information(self , 'Msg' , self.user + ' , 帳號修改完成。')

                ### clear and reload account list
                self.ui.n_user_user.clear()
                self.ui.n_user_pwd.clear()
                self.ui.n_user_lv.clear()
                self.ui.n_user_status.clear()
                
                self.normal_manager_account_list()
                self.normal_user_account_list()
                
        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > normal manager account list : ' + str(e))
        finally:
            pass

    ##############################
    # normal user combox status
    ##############################
    def normal_user_combox_status(self):
        self.text = self.ui.n_user_combox_status.currentText()
        
        if self.text == '使用中':
            self.ui.n_user_status.setText(str('run'))
        elif self.text == '停用中':
            self.ui.n_user_status.setText(str('stop'))

    ##########################
    # normal user combox lv
    ##########################
    def normal_user_combox_lv(self):
        self.text = self.ui.n_user_combox_lv.currentText()
        if self.text == '一般管理者':
            self.ui.n_user_lv.setText(str(2))
        elif self.text == '一般使用者':
            self.ui.n_user_lv.setText(str(3))


    ############################################
    # work record normal manager account list
    ############################################
    def work_record_normal_manager_account_list(self):
        try:
            #################
            # admin lv = 1
            #################
            if s_lv == '1':
                
                ### work record
                self.work_record(s_user , '日誌 - 載入一般管理者帳號清單')

                ### clear
                self.ui.n_m_work_record_account_list.clear()
            
                ### start time , stop time
                self.ui.n_m_work_record_start_time.setDateTime(QDateTime.currentDateTime())
                self.ui.n_m_work_record_end_time.setDateTime(QDateTime.currentDateTime())
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='2' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                        self.ui.n_m_work_record_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
                
                ### click normal account detail
                self.ui.n_m_work_record_account_list.itemClicked.connect(self.work_record_select_normal_user_account_detail)

                ### double click normal account detail
                self.ui.n_m_work_record_account_list.itemDoubleClicked.connect(self.work_record_query_by_normal_manager_user_account)

                self.conn.commit()
                self.conn.close()
            
            ########################
            # normal admin lv = 2
            ########################
            elif s_lv == '2':
                ### work record
                self.work_record(s_user , '日誌 - 載入一般管理者帳號清單 , ' + s_user + ' 無使用權限')
                ### clear
                self.ui.n_m_work_record_account_list.clear()
                ### show message
                self.ui.n_m_work_record_account_list.addItem('無使用權限')
                ### disable
                self.ui.n_m_work_record_start_time.setEnabled(False)
                self.ui.n_m_work_record_end_time.setEnabled(False)

            
            #######################
            # normal user lv = 3
            #######################
            elif s_lv == '3':
                ### work record
                self.work_record(s_user , '日誌 - 載入一般管理者帳號清單 , ' + s_user + ' 無使用權限')
                ### clear
                self.ui.n_m_work_record_account_list.clear()
                ### show message
                self.ui.n_m_work_record_account_list.addItem('無使用權限')
                ### disable
                self.ui.n_m_work_record_start_time.setEnabled(False)
                self.ui.n_m_work_record_end_time.setEnabled(False)
                self.ui.page_2_work_record.setEnabled(False)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work record normal manager account list : ' + str(e))
        finally:
            pass


    ################################
    # normal manager account list
    ################################
    def normal_manager_account_list(self):
        try:
            #################
            # admin lv = 1
            #################
            if s_lv == '1':
                
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般管理者帳號清單')

                ### clear
                self.ui.normal_manager_account_list.clear()
            
                ### disable / enable
                self.ui.n_user_combox_lv.setEnabled(False)
                self.ui.n_user_combox_status.setEnabled(False)
            
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select r_time , a_user , a_status from account where a_lv='2' order by r_time desc"
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                for val in self.res:
                        self.ui.normal_manager_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' (' + str(val[2]) + ')')
            
                ### click normal account detail
                self.ui.normal_manager_account_list.itemDoubleClicked.connect(self.select_normal_user_account_detail)

                self.conn.commit()
                self.conn.close()
            
            ########################
            # normal admin lv = 2
            ########################
            elif s_lv == '2':
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般管理者帳號清單 , 無使用權限')
                ### clear
                self.ui.normal_manager_account_list.clear()
                ### show message
                self.ui.normal_manager_account_list.addItem('無使用權限')
            
            #######################
            # normal user lv = 3
            #######################
            elif s_lv == '3':
                ### work record
                self.work_record(s_user , '人員管理 - 載入一般管理者帳號清單 , 無使用權限')
                ### clear
                self.ui.normal_manager_account_list.clear()
                ### show message
                self.ui.normal_manager_account_list.addItem('無使用權限')
                ### disable
                self.ui.n_user_user.setEnabled(False)
                self.ui.n_user_pwd.setEnabled(False)
                self.ui.n_user_lv.setEnabled(False)
                self.ui.n_user_combox_lv.setEnabled(False)
                self.ui.n_user_status.setEnabled(False)
                self.ui.n_user_combox_status.setEnabled(False)
                self.ui.page_1_account.setEnabled(False)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > normal manager account list : ' + str(e))
        finally:
            pass
            
    ################
    # work_record
    ################
    def work_record(self,user,msg):
        try:
            ### work msg
            self.w_r_user = user
            self.w_r_msg = msg

            #### record time
            self.w_r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.w_r_year = time.strftime("%Y" , time.localtime())
            self.w_r_month = time.strftime("%Y-%m" , time.localtime())
            self.w_r_day = time.strftime("%Y-%m-%d" , time.localtime())
            
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "insert into work_record(r_time , a_user , o_item , r_year , r_month , r_day) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(self.w_r_time , self.w_r_user , self.w_r_msg , self.w_r_year , self.w_r_month , self.w_r_day)
            self.curr.execute(self.sql)

            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work record : ' + str(e))
        finally:
            pass

    #################    
    # close window
    #################    
    def click_close(self):
        QApplication.closeAllWindows()
       
##########################################################################################################################
# login
##########################################################################################################################
#class main_login(QMainWindow):
class main_login(QFrame):
    
    #global s_user , s_lv , s_login_code

    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_animals_login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.login_init()

    ###############
    # init_login
    ###############
    def login_init(self):

        ### status bar
        #self.ui.statusbar.showMessage('Ready')

        ### btn register account submit
        self.ui.btn_register.clicked.connect(self.register_account_submit)

        ### btn login submit
        self.ui.btn_login.clicked.connect(self.login_submit)

        ### btn cancel
        self.ui.btn_cancel.clicked.connect(self.login_cancel)

    #################
    # login cancel
    #################
    def login_cancel(self):
        QApplication.closeAllWindows()

    #################
    # login_submit
    #################
    def login_submit(self):
        ### user and pwd
        self.user = self.ui.login_user.text()
        self.pwd  = self.ui.login_pwd.text()

        if len(self.user) == 0 or len(self.pwd) == 0:
            self.ui.login_msg.clear()
            self.ui.login_msg.setStyleSheet('color:red;')
            self.ui.login_msg.setText('登入 帳號 or 密碼不能空白 !')
            QMessageBox.information(self , 'Msg' , '登入 帳號 or 密碼不能空白 !')
        else:
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select a_user , a_lv from account where a_user='{0}' and a_pwd='{1}' and a_status='run'".format(self.user , self.pwd)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchone()
                
                if len(self.res[0]):
                    
                    ### global variable -> user , lv , login_code
                    global s_user , s_lv , s_login_code
                    s_user       = self.res[0]
                    s_lv         = self.res[1]
                    self.in_time = QDateTime.currentDateTime()
                    self.login_time = self.in_time.toString("yyyy-MM-dd HH:mm:ss")
                    s_login      = s_user +'/'+ self.login_time
                    s_login_code = hashlib.md5(s_login.encode())
                    s_login_code = s_login_code.hexdigest()
                    
                    ### login successful    
                    self.ui.login_msg.clear()
                    self.ui.login_msg.setStyleSheet('color:blue;')
                    self.ui.login_msg.setText('登入成功 , 馬上進入主頁')
                    QMessageBox.information(self , 'Msg' , '登入成功 , 馬上進入主頁')

                    ### in out record
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                    self.in_out_record_sql = "insert into in_out_record(login_time , a_user , r_year , r_month , r_day , login_code) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(self.r_time , s_user , self.r_year , self.r_month , self.r_day , s_login_code)
                    self.in_out_record_res = self.curr.execute(self.in_out_record_sql)

                    ### work record
                    self.w_r_user = s_user
                    self.w_r_msg  = '登入成功'
                    self.login_work_record_sql = "insert into work_record(r_time , a_user , o_item , r_year , r_month , r_day) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(self.r_time , self.w_r_user , self.w_r_msg , self.r_year , self.r_month , self.r_day)
                    self.login_work_record = self.curr.execute(self.login_work_record_sql)

                    if self.in_out_record_res and self.login_work_record:
                        try:
                            ### show main content
                            self.main = main_content()
                            self.main.show()

                            ### login successful then close login form
                            self.close()

                            self.conn.commit()
                            self.conn.close()
                        
                        except Exception as e:
                            QMessageBox.information(self , 'Msg' ,  '< Error > login successful then show main content : ' + str(e))
                    else:
                        QMessageBox.information(self , 'Msg' , '< Error > in out record failed. ')

            except Exception as e:
                self.ui.login_msg.clear()
                self.ui.login_msg.setStyleSheet('color:red;')
                self.ui.login_msg.setText('帳號  : ' + self.user + ' 沒有註冊過，無此帳號 !')
                QMessageBox.information(self , 'Msg' , '帳號  : ' + self.user + ' 沒有註冊過，無此帳號 !')

            finally:
                pass
                
    
    ############################
    # register_account_submit
    ############################
    def register_account_submit(self):
            ### user and pwd
            self.user = self.ui.login_user.text()
            self.pwd  = self.ui.login_pwd.text()

            if len(self.user) == 0 or len(self.pwd) == 0:
                self.ui.login_msg.clear()
                self.ui.login_msg.setStyleSheet('color:red;')
                self.ui.login_msg.setText('註冊 帳號 or 密碼 不能空白 !')
                QMessageBox.information(self , 'Msg' , '註冊 帳號 or 密碼 不能空白 !')

            else:
                try:
                    ### check account then add account
                    self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                    self.curr = self.conn.cursor()
                    self.sql = "select a_user from account where a_user='{0}' and a_status='run'".format(self.user , self.pwd)
                    self.curr.execute(self.sql)
                    self.res = self.curr.fetchone()

                    if len(self.res[0]) or self.res == 'admin':
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setStyleSheet('color:red')
                        self.ui.login_msg.setText('帳號 : ' + self.user + ' 已被使用 !')
                        QMessageBox.information(self , 'Msg' , '帳號 : ' + self.user + ' 已被使用 !')

                except Exception as e:

                    #### record time
                    self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day = time.strftime("%Y-%m-%d" , time.localtime())

                    #### check account then add account
                    self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                    self.curr = self.conn.cursor()
                    self.sql = "insert into account(r_time , r_year , r_month , r_day , a_user , a_pwd , a_lv , a_status) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(self.r_time , self.r_year , self.r_month , self.r_day , self.user , self.pwd , '3' , 'stop')
                    self.res = self.curr.execute(self.sql)

                    if self.res:
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setText('帳號 : ' + self.user + ' 新增成功.')
                        QMessageBox.information(self , 'Msg' , '帳號 : ' + self.user + ' 新增成功.')

                finally:
                    self.conn.commit()
                    self.conn.close()

#######################################################################################################################################
#
# start
#
#######################################################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = main_login()
    #login.setFixedSize(500,400)
    login.show()
    sys.exit(app.exec())
    

