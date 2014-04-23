__author__ = 'briandoolittle'

import Display_Module

rowgpios = ["P8_7","P8_9","P8_11"]
colgpios = ["P8_8"]

display = Display_Module.Display(rowgpios,colgpios)


array1 = [[0],
		  [1],
		  [0]]

while True:
    display.run(array1, 2, 2)
    print "meow"