class CircularQueue:

    # list where the circularqueue elements are stored
    queue = []

    # Takes a list and creates a circularqueue object
    def __init__(self,list):
        self.queue = list
        self.length = len(self.queue)
        return

    # Shift: takes the head of self.queue and shifts it to the tail
    def shift(self):
        self.queue = self.queue[1:self.length] + [self.queue[0]]
        return

    # GetHead: returns the head of self.queue
    def getHead(self):
        return self.queue[0]

class CircularArray:

    def __init__(self,array):
        self.array = array
        self.numrows = len(self.array)
        self.numcols = len(self.array[0])

    def shiftLeft(self,rowids=[]):
        if rowids == []:
            rowids = range(0,self.numrows)

        for row in rowids:
            self.array[row] = self.array[row][1:self.numcols] + [self.array[row][0]]

    def shiftRight(self,rowids=[]):
        if rowids == []:
            rowids = range(0,self.numrows)
        
        for row in rowids:

            self.array[row] = [self.array[row][self.numcols-1]] + self.array[row][0:self.numcols-1]

    def shiftUp(self,colids=[]):
        if colids == []:
            colids = range(0,self.numcols)

        temparray = self.array

        for col in colids:
            for row in range(0,self.numrows):

                newrow = row - 1

                if newrow < 0:
                    newrow = self.numrows-1

                self.array[row][col] = temparray[newrow][col]

    def shiftDown(self,colids=[]):
        if colids == []:
                colids = range(0,self.numcols)

        temparray = self.array

        for col in colids: 
            for row in range(0,self.numrows):

                newrow = row + 1

                if newrow == self.numrows:
                    newrow = 0
                    
                self.array[row][col] = temparray[newrow][col]







