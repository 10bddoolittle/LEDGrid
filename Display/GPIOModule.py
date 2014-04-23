from DataStructures.CircularQueue import CircularQueue
import Adafruit_BBIO.GPIO as GPIO


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
        for col in range(len(active_columns)):
            GPIO.output(self.colgpios[col], active_columns[col])
        return

    # output a list of active rows through the row gpios
    def activateRow(self):
        GPIO.output(self.rowgpios.getHead(),1)
        return 

    def deactivateRow(self):
        GPIO.output(self.rowgpios.getHead(),0)
        return 

