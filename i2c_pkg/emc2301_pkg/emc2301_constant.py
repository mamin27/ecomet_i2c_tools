# Address:

EMC2301_ADDRESS    = 0x5E      # 8 bit version

# Register

CONF               = 0x20   # Configuration
FAN_STAT           = 0x24   # Fan Status
FAN_STALL          = 0x25   # Fan Stall Status
FAN SPIN           = 0x26   # Fan Spin Status
DRIVE_FALL         = 0x27   # Drive Fall Status
FAN_INTERRUPT      = 0x29   # Controls the masking of interrupts on all fan related channels
PWM_POLARITY       = 0x2A   # Configures Polarity of the PWM driver
PWM_OUTPUT         = 0x2B   # Configures Output type of the PWM driver
PWM BASE           = 0x2D   # Selects the base frequency for the PWM output
FAN_SETTING        = 0x30   # Displays Driver inputs or Direct control of fan
PWM DIVIDE         = 0x31   # Store the divide ratio to set the frequency
FAN_CONF1          = 0x32   # FAN configuration #1
FAN_CONF2          = 0x33   # FAN configuration #2
GAIN               = 0x35   # Holds the gain terms
FAN_SPIN_UP        = 0x36   # Sets the config for Spin Up Routine
FAN_MAX_STEP       = 0x37   # Sets the maximum change per update
FAN_MIN_DRIVE      = 0x38   # Sets the minimum drive value
FAN_TACH           = 0x39   # Holds the tachometer reading
FAN_FAIL_BAND_LB   = 0x3A   # Stores the number of Tach counts used to determine how the actual fan speed must match the target fan speed low byte
FAN_FAIL_BAND_HB   = 0x3B   # -- High byte
TACH_TARGET_LB     = 0x3C   # Holds the target tachometer low byte
TACH_TARGET_HB     = 0x3D   # -- High byte
TACH_READ_HB       = 0x3E   # Holds the tachometer reading high byte
TACH_READ_LB       = 0x3F   # -- Low byte
SOFTWARE_LOCK      = 0xEF   # Lock all SWL register
PRODUCT_ID         = 0xFD   # Stores the unique Product ID
MANUF_ID           = 0xFE   # Manufacturer ID
REVISION_ID        = 0xFF   # Revision ID

# CONF (0x20) 8 Bits:        

MASK               = 0x80   # Blocks the ALERT# pin
DIS_TO             = 0x40   # Disables the SMBus timeout function
WD_EN              = 0x20   # Enables the WatchDog timer
DR_EXT_CLK         = 0x02   # Enables the internal tachometer clock or external clock
USE_EXT_CLK        = 0x01   # Enables to use a clock present on the CLK pin

# FAN STATUS (0x24) 8 Bits:

WATCH              = 0x80   # Indicates that the Watchdog Timer has expired
DRIVE_FAIL         = 0x04   # Indicates that the Fan driver cannot meet the programmed fan speed at maximum PWM duty cycle
FAN_SPIN           = 0x02   # Indicates that the Fan driver cannot spin up.
FAN_STALL          = 0x01   # Indicates that the Fan driver have stalled.

# FAN STALL STATUS (0x25) 8 Bits:

FAN_STALL_I        = 0x01

# FAN SPIN STATUS (0x26) 8 Bits:

FAN_SPIN_I         = 0x01

# FAN DRIVE STATUS (0x27) 8 Bits:

DRIVE_FAIL_I       = 0x01

# FAN INTERRUPT ENABLE (0x29) 8 Bits:

FAN_INT_EN         = 0x01  # Allows the Fan to assert the ALERT# pin

# PWM_POLARITY (0x2A) 8 Bits:

POLARITY           = 0x01  # Determine the polarity of PWM

# PWM_OUTPUT (0x2B) 8 Bits:

PWM_OT             = 0x01 #  Determine of output type of PWM driver

# PWM_BASE (0x2D) 8 Bits:

PWM_BASE           = 0x03 # 00 - 26 kHz (def)
                          # 01 - 19.531 kHz
                          # 10 - 4.882 Hz
                          # 11 - 2.441 Hz
                          
# FAN_CONF1 (0x32) 8 Bits:

UPDATE             = 0x07 # Ramp rate to the driver response
                          # 000 - 100ms
                          # 001 - 200ms
                          # 010 - 300ms
                          # 011 - 400ms (def)
                          # 100 - 500ms
                          # 101 - 800ms
                          # 110 - 1200ms
                          # 111 - 1600ms
EDGE			   = 0x18 # Number of Poles of the Fan
                          # 00 - 1 pole, effective tach multiplier 0.5
                          # 01 - 2 poles (def), -- 1
                          # 10 - 3 poles, -- 1.5
                          # 11 - 4 poles, -- 2
