import unittest
from CircularQueue import CircularQueue

class TestCircularQueue(unittest.TestCase):

    def test_init(self):
        list = range(0,4)
        CQ = CircularQueue(list)
        self.assertEqual(CQ.queue,list)
        self.assertEqual(CQ.length,len(list))

    def test_shift(self):
        list = range(0,4)
        CQ = CircularQueue(list)
        CQ.shift()
        self.assertEqual(CQ.queue,[1,2,3,0])

    def test_getHead(self):
        list = range(0,4)
        CQ = CircularQueue(list)
        for i in list:
            self.assertEqual(CQ.getHead(),i)
            CQ.shift()

if __name__ == '__main__':
    unittest.main()