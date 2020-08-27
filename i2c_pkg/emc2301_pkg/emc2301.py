from __future__ import division
import logging
import time
import math
from i2c_pkg.emc2301_pkg import emc2301_constant

reg_list = { 'CONF' : emc2301_constant.CONF,'FAN_STAT' : emc2301_constant.FAN_STAT, 'FAN_STALL' :  emc2301_constant.FAN_STALL, 'FAN_SPIN' : emc2301_constant.FAN_SPIN,
             'DRIVE_FALL' : emc2301_constant.DRIVE_FALL, 'FAN_INTERRUPT' : emc2301_constant.FAN_INTERRUPT, 
             'PWM_POLARITY' : emc2301_constant.PWM_POLARITY, 'PWM_OUTPUT' :  emc2301_constant.PWM_OUTPUT, 'PWM_BASE' : emc2301_constant.PWM_BASE, 
             'FAN_SETTING' : emc2301_constant.FAN_SETTING, 'PWM_DIVIDE' : emc2301_constant.PWM_DIVIDE, 
             'FAN_CONF1' : emc2301_constant.FAN_CONF1, 'FAN_CONF2' : emc2301_constant.FAN_CONF2, 'GAIN' : emc2301_constant.GAIN,
             'FAN_SPIN_UP' : emc2301_constant.FAN_SPIN_UP, 'FAN_MAX_STEP' : emc2301_constant.FAN_MAX_STEP, 'FAN_MIN_DRIVE' :  emc2301_constant.FAN_MIN_DRIVE,
             'FAN_TACH' : emc2301_constant.FAN_TACH, 'FAN_FAIL_BAND_LB' : emc2301_constant.FAN_FAIL_BAND_LB, 'FAN_FAIL_BAND_HB' :   emc2301_constant.FAN_FAIL_BAND_HB,
             'TACH_TARGET_LB' : emc2301_constant.TACH_TARGET_LB, 'TACH_TARGET_HB' :  emc2301_constant.TACH_TARGET_HB, 'TACH_READ_HB' : emc2301_constant.TACH_READ_HB, 'TACH_READ_LB' : emc2301_constant.TACH_READ_LB,
             'SOFTWARE_LOCK' : emc2301_constant.SOFTWARE_LOCK, 'PRODUCT_ID' : emc2301_constant.PRODUCT_ID, 'MANUF_ID' : emc2301_constant.MANUF_ID, 'REVISION_ID' : emc2301_constant.REVISION_ID
        }
conf_bit_on_list = { 'MASK' :  emc2301_constant.MASK,
                     'DIS_TO' : emc2301_constant.DIS_TO,
                     'WD_EN' :  emc2301_constant.WD_EN,
                     'DR_EXT_CLK' :  emc2301_constant.DR_EXT_CLK,
                     'USE_EXT_CLK' : emc2301_constant.USE_EXT_CLK
                }

conf_bit_off_list = { 'MASK_CLR' :  emc2301_constant.MASK_CLR,
                      'DIS_TO_CLR' : emc2301_constant.DIS_TO_CLR,
                      'WD_EN_CLR' :  emc2301_constant.WD_EN_CLR,
                      'DR_EXT_CLK_CLR' :  emc2301_constant.DR_EXT_CLK_CLR,
                      'USE_EXT_CLK_CLR' : emc2301_constant.USE_EXT_CLK_CLR
                }
   
conf_mask_bit_list = { 'MASK_M' : emc2301_constant.MASK_M,
                       'DIS_TO_M' : emc2301_constant.DIS_TO_M,
                       'WD_EN_M' :  emc2301_constant.WD_EN_M,
                       'DR_EXT_CLK_M' :  emc2301_constant.DR_EXT_CLK_M,
                       'USE_EXT_CLK_M' : emc2301_constant.USE_EXT_CLK_M
                      }
                      
