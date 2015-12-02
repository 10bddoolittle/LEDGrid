'''
The CircularQueue class is a one dimensional list data structure that
can be shifted to the right or left. The list wraps back on itself 
allowing the user to cycle through all of the elements of the list
'''
class CircularQueue:

    # CircularQueue is initialize with a list []
    def __init__(self,list):
        self.queue = list              # list to cycle through
        self.length = len(self.queue)  # Length of list

    # Shift: takes the head of self.queue and shifts it to the tail
    def shift(self):
        self.queue = self.queue[1:self.length] + [self.queue[0]]

    # GetHead: returns the current head of the circular queue
    # Input: None
    # OUTPUT: head of self.queue
    def getHead(self):
        return self.queue[0]

'''
The CircularArray is similar to the circular list but is two dimensional.
Columns of the array may be shifted up or down, and rows may be shifted
right or left.
'''
class CircularArray:

    # CircularArray is initialized with just an array [[]]
    def __init__(self,array):
        self.array = array
        self.numrows = len(self.array)
        self.numcols = len(self.array[0])

    # shiftLeft: shifts the elements of the specified row to the left
    #            appending the first element to the tail of the row
    # INPUT: rowids (list of row indexes that you want to shift)
    # OUTPUT: None (stores new array in self.array)
    def shiftLeft(self,rowids=[]):
        # if no rowids, will shift all rows
        if rowids == []:
            rowids = range(0,self.numrows)

        # looping through specified rows and shifting
        for row in rowids:
            self.array[row] = self.array[row][1:self.numcols] + [self.array[row][0]]

    # shiftRight: shifts the elements of the specified row to the right
    #             appending the last element to the head of the row
    # INPUT: rowids (list of row indexes that you want to shift)
    # OUTPUT: None (stores new array in self.array)
    def shiftRight(self,rowids=[]):
        # if no rowids, will shift all rows
        if rowids == []:
            rowids = range(0,self.numrows)
        
        # looping through specified rows and shifting
        for row in rowids:
            self.array[row] = [self.array[row][self.numcols-1]] + self.array[row][0:self.numcols-1]

    # shiftUp: shifts the elements of the specified column up appending
    #          the top element to the bottom of the column
    # INPUT: colids (list of column indexes that you want to shift)
    # OUTPUT: None (stores new array in self.array)
    def shiftUp(self,colids=[]):
        # if no colids, shift all columns
        if colids == []:
            colids = range(0,self.numcols)
        # creating array for temporary storage
        temparray = self.array
        # looping through columns and shifting up each row
        for col in colids:
            for row in range(0,self.numrows):
                newrow = row - 1
                # wrapping indices so that we don't index out of range
                if newrow < 0:
                    newrow = self.numrows-1
                self.array[row][col] = temparray[newrow][col]

    # shiftDown: shifts the elements of the specified column down
    #            appending the bottom element to the top of the column
    # INPUT: colids (list of column indexes that you want to shift)
    # OUTPUT: None (stores new array in self.array)
    def shiftDown(self,colids=[]):
        # if no colids, shift all columns
        if colids == []:
            colids = range(0,self.numcols)
        # creating array for temporary storage
        temparray = self.array
        # looping through columns and shifting down each row
        for col in colids: 
            for row in range(0,self.numrows):
                newrow = row + 1
                # wrapping indices so that we don't index out of range
                if newrow == self.numrows:
                    newrow = 0           
                self.array[row][col] = temparray[newrow][col]







