__author__ = 'briandoolittle'

import Display_Module

rowgpios = ["P8_7","P8_9","P8_11","P8_13","P8_15","P8_17"]
colgpios = ["P8_8","P8_10","P8_12","P8_14"]

display = Display_Module.Display(rowgpios,colgpios)


array1 = [[1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],]

array2 = [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],]

array3 = [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],]

array4 = [[0, 0, 0, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 1],]


while True:

    display.run(array1, 2, .001)
    display.run(array2, 2, .001)
    display.run(array3, 2, .001)
    display.run(array4, 2, .001)

