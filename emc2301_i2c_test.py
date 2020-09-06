#!/usr/bin/env python3

import sys
print (sys.version)
from  i2c_pkg.emc2301_pkg import emc2301
import logging

sens = emc2301.EMC2301()

logging.basicConfig(level=logging.INFO,  # change level looging to (INFO, DEBUG, ERROR)
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='emc2301.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
sens._logger = logging.getLogger('ecomet.emc2301')
sens._logger.info('Start logging ...')

ret = sens.self_test()
if ret == 0 :
    print(":TEST_PASSED:")
else :
    print(":MISSING_CHIP:")
    
(val,ret) = sens.productid()
sens._logger.info('PRODUCT Read correct') if ret == 0 else sens._logger.error('Read error %s'.format(ret))
sens._logger.info('PRODUCT ID: %s',format(val))

(val,ret) = sens.manufid()
sens._logger.info('MANUFACTURER Read correct') if ret == 0 else sens._logger.error('Read error %s'.format(ret))
sens._logger.info('MANUF ID: %s',format(val))

(val,ret) = sens.revisionid()
sens._logger.info('REVISION Read correct') if ret == 0 else sens._logger.error('Read error %s'.format(ret))
sens._logger.info('REVISION ID: %s',format(val))

register = emc2301.conf_register_list()
print ('{}'.format(register))

print ('---------------------------------')
sens.write_register(register = 'FAN_CONF1', bits = ['EN_ALGO_CLR'])
sens.write_register(register = 'FAN_SETTING', bits = [60])
from time import sleep
sleep(5)
register = emc2301.conf_register_list()
print ('{}'.format(register))
from time import sleep
sleep(5)
sens.write_register(register = 'FAN_SETTING', bits = [100])
from time import sleep
sleep(5)
register = emc2301.conf_register_list()
print ('{}'.format(register))
sens.write_register(register = 'FAN_SETTING', bits = [200])
sleep(5)
register = emc2301.conf_register_list()
print ('{}'.format(register))
sens.write_register(register = 'FAN_SETTING', bits = [255])
sleep(5)
register = emc2301.conf_register_list()
print ('{}'.format(register))
sens.write_register(register = 'FAN_SETTING', bits = [0])
sleep(5)
register = emc2301.conf_register_list()
print ('{}'.format(register))

#sens.write_register(register = 'FAN_CONF1', bits = ['EN_ALGO'])
print ('---------------------------------')

#register = emc2301.conf_register_list()
#print ('{}'.format(register))