fan_stat_bit_off_list = { 'WATCH_CLR' :  emc2301_constant.WATCH_CLR,
                      'DRIVE_FAIL_CLR' : emc2301_constant.DRIVE_FAIL_CLR,
                      'FAN_SPIN_CLR' :  emc2301_constant.FAN_SPIN_CLR,
                      'FAN_STALL_CLR' :  emc2301_constant.FAN_STALL_CLR
                }
   
fan_stat_mask_bit_list = { 'WATCH_M' : emc2301_constant.WATCH_M,
                       'DRIVE_FAIL_M' : emc2301_constant.DRIVE_FAIL_M,
                       'FAN_SPIN_M' :  emc2301_constant.FAN_SPIN_M,
                       'FAN_STALL_M' :  emc2301_constant.FAN_STALL_M
                      }
                      
fan_stat_bit_off_list = { 'WATCH_CLR' :  emc2301_constant.WATCH_CLR,
                      'DRIVE_FAIL_CLR' : emc2301_constant.DRIVE_FAIL_CLR,
                      'FAN_SPIN_CLR' :  emc2301_constant.FAN_SPIN_CLR,
                      'FAN_STALL_CLR' :  emc2301_constant.FAN_STALL_CLR
                }
   
fan_stat_mask_bit_list = { 'WATCH_M' : emc2301_constant.WATCH_M,
                       'DRIVE_FAIL_M' : emc2301_constant.DRIVE_FAIL_M,
                       'FAN_SPIN_M' :  emc2301_constant.FAN_SPIN_M,
                       'FAN_STALL_M' :  emc2301_constant.FAN_STALL_M
                      }
                      
logger = logging.getLogger(__name__) 

def conf_register_list() :

   emc = EMC2301()
   emc._logger = logging.getLogger('ecomet.emc2301.reglist') 
   register = {}
   reg_conf = {}
   reg_spin_up = {}
   reg_fan_stat = {}
   reg_pwm = {}
   reg_tach = {}
   reg_id = {}
   
   list_4096 = [32,64,128,256,512,1024,2048,4096]
   list_128 = [1,2,4,8,16,32,64,128]
   list_32 = [1,2,4,8,16,32]
   list_16 = [0,0,0,1,2,4,8,16]
                      
   reg_conf['MASK'] = 'UNMASKED' if emc.read_register( register = 'CONF' )[0] & conf_mask_bit_list['MASK_M'] > 0 else 'MASKED'
   reg_conf['DIS_TO'] = 'ENABLED' if emc.read_register( register = 'CONF' )[0] & conf_mask_bit_list['MASK_M'] > 0 else 'DISABLED'
   reg_conf['WD_EN'] = 'DISABLED' if emc.read_register( register = 'CONF' )[0] & conf_mask_bit_list['MASK_M'] > 0 else 'OPERATE'
   reg_conf['DR_EXT_CLK'] = 'CLK_INPUT' if emc.read_register( register = 'CONF' )[0] & conf_mask_bit_list['MASK_M'] > 0 else 'CLK_OUTPUT'
   reg_conf['USE_EXT_CLK'] = 'INTERNAL' if emc.read_register( register = 'CONF' )[0] & conf_mask_bit_list['MASK_M'] > 0 else 'EXTERNAL'
#   reg_conf['EN_ALGO'] =
#   reg_conf['RANGE'] =
#   reg_conf['EDGES'] =
#   reg_conf['UPDATE'] = 
#   reg_conf['EN_RRC'] = 
#   reg_conf['GLITCH_EN'] = 
#   reg_conf['DER_OPT'] =
#   reg_conf['ERR_RNG'] =
#   reg_conf['GAIND'] =
#   reg_conf['GAINI'] =
#   reg_conf['GAINP'] = 
   
