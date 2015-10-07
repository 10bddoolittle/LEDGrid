from DataStructures.CircularQueue import CircularQueue

class LEDArray:

    # circular queue
    # [0,1,2,...,(numrows - 1)]
    #rowindices = CircularQueue
    # list of lists for now, potentially implement as matrix in future

    # initialize array with numrows and numcols
    def __init__(self,numrows,numcols):
        self.array = []

        for row in range(0, numrows):
            arrayrow = []
            for col in range(0, numcols):
                arrayrow.append(0)
            self.array.append(arrayrow)

        self.rowindices = CircularQueue(range(0,numrows))
        return

    # sets self.array as newarray
    def updateArray(self,newarray):
        self.array = newarray
        return

    # Gets the list of active columns for the given row index
    def getActiveColumns(self,index):
        return self.array[index]

    # returns the head of rowindices
    def getRowIndex(self):
        return self.rowindices.getHead()

