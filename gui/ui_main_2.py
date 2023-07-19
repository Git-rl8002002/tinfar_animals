# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_animals_main(object):
    def setupUi(self, animals_main):
        if not animals_main.objectName():
            animals_main.setObjectName(u"animals_main")
        animals_main.resize(800, 600)
        self.tab_account = QWidget()
        self.tab_account.setObjectName(u"tab_account")
        self.gridLayout = QGridLayout(self.tab_account)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.tab_account)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.normal_manager_account_list = QListWidget(self.groupBox_5)
        self.normal_manager_account_list.setObjectName(u"normal_manager_account_list")

        self.verticalLayout_5.addWidget(self.normal_manager_account_list)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.normal_user_account_list = QListWidget(self.groupBox_3)
        self.normal_user_account_list.setObjectName(u"normal_user_account_list")

        self.verticalLayout.addWidget(self.normal_user_account_list)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_account)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.n_user_user = QLineEdit(self.groupBox_4)
        self.n_user_user.setObjectName(u"n_user_user")

        self.horizontalLayout.addWidget(self.n_user_user)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.n_user_pwd = QLineEdit(self.groupBox_4)
        self.n_user_pwd.setObjectName(u"n_user_pwd")

        self.horizontalLayout_2.addWidget(self.n_user_pwd)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.n_user_lv = QLineEdit(self.groupBox_4)
        self.n_user_lv.setObjectName(u"n_user_lv")

        self.horizontalLayout_3.addWidget(self.n_user_lv)

        self.n_user_combox_lv = QComboBox(self.groupBox_4)
        self.n_user_combox_lv.addItem("")
        self.n_user_combox_lv.addItem("")
        self.n_user_combox_lv.addItem("")
        self.n_user_combox_lv.setObjectName(u"n_user_combox_lv")

        self.horizontalLayout_3.addWidget(self.n_user_combox_lv)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.n_user_status = QLineEdit(self.groupBox_4)
        self.n_user_status.setObjectName(u"n_user_status")

        self.horizontalLayout_4.addWidget(self.n_user_status)

        self.n_user_combox_status = QComboBox(self.groupBox_4)
        self.n_user_combox_status.addItem("")
        self.n_user_combox_status.addItem("")
        self.n_user_combox_status.addItem("")
        self.n_user_combox_status.setObjectName(u"n_user_combox_status")

        self.horizontalLayout_4.addWidget(self.n_user_combox_status)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.btn_n_user_alter_submit = QPushButton(self.groupBox_4)
        self.btn_n_user_alter_submit.setObjectName(u"btn_n_user_alter_submit")

        self.verticalLayout_4.addWidget(self.btn_n_user_alter_submit)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        animals_main.addTab(self.tab_account, "")
        self.tab_realtime = QWidget()
        self.tab_realtime.setObjectName(u"tab_realtime")
        self.tab_realtime.setMaximumSize(QSize(794, 571))
        self.gridLayout_3 = QGridLayout(self.tab_realtime)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        animals_main.addTab(self.tab_realtime, "")
        self.tab_setup = QWidget()
        self.tab_setup.setObjectName(u"tab_setup")
        animals_main.addTab(self.tab_setup, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName(u"tab_history")
        animals_main.addTab(self.tab_history, "")
        self.tab_work_record = QWidget()
        self.tab_work_record.setObjectName(u"tab_work_record")
        animals_main.addTab(self.tab_work_record, "")

        self.retranslateUi(animals_main)

        animals_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(animals_main)
    # setupUi

    def retranslateUi(self, animals_main):
        animals_main.setWindowTitle(QCoreApplication.translate("animals_main", u"TabWidget", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("animals_main", u"\u5e33\u865f\u6e05\u55ae\u5217\u8868", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("animals_main", u"\u4e00\u822c\u7ba1\u7406\u8005", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("animals_main", u"\u4e00\u822c\u4f7f\u7528\u8005", None))
        self.groupBox.setTitle(QCoreApplication.translate("animals_main", u"\u5e33\u865f\u8a73\u7d30\u8cc7\u6599", None))
        self.groupBox_4.setTitle("")
        self.label_5.setText(QCoreApplication.translate("animals_main", u"\u5e33\u865f", None))
        self.label_6.setText(QCoreApplication.translate("animals_main", u"\u5bc6\u78bc", None))
        self.label.setText(QCoreApplication.translate("animals_main", u"\u7b49\u7d1a\u5206\u6210 , \u4e00\u822c\u7ba1\u7406\u8005 level 2 , \u4e00\u822c\u4f7f\u7528\u8005 leve 3", None))
        self.label_7.setText(QCoreApplication.translate("animals_main", u"\u7b49\u7d1a", None))
        self.n_user_combox_lv.setItemText(0, "")
        self.n_user_combox_lv.setItemText(1, QCoreApplication.translate("animals_main", u"\u4e00\u822c\u7ba1\u7406\u8005", None))
        self.n_user_combox_lv.setItemText(2, QCoreApplication.translate("animals_main", u"\u4e00\u822c\u4f7f\u7528\u8005", None))

        self.label_2.setText(QCoreApplication.translate("animals_main", u"\u72c0\u614b\u5206\u6210 , \u958b run ,  \u95dc stop \u5169\u7a2e", None))
        self.label_8.setText(QCoreApplication.translate("animals_main", u"\u72c0\u614b", None))
        self.n_user_combox_status.setItemText(0, "")
        self.n_user_combox_status.setItemText(1, QCoreApplication.translate("animals_main", u"\u4f7f\u7528\u4e2d", None))
        self.n_user_combox_status.setItemText(2, QCoreApplication.translate("animals_main", u"\u505c\u7528\u4e2d", None))

        self.btn_n_user_alter_submit.setText(QCoreApplication.translate("animals_main", u"\u4fee\u6539", None))
        animals_main.setTabText(animals_main.indexOf(self.tab_account), QCoreApplication.translate("animals_main", u"\u4eba\u54e1\u7ba1\u7406", None))
        animals_main.setTabText(animals_main.indexOf(self.tab_realtime), QCoreApplication.translate("animals_main", u"\u5373\u6642\u5e36\u6e2c\u53c3\u6578\u986f\u793a", None))
        animals_main.setTabText(animals_main.indexOf(self.tab_setup), QCoreApplication.translate("animals_main", u"\u8a2d\u5b9a", None))
        animals_main.setTabText(animals_main.indexOf(self.tab_history), QCoreApplication.translate("animals_main", u"\u6b77\u53f2\u7d00\u9304", None))
        animals_main.setTabText(animals_main.indexOf(self.tab_work_record), QCoreApplication.translate("animals_main", u"\u5de5\u4f5c\u65e5\u8a8c", None))
    # retranslateUi

