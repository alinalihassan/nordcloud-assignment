import unittest

from src.main import LinkStation, Device


class LinkStationUnitTest(unittest.TestCase):
    def test_get_power(self):
        link_station = LinkStation(x=0, y=0, reach=10)
        device = Device(x=0, y=0)
        power = link_station.get_power(device)

        self.assertEqual(power, 100)

    def test_no_link_station(self):
        link_station = LinkStation(x=0, y=0, reach=10)
        device = Device(x=100, y=100)
        power = link_station.get_power(device)

        self.assertEqual(power, 0)


if __name__ == '__main__':
    unittest.main()