RANGE              = 0x60 # Range of TACH
                          # 00 - min 500 RPM, tach multiplier 1
                          # 01 - min 1000 RPM (def), tach multiplier 2
                          # 10 - min 2000 RPM, tach multiplier 4
                          # 11 - min 4000 RPM, tach multiplier 8
EN_AGLO            = 0x80 # Enables Fan Speed Control Algorithm

# FAN_CONF2 (0x33) 8 Bits:

ERR_RNG            = 0x06 # Control Advanced Control (Error window)
                          # 00 - 0 RPM (def)
                          # 01 - 50 RPM
                          # 10 - 100 RPM
                          # 11 - 200 RPM
DER_OPT            = 0x18 # Control Advanced Control
                          # 00 - No derivate option used
                          # 01 - Basic derivate
                          # 10 - Step derivate
                          # 11 - Basic and Step derivate
GLITCH_EN          = 0x20 # Disable low pass Glitch filter (remove high frequency noise)
EN_RRC             = 0x40 # Enable Ramp Rate Control

# GAIN (0x35) 8 Bits:

GAINP              = 0x03 # Control proportional Gain
                          # 00 - gain factor 1x
                          # 01 - gain factor 2x
                          # 10 - gain factor 4x (def)
                          # 11 - gain factor 8x
GAINI             = 0x0C  # Control integral Gain 
GAIND             = 0x30  # Control derivate Gain

# FAN_SPIN_UP (0x36) 8 Bits:

SPINUP_TIME       = 0x03  # Determines max spin up time
                          # 00 - 250ms
                          # 01 - 500ms (def)
                          # 10 - 1s
                          # 11 - 2s
SPIN_LVL          = 0x1C  # Determines final drive level used by Spin Up Routines
                          # 000 - 30%
                          # 001 - 35%
                          # 010 - 40%
                          # 011 - 45%
                          # 100 - 50%
                          # 101 - 55%
                          # 110 - 60% (def)
                          # 111 - 65%
NOKICK            = 0x20  # Determines if the Spin UP Routines will drive fan  to 100% duty cycle for 1/4 of the programed spin
DRIVE_FAIL_CNT    = 0xC0  # Determines how many updates cycles are used for Drive fail detection function
                          # 00 - Disabled
                          # 01 - 16 updates period
                          # 10 - 32 --
                          # 11 - 64 --

# FAN_MAX_STEP (0x37) 8 Bits:

FAN_MAX_STEP_MASK  = 0x3F

# FAN_MIN_DRIVE (0x38) 8 Bits:

FAN_MIN_DRIVE_MASK = 0xFF     # Def 40% (0x66)

# FAN_TACH (0x39) 8 Bits:

FAN_TACH_MASK      = 0xFF     # Def (0xF5)

# TACH Reg (0x3A,3B,3C,3D,3E,3F) 8 Bits:

FAN_FAIL_BAND_LB_M = 0xF8   # def (0xF8)
FAN_FAIL_BAND_HB_M = 0xFF   # def (0xFF)
TACH_TARGET_LB_M   = 0xF8   # def (0xF8)
TACH_TARGET_HB_M   = 0xFF   # def (0xFF)
TACH_READ_HB_MASK  = 0xFF   # def (0xFF)
TACH_READ_LB_MASK  = 0xF8   # def (0xF8)

# SOFTWARE_LOCK (0xEF) 8 Bits:

LOCK               = 0x01   # locked register

# CONF (0x20) 8 Bits clear :        

MASK_CLR           = 0x7F   # Blocks the ALERT# pin
DIS_TO_CLR         = 0xBF   # Disables the SMBus timeout function
WD_EN_CLR          = 0xDF   # Enables the WatchDog timer
DR_EXT_CLK_CLR     = 0xFD   # Enables the internal tachometer clock or external clock
USE_EXT_CLK_CLR    = 0xFE

# CONF Mask bites
CONF_HRES          = 0x0300
CONF_TRES          = 0x0400
CONF_BAT           = 0x0800
CONF_MODE          = 0x1000
CONF_HEAT          = 0x2000

# CONF MASK (0x20) 8 Bits:        

MASK_M             = 0x80   # Blocks the ALERT# pin
DIS_TO_M           = 0x40   # Disables the SMBus timeout function
WD_EN_M            = 0x20   # Enables the WatchDog timer
DR_EXT_CLK_M       = 0x02   # Enables the internal tachometer clock or external clock
USE_EXT_CLK_M      = 0x01   # Enables to use a clock present on the CLK pin
