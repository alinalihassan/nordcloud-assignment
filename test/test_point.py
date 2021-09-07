import unittest

from src.main import Point


class PointTestCase(unittest.TestCase):
    def test_point_validity(self):
        point = Point(7, -14)

        self.assertEqual(point.x, 7)
        self.assertEqual(point.y, -14)

    def test_point_equality(self):
        point1 = Point(0, 0)
        point2 = Point(0, 0)
        point3 = Point(0, 1)

        self.assertEqual(point1, point2)
        self.assertNotEqual(point1, point3)

    def test_point_distance(self):
        point1 = Point(-7, -4)
        point2 = Point(17, 6.5)

        print(point1.get_distance_to(point2))
        self.assertEqual(point1.get_distance_to(point2), 26.196373794859472)


if __name__ == '__main__':
    unittest.main()
