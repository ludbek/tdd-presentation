from geometry import Cuboid
import unittest

class TestCuboid(unittest.TestCase):
    def setUp(self):
        self.acuboid = Cuboid(10, 20, 30)

    def test_area(self):
        assert self.acuboid.get_area() == 200

    def test_volume(self):
        assert self.acuboid.get_volume() == 6000
