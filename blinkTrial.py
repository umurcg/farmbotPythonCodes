import serial
import time 

ser=serial.Serial('/dev/ttyACM0',9600)

#wait for the connnection
time.sleep(2)

ser.write('5')

print "Finished writing"
