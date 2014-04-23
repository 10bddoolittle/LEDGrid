import time

from Display.GPIOModule import GPIOModule
from Display.LEDArray import LEDArray


class Display:

#active_cols = []

    def __init__(self,rowgpios,colgpios):
        self.numrows = len(rowgpios)
        self.numcols = len(colgpios)
        self.led_array = LEDArray(self.numrows, self.numcols)
        self.gpio_module = GPIOModule(rowgpios,colgpios)
        return

    def outputPattern(self):
        # turn off current row
        self.gpio_module.deactivateRow()
        # shifting the circular queues
        self.gpio_module.rowgpios.shift()
        self.led_array.rowindices.shift()
        # getting the new set of active columns
        active_cols = self.led_array.getActiveColumns(self.led_array.getRowIndex())
        # Outputting Values to the LED Grid Hardware
        self.gpio_module.outputColumns(active_cols)
        # Activate the new row
        self.gpio_module.activateRow()
        return

    def run(self, array, run_time):
        dt = 0

        display.led_array.updateArray(array)

        timestart = time.time()
        while dt < run_time:

            display.outputPattern()
            time.sleep(0.01)
            dt = time.time()-timestart


if __name__ == "__main__":

    rowgpios = ["P8_10","P8_12"]
    colgpios = ["P8_14","P8_16"]

    display = Display(rowgpios,colgpios)

    while True:
        array_1 = [[1, 0],
                   [0, 0]]

        array_2 = [[0, 1],
                   [0, 0]]

        array_3 = [[0, 0],
                   [1, 0]]

        array_4 = [[0, 0],
                   [0, 1]]

        display.run(array_1, 2 )
        display.run(array_2, 2 )
        display.run(array_3, 2 )
        display.run(array_4, 2 )


    # while True:
    #     time.sleep(.01)
    #     display.run()






