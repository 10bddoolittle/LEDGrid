from DataStructures.CircularQueue import CircularQueue
import Adafruit_BBIO.GPIO as GPIO
import time


class GPIOModule:

    # Use circular queue because row outputs are periodic and predictable
    #rowgpios = CircularQueue()
    
    # plain list because column outputs are dynamic
    #colgpios = []

    def __init__(self,rowgpios,colgpios):
        self.rowgpios = CircularQueue(rowgpios)
        self.colgpios = colgpios

        for row in range(len(rowgpios)):
            GPIO.setup(rowgpios[row], GPIO.OUT)

        for col in range(len(colgpios)):
            GPIO.setup(colgpios[col], GPIO.OUT)

        return

    # output a list of the active columns through column GPIOs
    # active_columns is a list of 0 or 1's
    # colgpios is a list of gpio ports
    def outputColumns(self,active_columns):
        map(self.setLED,self.colgpios,active_columns)


    # output a list of active rows through the row gpios
    def activateRow(self):
        GPIO.output(self.rowgpios.getHead(),1)

    def deactivateRow(self):
        GPIO.output(self.rowgpios.getHead(),0)

    def setLED(self,gpio,value):
        GPIO.output(gpio,value)


