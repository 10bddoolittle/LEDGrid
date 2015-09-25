from DataStructures import CircularQueue
import Adafruit_BBIO.GPIO as GPIO


class GPIOModule:

    # Use circular queue because row outputs are periodic and predictable
    rowgpios = CircularQueue()
    # plain list because column outputs are dynamic
    colgpios = []

    def __init__(self,rowgpios,colgpios):
        return

    # output a list of the active columns through column GPIOs
    def OutputColumns(self,active_columns):
        return

    # output a list of active rows through the row gpios
    def OutputRows(self,active_rows):
        return