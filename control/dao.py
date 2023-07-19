#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221129
# Update   : 20221208
# Function : new taipei animals department

################################################################################################################################################################################
# MySQL
################################################################################################################################################################################
db          = {'root':'password' , 'tinfar':'1qaz2wsx' , 'backup':'backup#123'}
db_connect  = {'host':'61.220.205.143' , 'port':3306 , 'user':'backup' , 'pwd':'SLbackup#123' , 'db':'tinfar_animals' , 'charset':'utf8'}

################################################################################################################################################################################
# device
################################################################################################################################################################################

###############
#
# modbus RTU
#
###############

### tinfar test CW9 - modbus RTU
i6_rtu_connect = {'mac_port1':'/dev/tty.usbserial-1410','mac_port2':'/dev/tty.usbserial-AB0LZ3NC','linux_port':'/dev/ttyUSB0','win_port':'COM4'} 
i6_rtu_para    = {'br':'9600','fc':'4','kind':'cw9','tb':'modbus_sensor','protocol':'modbusRTU'}
i6_rtu_sensor  = {'temp':'0x0000','rh':'0x0001','co2':'0x0002','pm2.5':'0x0003','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm10':'0x0008' , 'nh3':'0x000A' , 'h2s':'0x000B' , 'pr':'0x0010'}

###############
#
# modbus TCP
#
###############

### 連大興 I6 - modbus TCP
lian_i6_tcp_connect = {'ip':'60.248.16.152','port':502,'id':2}
lian_i6_tcp_param   = {'kind':'CB','tb':'medicine','protocol':'modbusTCP'}
lian_i6_tcp_sensor  = {'temp':'0x0000','ec':'0x0001','ph':'0x0002','pm2.5':'0x0003','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm10':'0x0008'}

### tinfar test CW9 - modbus TCP
i6_tcp_connect = {'ip':'61.220.205.144','port':502,'id':1}
i6_tcp_param   = {'kind':'CB','tb':'medicine','protocol':'modbusTCP'}
i6_tcp_sensor  = {'temp':'0x0000','rh':'0x0001','co2':'0x0002','pm2.5':'0x0003','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm10':'0x0008'}

### tinfar test CW9 - modbus TCP
i6_tcp_connect2 = {'ip':'61.220.205.144','port':502,'id':3}
i6_tcp_param2   = {'kind':'CB','tb':'medicine','protocol':'modbusTCP'}
i6_tcp_sensor2  = {'temp':'0x0000','rh':'0x0001','co2':'0x0002','pm2.5':'0x0003','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm10':'0x0008'}

### tinfar test CB - modbus TCP
cb_tcp_connect = {'ip':'61.220.205.144','port':502}
cb_tcp_param   = {'kind':'CB','tb':'medicine','protocol':'modbusTCP'}
cb_tcp_sensor  = {'temp':'0x0000','rh':'0x0001','co2':'0x0002','pm2.5':'0x0000','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm1.0':'0x0001','noise':'0x0002'}

