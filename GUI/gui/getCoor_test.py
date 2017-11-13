import getCoor
import unittest

d = getCoor.Coor()

class TestCoordinate(unittest.TestCase):

    def test_coor(self):
        self.assertEqual(d.getNewCoor(['1',1],'N'), ['1',0])
        self.assertEqual(d.getNewCoor(['1',1],'S'), ['1',2])
        self.assertEqual(d.getNewCoor(['1',1],'W'), ['0',1])
        self.assertEqual(d.getNewCoor(['1',1],'E'), ['2',1])
    
    def test_cornercase(self):
        pass

if __name__ == "__main__":
    unittest.main()
