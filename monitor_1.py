#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221129
# Update   : 20221208
# Function : new taipei animals department


import time , pymysql , minimalmodbus , logging
from sys import argv
from pyModbusTCP.client import *
from control.dao import * 


###############################################################################################################################################
#
# monitor
#
###############################################################################################################################################
class monitor():
    
    ### log
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d H%:%M:%S")

    #########
    # init
    #########
    def __init__(self):
        ### by modbus TCP
        self.get_cw9_m_tcp() 
        
        ### by modbus RTU
        #self.get_cw9_m_rtu() 

    ################################
    # read CW9 register value
    ################################
    def get_cw9_m_tcp(self):
        
        try:
            #while True:

                #########################
                # CW9 - 1 by modbusTCP
                #########################
                self.cb = ModbusClient(host=i6_tcp_connect['ip'],port=i6_tcp_connect['port'],unit_id=i6_tcp_connect['id'],auto_open=True,auto_close=True,debug=False)

                ### record time
                self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                self.r_year  = time.strftime("%Y" , time.localtime())
                self.r_month = time.strftime("%Y-%m" , time.localtime())
                self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                self.n_time  = time.strftime("%H:%M:%S" , time.localtime())
                
                ### 溫度
                self.cb_val1 = self.cb.read_input_registers(int(cb_tcp_sensor['temp'],16),1)
                ### 濕度
                self.cb_val2 = self.cb.read_input_registers(int(cb_tcp_sensor['rh'],16),1)
                ### co2
                self.cb_val3 = self.cb.read_input_registers(int(cb_tcp_sensor['co2'],16),1)
                ### PM2.5
                self.cb_val4 = self.cb.read_input_registers(int(cb_tcp_sensor['pm2.5'],16),1)
                ### HCHO
                self.cb_val5 = self.cb.read_input_registers(int(cb_tcp_sensor['hcho'],16),1)
                
                print(self.r_time  + ' ( CW9 - 1 ) , TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％ , CO2 : ' + str(self.cb_val3[0]/10) + ' ppm' + ' , PM2.5 : ' + str(self.cb_val4[0]/10) + ' °C , HCHO : ' + str(self.cb_val5[0]/10) + ' ％')
                
                ### write to file & write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , SN3401P sensor 1 - TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％ ,  CO2 : ' + str(self.cb_val3[0]/10) + ' ppm , PM2.5 : ' + str(self.cb_val4[0]/10) + ' ug/m3 , HCHO : ' + str(self.cb_val5[0]/10) + ' ppm \n'
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'A' , '1', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')    

                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'A' , '2', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok') 
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'A' , '3', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'A' , '4', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok') 
                
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'B' , '5', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')     
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'B' , '6', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'B' , '7', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')         

                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'C' , '8', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')      
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'C' , '9', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'C' , '10', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'C' , '11', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'C' , '12', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')        

                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'D' , '13', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'D' , '14', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'D' , '15', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'D' , '16', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       

                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'E' , '17', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'E' , '18', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusTCP' , 'E' , '19', 'TEMP , RH , NH3 , H2S , PR' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 , 'ok')       

                

                #########################
                # CW9 - 2 by modbusTCP
                #########################
                '''
                self.cb = ModbusClient(host=i6_tcp_connect2['ip'],port=i6_tcp_connect2['port'],unit_id=i6_tcp_connect2['id'],auto_open=True,auto_close=True,debug=False)
                
                ### record time
                self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
                self.r_year  = time.strftime("%Y" , time.localtime())
                self.r_month = time.strftime("%Y-%m" , time.localtime())
                self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                self.n_time  = time.strftime("%H:%M:%S" , time.localtime())

                ### 溫度
                self.cb_val1 = self.cb.read_input_registers(int(cb_tcp_sensor['temp'],16),1)
                ### 濕度
                self.cb_val2 = self.cb.read_input_registers(int(cb_tcp_sensor['rh'],16),1)

                print(self.r_time  + ' ( CW9 - 2 ) , TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％ ')

                ### write to file & write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , SN3401P sensor 2 - TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％\n' 
                self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusRTU' , 'A' , '1', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , 0 , 0 , 0 , 'ok')    
                '''
                print('\n')
                
                #time.slieep(5)

        except Exception as e:
            print('< Error > CW9 : ' + str(e))

    #######################
    # get cw9 mosbus RTU
    #######################
    def get_cw9_m_rtu(self):
            
            try:
                #while True:
                    
                    #########
                    #
                    # ID 1
                    #
                    #########
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                    self.n_time  = time.strftime("%H:%M:%S" , time.localtime())
                    ### port 
                    self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['mac_port2'] , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)
                    #self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['linux_port'] , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)
                
                    self.cw9.serial.baudrate = i6_rtu_para['br']
                    self.cw9.serial.timeout = 1
                    self.cw9.clear_buffers_before_each_transaction = True
                    self.cw9.close_port_after_each_call = True
                    self.cw9.debug = False
                
                    ###  show CW9 read register val
                    self.cw9_val1 = self.cw9.read_register(int(i6_rtu_sensor['temp'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val2 = self.cw9.read_register(int(i6_rtu_sensor['rh'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val3 = self.cw9.read_register(int(i6_rtu_sensor['co2'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val4 = self.cw9.read_register(int(i6_rtu_sensor['pm2.5'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val5 = self.cw9.read_register(int(i6_rtu_sensor['hcho'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val6 = self.cw9.read_register(int(i6_rtu_sensor['tvoc'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val7 = self.cw9.read_register(int(i6_rtu_sensor['o3'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val8 = self.cw9.read_register(int(i6_rtu_sensor['pm10'],16),functioncode=int(i6_rtu_para['fc']))
                    
                    print('ID : 1')
                    print(self.r_time + ' , modbudRTU , CW9-TEMP  : ' + str(self.cw9_val1/10) + ' °C')
                    print(self.r_time + ' , modbudRTU , CW9-RH    : ' + str(self.cw9_val2/10) + ' %')
                    print(self.r_time + ' , modbudRTU , CW9-CO2   : ' + str(self.cw9_val3/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-PM2.5 : ' + str(self.cw9_val4/10) + ' ug/m3')
                    print(self.r_time + ' , modbudRTU , CW9-HCHO  : ' + str(self.cw9_val5/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-TVOC  : ' + str(self.cw9_val6/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-O3    : ' + str(self.cw9_val7/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-PM10  : ' + str(self.cw9_val8/10) + ' ug/m3')

                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , modbusRTU , A , ID : 1 , TEMP : ' + str(self.cw9_val1/10) + ' °C , RH : ' + str(self.cw9_val2/10) + ' ％ , CO2 : ' +  str(self.cw9_val3/10) + ' ppm , PM2.5 : ' + str(self.cw9_val4/10) + ' ppm , HCHO : ' + str(self.cw9_val5/10) + ' ppm \n'
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'A' , '1', 'TEMP , RH , CO2 , PM2.5 , HCHO' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    
                    print('\n')

                    time.sleep(1)
                    
                    #########
                    #
                    # ID 2
                    #
                    #########
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                    self.n_time  = time.strftime("%H:%M:%S" , time.localtime())
                    ### port 
                    self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['mac_port2'] , slaveaddress=2 , mode=minimalmodbus.MODE_RTU)
                    #self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['linux_port'] , slaveaddress=2 , mode=minimalmodbus.MODE_RTU)
                    
                    self.cw9.serial.baudrate = i6_rtu_para['br']
                    self.cw9.serial.timeout = 1
                    self.cw9.clear_buffers_before_each_transaction = True
                    self.cw9.close_port_after_each_call = True
                    self.cw9.debug = False

                    ###  show CW9 read register val
                    self.cw9_val1 = self.cw9.read_register(int(i6_rtu_sensor['temp'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val2 = self.cw9.read_register(int(i6_rtu_sensor['rh'],16),functioncode=int(i6_rtu_para['fc']))
                    
                    print('ID : 2')
                    print(self.r_time + ' , modbudRTU , CW9-TEMP : ' + str(self.cw9_val1/10) + ' °C')
                    print(self.r_time + ' , modbudRTU , CW9-RH   : ' + str(self.cw9_val2/10) + ' %')

                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , modbusRTU , A , ID : 2 , TEMP : ' + str(self.cw9_val1/10) + ' °C , RH : ' + str(self.cw9_val2/10) + ' ％ \n'
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'A' , '2', 'TEMP , RH' , self.cw9_val1/10 , self.cw9_val2/10 , 0 , 0 , 0 , 'ok')    
                    
                    print('\n')
                    
                    time.sleep(1)

                    #########
                    #
                    # ID 3
                    #
                    #########
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                    self.n_time  = time.strftime("%H:%M:%S" , time.localtime())
                    ### port 
                    self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['mac_port2'] , slaveaddress=3 , mode=minimalmodbus.MODE_RTU)
                    #self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['linux_port'] , slaveaddress=3 , mode=minimalmodbus.MODE_RTU)
                    
                    self.cw9.serial.baudrate = i6_rtu_para['br']
                    self.cw9.serial.timeout = 1
                    self.cw9.clear_buffers_before_each_transaction = True
                    self.cw9.close_port_after_each_call = True
                    self.cw9.debug = False

                    ###  show CW9 read register val
                    self.cw9_val1 = self.cw9.read_register(int(i6_rtu_sensor['temp'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val2 = self.cw9.read_register(int(i6_rtu_sensor['rh'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val3 = self.cw9.read_register(int(i6_rtu_sensor['nh3'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val4 = self.cw9.read_register(int(i6_rtu_sensor['h2s'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val5 = self.cw9.read_register(int(i6_rtu_sensor['pr'],16),functioncode=int(i6_rtu_para['fc']))
                    
                    print('ID : 3')
                    print(self.r_time + ' , modbudRTU , CW9-TEMP : ' + str(self.cw9_val1/10) + ' °C')
                    print(self.r_time + ' , modbudRTU , CW9-RH   : ' + str(self.cw9_val2/10) + ' %')
                    print(self.r_time + ' , modbudRTU , CW9-NH3  : ' + str(self.cw9_val3/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-H2S  :  ' + str(self.cw9_val4/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-PR   : ' + str(self.cw9_val5/10) + ' hPa')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , modbusRTU , A , ID : 3 , TEMP : ' + str(self.cw9_val1/10) + ' °C , RH : ' + str(self.cw9_val2/10) + ' ％ , NH3 : ' +  str(self.cw9_val3/10) + ' ppm , H2S : ' + str(self.cw9_val4/10) + ' ppm , PR : ' + str(self.cw9_val5/10) + ' hPa \n'
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time  , 'modbusRTU' , 'A' , '3', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    

                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'A' , '4', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'B' , '5', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'B' , '6', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'B' , '7', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'C' , '8', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'C' , '9', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'C' , '10', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'C' , '11', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'C' , '12', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'D' , '13', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'D' , '14', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'D' , '15', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'D' , '16', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'E' , '17', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'E' , '18', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'E' , '19', 'TEMP , RH , NH3 , H2S , PR' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    
                    print('\n')
                    
                    time.sleep(1)

            except IOError as e:
                print('< IOError > : ' + str(e))
            finally:
                pass
    
    ###################
    # db insert file
    ###################
    def db_insert_file(self , add_content , r_time , r_year , r_month , r_day , r_daytime , protocol , area , kind , content , val1 , val2 , val3 , val4 , val5 , status):
        try:
            ### write to file
            #self.add = open('/var/www/html/plc_web/control/modbusTCP_record.txt','a')
            #self.add.write(add_content)
            #self.add.close()

            ### write to MySQL
            self.r_time    = r_time
            self.r_year    = r_year
            self.r_month   = r_month
            self.r_day     = r_day
            self.r_daytime = r_daytime
            self.area      = area 
            self.kind      = kind 
            self.content   = content 
            self.protocol  = protocol
            self.val1      = val1
            self.val2      = val2
            self.val3      = val3
            self.val4      = val4
            self.val5      = val5
            self.status    = status

            ### create table by month
            self.data = self.r_month.split('-')
            self.b_month = self.data[0]+'_'+self.data[1]

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            try:
                self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,r_daytime varchar(100) null,s_area varchar(200) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(self.b_month)
                self.curr2.execute(self.build_sql)
                self.conn2.commit()
                self.conn2.close()
            except Exception as e:
                self.sql2 = "insert into {0}(r_time,r_year,r_month,r_day,r_daytime,s_protocol,s_area,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}')".format(self.b_month , self.r_time , self.r_year , self.r_month , self.r_day , self.r_daytime , self.protocol , self.area , self.kind , self.content , self.val1 , self.val2 , self.val3 , self.val4 , self.val5 , self.status)
                self.curr2.execute(self.sql2)
                self.conn2.commit()
                self.conn2.close()
            
            print(str(r_time) + ' , ' + str(self.area)  + ' , ' + str(self.kind) + ' , insert into mysql successful.')

        except Exception as e:
            print('< Error > DB insert file : ' + str(e))
        finally:
            pass


###############################################################################################################################################
#
# start
#
###############################################################################################################################################
if __name__ == '__main__':
    realtime = monitor()
