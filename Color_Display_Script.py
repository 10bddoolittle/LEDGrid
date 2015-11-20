import Display_Module
from DataStructures.CircularQueue import CircularArray

rowgpios = ["P8_7",
			"P8_9",
			"P8_11"]

colgpios = ["P8_8","P8_10","P8_12","P8_14"]

display = Display_Module.Display(rowgpios,colgpios)


red = [[0],[0],[1]]
blue = [[0],[1],[0]]
green = [[1],[0],[0]]
purple = [[0],[1],[1]]
yellow = [[1],[0],[1]]
cyan = [[1],[1],[0]]
white = [[1],[1],[1]]
black = [[0],[0],[0]]

ledrow = CircularArray(
					[[1,1,0,0],
				     [0,0,1,1],
					 [1,0,1,0]]
					)

runtime = .6
flickertime = .00001
flashtime = .15

it = 0

while True:
    # display.run(red, runtime, flickertime)
    # display.run(white, flashtime, flickertime)
    # display.run(purple, runtime, flickertime)
    # display.run(white, flashtime, flickertime)
    # display.run(blue, runtime, flickertime)
    # display.run(white, flashtime, flickertime)
    # display.run(cyan, runtime, flickertime)
    # display.run(white, flashtime, flickertime)
    # display.run(green, runtime, flickertime)
    # display.run(white, flashtime, flickertime)
    # display.run(yellow, runtime, flickertime)
    # display.run(white, flashtime, flickertime)

    display.run(ledrow.array,flashtime,flickertime)
    ledrow.shiftRight([0])
    ledrow.shiftRight([1])
    ledrow.shiftRight([2])

  