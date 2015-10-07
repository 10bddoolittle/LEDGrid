import unittest
from LEDArray import LEDArray
from DataStructures.CircularQueue import CircularQueue

class TestLEDArray(unittest.TestCase):

    def test_init(self):
        ledArray = LEDArray(2, 4)
        self.assertEqual(ledArray.array,[[0,0,0,0],[0,0,0,0]])
        self.assertEqual(ledArray.rowindices.queue,CircularQueue([0,1]).queue)

    def test_updateArray(self):
        ledArray = LEDArray(2, 2)
        ledArray.updateArray([[1,1],[1,1]])
        self.assertEqual(ledArray.array,[[1,1],[1,1]])

    def test_getActiveColumns(self):
        ledArray = LEDArray(2,2)
        self.assertEqual(ledArray.getActiveColumns(0),[0,0])
        ledArray.updateArray([[0,0],[1,1]])
        self.assertEqual(ledArray.getActiveColumns(1),[1,1])

    def test_getRowIndex(self):
        ledArray = LEDArray(4, 3)
        index = ledArray.getRowIndex()
        self.assertEqual(index,0)

if __name__ == '__main__':
    unittest.main()