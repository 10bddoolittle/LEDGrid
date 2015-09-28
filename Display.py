from Display.GPIOModule import GPIOModule
from Display.LEDArray import LEDArray
import time

class Display:

    #active_cols = []

    def __init__(self,rowgpios,colgpios):
    	self.numrows = len(rowgpios)
    	self.numcols = len(colgpios)
		self.led_array = LEDArray(self.numrows, self.numcols))
		self.gpio_module = GPIOModule(rowgpios,colgpios)
        return

    def run(self):
    	self.gpio_module.deactivateRow()
    	self.gpio_module.rowgpios.shift()
    	self.led_array.rowindices.shift()
   		active_cols = self.led_array.getActiveColumns(self.led_array.getRowIndex())
   		self.gpio_module.outputColumns(active_cols)
   		self.gpio_module.activateRow()
    	return


if __name__ == "__main__":
	
	rowgpios = ["P8_10","P8_12"]
	colgpios = ["P8_14","P8_16"]

	display = Display(rowgpios,colgpios)

	display.led_array.updateArray([[1,1],[1,1]])
	
	while True:
		time.sleep(.02)
		display.run()






    