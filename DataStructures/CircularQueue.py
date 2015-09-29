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