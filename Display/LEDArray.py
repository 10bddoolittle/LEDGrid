from DataStructures import CircularQueue


class LEDArray:

    # circular queue
    # [0,1,2,...,(numrows - 1)]
    rowindices = CircularQueue
    array = [[]] # list of lists for now, potentially implement as matrix in future

    # initialize array with numrows and numcols
    def __init__(self,numrows,numcols):
        return

    # sets self.array as newarray
    def UpdateArray(self,newarray):
        return

    # returns the row at index
    def GetRow(self,index):
        return

    # returns the head of rowindices
    def GetRowIndex(self):
        return

