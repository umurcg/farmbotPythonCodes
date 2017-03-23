import serial
import fb_basics as basic



def drive(dir,angle):
   
   command=str(dir)+','+str(angle)
   basic.connectArduino('ACM0').write(command)
        

drive(0,360*4)
