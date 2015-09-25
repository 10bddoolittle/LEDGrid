from DataStructures import CircularQueue


class LEDArray:

    # circular queue
    # [0,1,2,...,(numrows - 1)]
    rowindices = CircularQueue
    array = [[]] # list of lists for now, potentially implement as matrix in future

    # initialize array with numrows and numcols
    def __init__(self,numrows,numcols):
        for row in range(0, numrows):
            for col in range(0, numcols):
                self.array[row][col].append(0)

        self.rowindices = CircularQueue(range(0,numrows))
        
        return

    # sets self.array as newarray
    def updateArray(self,newarray):
        self.array = newarray
        return

    # returns the row at index
    def getRow(self,index):
        return self.array[index]

    # returns the head of rowindices
    def getRowIndex(self):
        return self.rowindices.getHead

