import serial
import time



def connectArduino(portName):
	ser=serial.Serial('/dev/tty'+portName,9600)
	time.sleep(2)
	return ser




connectArduino('ACM0').write('5')