#   reg_spin_up['DRIVE_FAIL_CNT'] =
#   reg_spin_up['NOKICK'] =
#   reg_spin_up['SPIN_LVL'] =
#   reg_spin_up['SPINUP_TIME'] =
   tbin = emc.read_register( register = 'FAN_MAX_STEP' )[0]
   res = 0
   for idx in range (0,6) :
     res = res + (tbin % 2)  * list_32[idx]
     tbin = tbin >> 1
   reg_spin_up['FAN_MAX_STEP'] = res
   tbin = emc.read_register( register = 'FAN_MIN_DRIVE' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin % 2)  * list_128[idx]
     tbin = tbin >> 1
   reg_spin_up['FAN_MIN_DRIVE'] = (res/255)*100
   
   reg_fan_stat['WATCH'] = 'EXPIRED' if emc.read_register( register = 'FAN_STAT' )[0] & fan_stat_mask_bit_list['WATCH_M'] > 0 else 'NOT_SET'
   reg_fan_stat['DRIVE_FAIL'] = 'CANOT_MEET' if emc.read_register( register = 'FAN_STAT' )[0] & fan_stat_mask_bit_list['DRIVE_FAIL_M'] > 0 else 'MEET'
   reg_fan_stat['FAN_SPIN'] = 'CANOT_SPIN' if emc.read_register( register = 'FAN_STAT' )[0] & fan_stat_mask_bit_list['FAN_SPIN_M'] > 0 else 'SPIN'
   reg_fan_stat['FAN_STALL'] = 'STALL' if emc.read_register( register = 'FAN_STAT' )[0] & fan_stat_mask_bit_list['FAN_STALL_M'] > 0 else 'NOT_STALL'
   tbin = emc.read_register( register = 'FAN_SETTING' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin % 2) * list_128[idx]  
     tbin = tbin >> 1
   reg_fan_stat['FAN_SETTING'] = (res/255)*100
   
   
#   reg_pwm['PWM_POLARITY'] = 
#   reg_pwm['PWM_OUTPUT'] = 
#   reg_pwm['PWM_BASE'] =
   tbin = emc.read_register( register = 'PWM_DIVIDE' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin % 2)  * list_128[idx]
     tbin = tbin >> 1
   reg_pwm['PWM_DIVIDE'] = res

   tbin = emc.read_register( register = 'FAN_TACH' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin % 2) * list_4096[idx]
     tbin_hb = tbin >> 1
   reg_tach['FAN_TACH'] = res 
   tbin_lb = emc.read_register( register = 'FAN_FAIL_BAND_LB' )[0]
   tbin_hb = emc.read_register( register = 'FAN_FAIL_BAND_HB' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin_hb % 2) * list_4096[idx]
     tbin_hb = tbin_hb >> 1
   for idx in range (0,8) :
     res = res + (tbin_lb % 2) * list_16[idx]
     tbin_lb = tbin_lb >> 1
   reg_tach['FAN_FAIL_BAND'] = res
   tbin_lb = emc.read_register( register = 'TACH_TARGET_LB' )[0]
   tbin_hb = emc.read_register( register = 'TACH_TARGET_HB' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin_hb % 2) * list_4096[idx]
     tbin_hb = tbin_hb >> 1
   for idx in range (0,8) :
     res = res + (tbin_lb % 2) * list_16[idx]
     tbin_lb = tbin_lb >> 1
   reg_tach['TACH_TARGET'] = res
   tbin_lb = emc.read_register( register = 'TACH_READ_LB' )[0]
   tbin_hb = emc.read_register( register = 'TACH_READ_HB' )[0]
   res = 0
   for idx in range (0,8) :
     res = res + (tbin_hb % 2) * list_4096[idx]
     tbin_hb = tbin_hb >> 1
   for idx in range (0,8) :
     res = res + (tbin_lb % 2) * list_16[idx]
     tbin_lb = tbin_lb >> 1
   reg_tach['TACH_READ'] = res
       
   reg_id['PRODUCT_ID'] = emc.productid()[0]
   reg_id['MANUF_ID'] = emc.manufid()[0]
   reg_id['REVISION_ID'] = emc.revisionid()[0]
   
   register['CONF'] = reg_conf
   register['FAN_STAT'] = reg_fan_stat
   register['SPIN'] = reg_spin_up
   register['PWM'] = reg_pwm
   register['TACH'] = reg_tach
   register['ID'] = reg_id
   
   return (register);

