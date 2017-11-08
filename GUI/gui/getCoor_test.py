import getCoor
import unittest

d = getCoor.Coor()

class TestCoordinate(unittest.TestCase):

    def test_coor(self):
        self.assertEqual(d.getNewCoor(['B',1],'N'), ['B',0])
        self.assertEqual(d.getNewCoor(['B',1],'S'), ['B',2])
        self.assertEqual(d.getNewCoor(['B',1],'W'), ['A',1])
        self.assertEqual(d.getNewCoor(['B',1],'E'), ['C',1])
    
    def test_cornercase(self):
        pass

if __name__ == "__main__":
    unittest.main()
