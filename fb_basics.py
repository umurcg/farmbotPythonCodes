import serial
import time
from enum import IntEnum

class farmBot:

	class Axes(IntEnum):
		X=1
		Y=2
		Z=3



	serialConnection=None
	portName=None

	def __init__(self):

		self.portName='ACM0'
		self.serialConnection=self.connect_arduino()


	def connect_arduino(self):
		ser=serial.Serial('/dev/tty'+self.portName,9600)
		time.sleep(2)
		return ser

	def driveTrial(self, degree):
		self.serialConnection.write(degree)

	def driveAxis(self, axis, degree):
		self.serialConnection.write(axis+' '+degree)

	def conevrtDistanceToDegree(self,axis,length):
		#TODO calculate lengths for each axes from motor rotation
		return None

	#comment
	#connectArduino('ACM0').write('5')

