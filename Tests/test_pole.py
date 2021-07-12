#
# Author: Wei Sheik
# Date:   31 Mar 2021
#

import serial

ser = serial.Serial("COM6", 115200)
ser

ser.open()
ser.is_open

s = ser.read(100)

ser.close()