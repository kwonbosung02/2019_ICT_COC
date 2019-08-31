import serial
import time
'''
class serial.Serial

__init__(
     port=None,
     baudrate=9600,
     bytesize=EIGHTBITS,
     parity=PARITY_NONE,
     stopbits=STOPBITS_ONE,
     timeout=None,
     xonxoff=False,
     rtscts=False,
     writeTimeout=None,
     dsrdtr=False,
     interCharTimeout=None 
)
'''

ard = serial.Serial('/dev/ttyACM0')
ard.write([0])
time.sleep(1)
ard.write([1])
time.sleep(1)
ard.write([2])

time.sleep(1)
ard.write([3])

time.sleep(1)
ard.write([4])
