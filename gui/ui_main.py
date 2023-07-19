# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1024, 768))
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tab_account = QWidget()
        self.tab_account.setObjectName(u"tab_account")
        self.layoutWidget = QWidget(self.tab_account)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 40, 371, 141))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.a_r_time = QLabel(self.layoutWidget)
        self.a_r_time.setObjectName(u"a_r_time")
        font1 = QFont()
        font1.setPointSize(18)
        self.a_r_time.setFont(font1)

        self.horizontalLayout_5.addWidget(self.a_r_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.a_user = QLabel(self.layoutWidget)
        self.a_user.setObjectName(u"a_user")
        self.a_user.setFont(font1)

        self.horizontalLayout_2.addWidget(self.a_user)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.a_pwd = QLabel(self.layoutWidget)
        self.a_pwd.setObjectName(u"a_pwd")
        self.a_pwd.setFont(font1)

        self.horizontalLayout_3.addWidget(self.a_pwd)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.a_status = QLabel(self.layoutWidget)
        self.a_status.setObjectName(u"a_status")
        self.a_status.setFont(font1)

        self.horizontalLayout_4.addWidget(self.a_status)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.groupBox_15 = QGroupBox(self.tab_account)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 10, 371, 491))
        self.groupBox_15.setFont(font1)
        self.main_account_list = QListWidget(self.groupBox_15)
        self.main_account_list.setObjectName(u"main_account_list")
        self.main_account_list.setGeometry(QRect(10, 40, 351, 441))
        self.main_account_list.setFont(font)
        self.tabWidget.addTab(self.tab_account, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 781, 221))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.groupBox.setFont(font2)
        self.realtime_monitor_i6_list = QListWidget(self.groupBox)
        self.realtime_monitor_i6_list.setObjectName(u"realtime_monitor_i6_list")
        self.realtime_monitor_i6_list.setGeometry(QRect(10, 30, 761, 181))
        self.realtime_monitor_i6_list.setFont(font)
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 270, 781, 241))
        self.groupBox_2.setFont(font2)
        self.realtime_monitor_i6_list_2 = QListWidget(self.groupBox_2)
        self.realtime_monitor_i6_list_2.setObjectName(u"realtime_monitor_i6_list_2")
        self.realtime_monitor_i6_list_2.setGeometry(QRect(10, 30, 761, 201))
        self.realtime_monitor_i6_list_2.setFont(font)
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(800, 60, 201, 181))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(False)
        self.groupBox_4.setFont(font3)
        self.layoutWidget1 = QWidget(self.groupBox_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 181, 141))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.monitor_now_time = QLabel(self.layoutWidget1)
        self.monitor_now_time.setObjectName(u"monitor_now_time")
        self.monitor_now_time.setFont(font)

        self.verticalLayout_2.addWidget(self.monitor_now_time)

        self.monitor_item1 = QLabel(self.layoutWidget1)
        self.monitor_item1.setObjectName(u"monitor_item1")
        self.monitor_item1.setFont(font)

        self.verticalLayout_2.addWidget(self.monitor_item1)

        self.monitor_item2 = QLabel(self.layoutWidget1)
        self.monitor_item2.setObjectName(u"monitor_item2")
        self.monitor_item2.setFont(font)

        self.verticalLayout_2.addWidget(self.monitor_item2)

        self.monitor_item3 = QLabel(self.layoutWidget1)
        self.monitor_item3.setObjectName(u"monitor_item3")
        self.monitor_item3.setFont(font)

        self.verticalLayout_2.addWidget(self.monitor_item3)

        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(800, 290, 201, 211))
        self.groupBox_5.setFont(font1)
        self.layoutWidget2 = QWidget(self.groupBox_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 181, 171))
        font4 = QFont()
        font4.setPointSize(15)
        self.layoutWidget2.setFont(font4)
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.monitor_now_time_2 = QLabel(self.layoutWidget2)
        self.monitor_now_time_2.setObjectName(u"monitor_now_time_2")
        self.monitor_now_time_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_now_time_2)

        self.monitor_item1_2 = QLabel(self.layoutWidget2)
        self.monitor_item1_2.setObjectName(u"monitor_item1_2")
        self.monitor_item1_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_item1_2)

        self.monitor_item2_2 = QLabel(self.layoutWidget2)
        self.monitor_item2_2.setObjectName(u"monitor_item2_2")
        self.monitor_item2_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_item2_2)

        self.monitor_item3_2 = QLabel(self.layoutWidget2)
        self.monitor_item3_2.setObjectName(u"monitor_item3_2")
        self.monitor_item3_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_item3_2)

        self.monitor_item4_2 = QLabel(self.layoutWidget2)
        self.monitor_item4_2.setObjectName(u"monitor_item4_2")
        self.monitor_item4_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_item4_2)

        self.monitor_item5_2 = QLabel(self.layoutWidget2)
        self.monitor_item5_2.setObjectName(u"monitor_item5_2")
        self.monitor_item5_2.setFont(font)

        self.verticalLayout_3.addWidget(self.monitor_item5_2)

        self.layoutWidget3 = QWidget(self.tab_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(670, 10, 338, 38))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_start_monitor_i6 = QCommandLinkButton(self.layoutWidget3)
        self.btn_start_monitor_i6.setObjectName(u"btn_start_monitor_i6")
        self.btn_start_monitor_i6.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_start_monitor_i6)

        self.btn_stop_monitor_i6 = QCommandLinkButton(self.layoutWidget3)
        self.btn_stop_monitor_i6.setObjectName(u"btn_stop_monitor_i6")
        self.btn_stop_monitor_i6.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_stop_monitor_i6)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 30, 761, 641))
        self.groupBox_3.setFont(font4)
        self.realtime_sn3401p_list_1 = QListWidget(self.groupBox_3)
        self.realtime_sn3401p_list_1.setObjectName(u"realtime_sn3401p_list_1")
        self.realtime_sn3401p_list_1.setGeometry(QRect(10, 69, 741, 260))
        self.realtime_sn3401p_list_2 = QListWidget(self.groupBox_3)
        self.realtime_sn3401p_list_2.setObjectName(u"realtime_sn3401p_list_2")
        self.realtime_sn3401p_list_2.setGeometry(QRect(10, 370, 741, 260))
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 91, 16))
        self.label.setFont(font4)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 340, 91, 16))
        self.label_2.setFont(font4)
        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(780, 50, 221, 311))
        self.groupBox_6.setFont(font4)
        self.layoutWidget4 = QWidget(self.groupBox_6)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 30, 201, 271))
        self.verticalLayout = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sn3401p_s_1_r_time = QLabel(self.layoutWidget4)
        self.sn3401p_s_1_r_time.setObjectName(u"sn3401p_s_1_r_time")

        self.verticalLayout.addWidget(self.sn3401p_s_1_r_time)

        self.sn3401p_s_1_val = QLabel(self.layoutWidget4)
        self.sn3401p_s_1_val.setObjectName(u"sn3401p_s_1_val")

        self.verticalLayout.addWidget(self.sn3401p_s_1_val)

        self.sn3401p_s_2_val = QLabel(self.layoutWidget4)
        self.sn3401p_s_2_val.setObjectName(u"sn3401p_s_2_val")

        self.verticalLayout.addWidget(self.sn3401p_s_2_val)

        self.sn3401p_s_3_val = QLabel(self.layoutWidget4)
        self.sn3401p_s_3_val.setObjectName(u"sn3401p_s_3_val")

        self.verticalLayout.addWidget(self.sn3401p_s_3_val)

        self.sn3401p_s_4_val = QLabel(self.layoutWidget4)
        self.sn3401p_s_4_val.setObjectName(u"sn3401p_s_4_val")

        self.verticalLayout.addWidget(self.sn3401p_s_4_val)

        self.sn3401p_s_5_val = QLabel(self.layoutWidget4)
        self.sn3401p_s_5_val.setObjectName(u"sn3401p_s_5_val")

        self.verticalLayout.addWidget(self.sn3401p_s_5_val)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_s_1_thread_start = QCommandLinkButton(self.layoutWidget4)
        self.btn_s_1_thread_start.setObjectName(u"btn_s_1_thread_start")
        self.btn_s_1_thread_start.setFont(font)

        self.horizontalLayout_10.addWidget(self.btn_s_1_thread_start)

        self.btn_s_1_thread_stop = QCommandLinkButton(self.layoutWidget4)
        self.btn_s_1_thread_stop.setObjectName(u"btn_s_1_thread_stop")
        self.btn_s_1_thread_stop.setFont(font)

        self.horizontalLayout_10.addWidget(self.btn_s_1_thread_stop)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_s_1_start = QCommandLinkButton(self.layoutWidget4)
        self.btn_s_1_start.setObjectName(u"btn_s_1_start")
        self.btn_s_1_start.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn_s_1_start)

        self.btn_s_1_stop = QCommandLinkButton(self.layoutWidget4)
        self.btn_s_1_stop.setObjectName(u"btn_s_1_stop")
        self.btn_s_1_stop.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn_s_1_stop)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(780, 390, 221, 281))
        self.groupBox_7.setFont(font4)
        self.layoutWidget5 = QWidget(self.groupBox_7)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 30, 201, 241))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sn3401p_s2_r_time = QLabel(self.layoutWidget5)
        self.sn3401p_s2_r_time.setObjectName(u"sn3401p_s2_r_time")

        self.verticalLayout_4.addWidget(self.sn3401p_s2_r_time)

        self.sn3401p_s2_1_val = QLabel(self.layoutWidget5)
        self.sn3401p_s2_1_val.setObjectName(u"sn3401p_s2_1_val")

        self.verticalLayout_4.addWidget(self.sn3401p_s2_1_val)

        self.sn3401p_s2_2_val = QLabel(self.layoutWidget5)
        self.sn3401p_s2_2_val.setObjectName(u"sn3401p_s2_2_val")

        self.verticalLayout_4.addWidget(self.sn3401p_s2_2_val)

        self.sn3401p_s2_3_val = QLabel(self.layoutWidget5)
        self.sn3401p_s2_3_val.setObjectName(u"sn3401p_s2_3_val")

        self.verticalLayout_4.addWidget(self.sn3401p_s2_3_val)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_s_2_thread_start = QCommandLinkButton(self.layoutWidget5)
        self.btn_s_2_thread_start.setObjectName(u"btn_s_2_thread_start")
        self.btn_s_2_thread_start.setFont(font4)

        self.horizontalLayout_11.addWidget(self.btn_s_2_thread_start)

        self.btn_s_2_thread_stop = QCommandLinkButton(self.layoutWidget5)
        self.btn_s_2_thread_stop.setObjectName(u"btn_s_2_thread_stop")
        self.btn_s_2_thread_stop.setFont(font4)

        self.horizontalLayout_11.addWidget(self.btn_s_2_thread_stop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_s_2_start = QCommandLinkButton(self.layoutWidget5)
        self.btn_s_2_start.setObjectName(u"btn_s_2_start")
        self.btn_s_2_start.setFont(font4)

        self.horizontalLayout_7.addWidget(self.btn_s_2_start)

        self.btn_s_2_stop = QCommandLinkButton(self.layoutWidget5)
        self.btn_s_2_stop.setObjectName(u"btn_s_2_stop")
        self.btn_s_2_stop.setFont(font4)

        self.horizontalLayout_7.addWidget(self.btn_s_2_stop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 20, 381, 211))
        self.groupBox_8.setFont(font4)
        self.sn3401p_total_list = QListWidget(self.groupBox_8)
        self.sn3401p_total_list.setObjectName(u"sn3401p_total_list")
        self.sn3401p_total_list.setGeometry(QRect(10, 40, 361, 161))
        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(800, 40, 211, 131))
        self.groupBox_9.setFont(font4)
        self.sn3401p_total_update = QLabel(self.groupBox_9)
        self.sn3401p_total_update.setObjectName(u"sn3401p_total_update")
        self.sn3401p_total_update.setGeometry(QRect(10, 40, 191, 21))
        self.sn3401p_total_update.setFont(font4)
        self.layoutWidget6 = QWidget(self.groupBox_9)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 80, 181, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_sn3401p_start_total = QCommandLinkButton(self.layoutWidget6)
        self.btn_sn3401p_start_total.setObjectName(u"btn_sn3401p_start_total")
        self.btn_sn3401p_start_total.setFont(font4)

        self.horizontalLayout_8.addWidget(self.btn_sn3401p_start_total)

        self.btn_sn3401p_stop_total = QCommandLinkButton(self.layoutWidget6)
        self.btn_sn3401p_stop_total.setObjectName(u"btn_sn3401p_stop_total")
        self.btn_sn3401p_stop_total.setFont(font4)

        self.horizontalLayout_8.addWidget(self.btn_sn3401p_stop_total)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 240, 381, 211))
        self.groupBox_10.setFont(font4)
        self.sn3401p_total_list_by_day = QListWidget(self.groupBox_10)
        self.sn3401p_total_list_by_day.setObjectName(u"sn3401p_total_list_by_day")
        self.sn3401p_total_list_by_day.setGeometry(QRect(10, 40, 361, 161))
        self.groupBox_11 = QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(400, 20, 381, 211))
        self.groupBox_11.setFont(font4)
        self.sn3401p_total_list_by_failed = QListWidget(self.groupBox_11)
        self.sn3401p_total_list_by_failed.setObjectName(u"sn3401p_total_list_by_failed")
        self.sn3401p_total_list_by_failed.setGeometry(QRect(10, 40, 361, 161))
        self.groupBox_12 = QGroupBox(self.tab_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(800, 250, 211, 201))
        self.groupBox_12.setFont(font4)
        self.layoutWidget7 = QWidget(self.groupBox_12)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(10, 40, 191, 61))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sensor_by_day_final_record = QLabel(self.layoutWidget7)
        self.sensor_by_day_final_record.setObjectName(u"sensor_by_day_final_record")
        self.sensor_by_day_final_record.setFont(font4)

        self.verticalLayout_6.addWidget(self.sensor_by_day_final_record)

        self.groupBox_13 = QGroupBox(self.tab_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(400, 240, 381, 211))
        self.groupBox_13.setFont(font4)
        self.sn3401p_total_list_by_day_2 = QListWidget(self.groupBox_13)
        self.sn3401p_total_list_by_day_2.setObjectName(u"sn3401p_total_list_by_day_2")
        self.sn3401p_total_list_by_day_2.setGeometry(QRect(10, 40, 361, 161))
        self.groupBox_14 = QGroupBox(self.tab_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(10, 460, 381, 231))
        self.groupBox_14.setFont(font4)
        self.realtime_cw9_1 = QListWidget(self.groupBox_14)
        self.realtime_cw9_1.setObjectName(u"realtime_cw9_1")
        self.realtime_cw9_1.setGeometry(QRect(10, 30, 361, 191))
        self.groupBox_16 = QGroupBox(self.tab_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(400, 460, 381, 231))
        self.groupBox_16.setFont(font4)
        self.realtime_cw9_2 = QListWidget(self.groupBox_16)
        self.realtime_cw9_2.setObjectName(u"realtime_cw9_2")
        self.realtime_cw9_2.setGeometry(QRect(10, 30, 361, 191))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Account</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.a_r_time.setText("")
        self.a_user.setText("")
        self.a_pwd.setText("")
        self.a_status.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Account list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account), QCoreApplication.translate("MainWindow", u"Account", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CB", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"I6", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"CB", None))
        self.monitor_now_time.setText("")
        self.monitor_item1.setText("")
        self.monitor_item2.setText("")
        self.monitor_item3.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"I6", None))
        self.monitor_now_time_2.setText("")
        self.monitor_item1_2.setText("")
        self.monitor_item2_2.setText("")
        self.monitor_item3_2.setText("")
        self.monitor_item4_2.setText("")
        self.monitor_item5_2.setText("")
        self.btn_start_monitor_i6.setText(QCoreApplication.translate("MainWindow", u"start monitor", None))
        self.btn_stop_monitor_i6.setText(QCoreApplication.translate("MainWindow", u"stop monitor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Realtime monitor CB,I6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CW9 - 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CW9 - 2", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"CW9 - 1 update", None))
        self.sn3401p_s_1_r_time.setText("")
        self.sn3401p_s_1_val.setText("")
        self.sn3401p_s_2_val.setText("")
        self.sn3401p_s_3_val.setText("")
        self.sn3401p_s_4_val.setText("")
        self.sn3401p_s_5_val.setText("")
        self.btn_s_1_thread_start.setText(QCoreApplication.translate("MainWindow", u"T Start", None))
        self.btn_s_1_thread_stop.setText(QCoreApplication.translate("MainWindow", u"T Stop", None))
        self.btn_s_1_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_s_1_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"CW9 - 2 update", None))
        self.sn3401p_s2_r_time.setText("")
        self.sn3401p_s2_1_val.setText("")
        self.sn3401p_s2_2_val.setText("")
        self.sn3401p_s2_3_val.setText("")
        self.btn_s_2_thread_start.setText(QCoreApplication.translate("MainWindow", u"T Start", None))
        self.btn_s_2_thread_stop.setText(QCoreApplication.translate("MainWindow", u"T Stop", None))
        self.btn_s_2_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_s_2_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Realtime monitor SN3401P", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P sensor total rows", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"update", None))
        self.sn3401p_total_update.setText("")
        self.btn_sn3401p_start_total.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_sn3401p_stop_total.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P sensor total and final by day ", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P sensor by failed", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"final", None))
        self.sensor_by_day_final_record.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P sensor final record by day", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P CW9 - 1", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"SN3401P CW9 - 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Total SN3401P", None))
    # retranslateUi

