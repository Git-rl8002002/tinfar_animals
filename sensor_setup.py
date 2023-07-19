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


from control.dao import * 
from gui.ui_login import *
from gui.ui_main_3 import *

##########################################################################################################################
# main
##########################################################################################################################
class area_sensor_setup(QMainWindow):

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
                if str(val[1]) is not None:
                    self.ui.a_s_1_pr_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_pr_top_manual.setChecked(True)
                self.ui.a_s_1_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_pr_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_pr_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_h2s_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_h2s_top_manual.setChecked(True)
                self.ui.a_s_1_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_h2s_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_h2s_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_nh3_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_nh3_top_manual.setChecked(True)
                self.ui.a_s_1_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_nh3_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_nh3_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_rh_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_rh_top_manual.setChecked(True)
                self.ui.a_s_1_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_rh_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_rh_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_temp_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_temp_top_manual.setChecked(True)
                self.ui.a_s_1_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_temp_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_temp_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_temp_bottom_manual.setChecked(True)
                self.ui.a_s_1_temp_bottom_device.setText(str(val[3]))
            
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_pr_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_pr_top_manual.setChecked(True)
                self.ui.a_s_1_pr_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='pr' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_pr_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_pr_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_h2s_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_h2s_top_manual.setChecked(True)
                self.ui.a_s_1_h2s_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='h2s' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_h2s_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_h2s_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_nh3_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_nh3_top_manual.setChecked(True)
                self.ui.a_s_1_nh3_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='nh3' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_nh3_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_nh3_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_rh_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_rh_top_manual.setChecked(True)
                self.ui.a_s_1_rh_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='rh' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_rh_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_rh_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
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
                if str(val[1]) is not None:
                    self.ui.a_s_1_temp_top_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_temp_top_manual.setChecked(True)
                self.ui.a_s_1_temp_top_device.setText(str(val[3]))

            self.sql2 = "select s_alarm_bottom , s_bottom_auto_run , s_bottom_manual_run , s_alarm_bottom_device from setup_record where s_area='a' and s_id='1' and s_item='temp' limit 1,1"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            for val in self.res2:
                ### top value
                self.ui.a_s_1_temp_bottom.setText(str(val[0]))
                if str(val[1]) is not None:
                    self.ui.a_s_1_temp_bottom_auto.setChecked(True)
                elif str(val[2]) is not None:
                    self.ui.a_s_1_temp_bottom_manual.setChecked(True)
                self.ui.a_s_1_temp_bottom_device.setText(str(val[3]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > a area sensor 1 temp : ' + str(e))
        finally:
            pass    


def main():
    app = QApplication(sys.argv)
    main = area_sensor_setup()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    