class EMC2301(object):
    '''emc2301() PWM LED/servo controller.'''

    def __init__(self, address=emc2301_constant.EMC2301_ADDRESS, i2c=None, **kwargs) :
        '''Initialize the emc2301.'''
        # Setup I2C interface for the device.
        if i2c is None:
            import i2c_pkg.i2c as I2C
            i2c = I2C
        self._logger = logging.getLogger(__name__)    
        self._device = i2c.get_i2c_device(address, **kwargs)
    def self_test(self) :
        try :
          (np,ret) = self.productid()
        except :
          ret = 1
        return ret
    def read_register(self, register) :
        if register in ['CONF','FAN_STAT','PWM_DIVIDE','FAN_SETTING','FAN_MAX_STEP','FAN_MIN_DRIVE',
                        'FAN_TACH','FAN_FAIL_BAND_LB','FAN_FAIL_BAND_HB','TACH_TARGET_LB','TACH_TARGET_HB','TACH_READ_LB','TACH_READ_HB',
                        'PRODUCT_ID','MANUF_ID','REVISION_ID'] :
           ret = 0
           try:
              reg_status_bita = self._device.readList(reg_list[register],1)
              if not reg_status_bita:
                return (0x00,2)
              reg_status_hex = '0x' + '{0:02x}'.format(reg_status_bita[0])
              reg_status = int(reg_status_hex, 0)
           except :
              ret = ret + 1;
           if ret > 1 :
              self._logger.debug('read_register %s failed (%s)',register,ret)
              return (0x00,ret)
           else :
              self._logger.debug('read_register, init reg_status: %s', '{0}'.format(reg_status_hex))
              self._logger.debug('read_register %s, data: %s', register, '{0:b}'.format(reg_status))
              return (reg_status,0)
    def write_register(self, register, bits) :
          ret = 0
          (reg_status,ret) = self.read_register( register = register )
          if register == 'CONF' :
           for ibit in bits :
               bit_clr = ibit + '_CLR'
               if register == 'CONF' :
                  reg_status = reg_status & conf_bit_off_list[bit_clr]
               self._logger.debug('write_register, init reg_status: %s, bit_mask_reg %s', '{0:02X}'.format(reg_status), format(bit_clr))
               reg_status = reg_status | conf_bit_on_list[ibit]
               self._logger.debug('write_register, init reg_status: %s, bit %s', '{0:02X}'.format(reg_status), '{0:02X}'.format(conf_bit_on_list[ibit]))
           reg_status = reg_status & 0xff
           try :
               self._device.write8(reg_list[register],reg_status)
           except :
               ret = ret + 1
               self._logger.debug('writelist error')
          else :
              ret = 1
          if ret > 1 :
             self._logger.debug('write_register %s failed (%s)', register, ret)
          else :
             self._logger.debug('write_register %s, byte data: %s', register,reg_status)
          return ret
    def productid (self) :
       ret = 0
       (temp,lret) = self.read_register( register = 'PRODUCT_ID' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('PRODUCT_ID: %s','{0:02X}'.format(temp))
           return ('{0:02X}'.format(temp),0)
    def manufid (self) :
       ret = 0
       (temp,lret) = self.read_register( register = 'MANUF_ID' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('MANUF_ID: %s','{0:02X}'.format(temp))
           return ('{0:02X}'.format(temp),0)
    def revisionid (self) :
       ret = 0
       (temp,lret) = self.read_register( register = 'REVISION_ID' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('REVISION_ID: %s','{0:02X}'.format(temp))
           return ('{0:02X}'.format(temp),0)
'''
    def write_mert_invoke (self, register) :
        if register == 'TEMP' or register == 'HUMDT' :
            try :
                self._device.writeRaw8(reg_list[register]);
            except :
                self._logger.info('write_invoke %s mask failed', register)
                return 1
            finally :
                self._logger.info('write_invoke %s mask', register)
                return 0
    def both_measurement (self) :
        byt_reg = ()
        ret = 0
        ret = self.write_register( register = 'CONF', bits = ['MODE_BOTH'])
        from time import sleep
        ret = ret + self.write_mert_invoke( register = 'TEMP' )
        sleep(0.02)
        byt_reg = self._device.readRaw32()
        self._logger.debug('temp byte: %s', hex(byt_reg[1] + (byt_reg[0] << 8)))
        self._logger.debug('humdt byte: %s', hex(byt_reg[3] + (byt_reg[2] << 8)))
        temp = int(byt_reg[1] + (byt_reg[0] << 8))
        temp = temp/power(2,16)
        temp = temp*165 - 40
        humdt = int(byt_reg[3] + (byt_reg[2] << 8))
        humdt = humdt/power(2,16)
        humdt = humdt*100
        return  (temp, humdt, ret)
    def measure_temp (self) :
        byt_reg = ()
        ret = 0
        ret = self.write_register( register = 'CONF', bits = ['MODE_ONLY'])
        from time import sleep
        ret = ret + self.write_mert_invoke( register = 'TEMP')
        sleep(0.01)
        byt_reg = self._device.readRaw16()
        self._logger.debug('temp byte: %s', hex(byt_reg[1] + (byt_reg[0] << 8)))
        temp = int(byt_reg[1] + (byt_reg[0] << 8))
        temp = temp/power(2,16)
        temp = temp*165 - 40
        return (temp,ret)
    def measure_hmdt (self) :
        byt_reg = ()
        ret = 0
        ret = self.write_register( register = 'CONF', bits = ['MODE_ONLY'])
        from time import sleep
        ret = ret + self.write_mert_invoke( register = 'HUMDT')
        sleep(0.01)
        byt_reg = self._device.readRaw16()
        self._logger.debug('temp byte: %s', hex(byt_reg[1] + (byt_reg[0] << 8)))
        hmdt = int(byt_reg[1] + (byt_reg[0] << 8))
        hmdt = hmdt/power(2,16)
        hmdt = hmdt*100
        return (hmdt,ret)
    def sw_reset (self) :
        ret = self.write_register( register = 'CONF', bits = ['RST_ON'])
        from time import sleep
        sleep(0.1) # wait for done sw reset
        return ret
    def battery (self) :
        (reg_status,ret) = self.read_register( register = 'CONF' )
        reg_status = reg_status & conf_bit_on_list['BTST_LO']
        if reg_status > 0 :
            ret = 1
        else :
            ret = 0
        return ret
    def serial (self) :
       ret = 0
       (byte1,lret) = self.read_register( register = 'SER_ID1' )
       if lret > 0 :
          ret = ret + 1
       (byte2,lret) = self.read_register( register = 'SER_ID2' )
       if lret > 0 :
          ret = ret + 1
       (byte3,lret) = self.read_register( register = 'SER_ID3' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('Serial: %s:%s:%s','{0:04X}'.format(byte1),'{0:04X}'.format(byte2),'{0:04X}'.format(byte3))
           return ('{0:04X}'.format(byte1) + '-' + '{0:04X}'.format(byte2) + '-' + '{0:04X}'.format(byte3),0)
    def manufacturer (self) :
       ret = 0
       (temp,lret) = self.read_register( register = 'MANUF' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('Serial: %s','{0:04X}'.format(temp))
           return ('{0:04X}'.format(temp),0)
    def deviceid (self) :
       ret = 0
       (temp,lret) = self.read_register( register = 'DEVID' )
       if lret > 0 :
          ret = ret + 1
       if ret > 0 : 
           self._logger.error('Read error %s'.format(ret))
           return (0,ret)
       else :
           self._logger.debug('DeviceID: %s','{0:04X}'.format(temp))
           return ('{0:04X}'.format(temp),0)
'''
