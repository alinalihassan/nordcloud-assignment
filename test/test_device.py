import unittest

from src.main import LinkStation, Device


class DeviceTestCase(unittest.TestCase):
    def test_get_best_link_station(self):
        link_stations = [LinkStation(x=0, y=0, reach=10)]
        device = Device(x=0, y=0)
        station, power = device.get_best_link_station(link_stations)

        self.assertEqual(station, link_stations[0])
        self.assertEqual(power, 100)

    def test_no_link_station(self):
        link_stations = [LinkStation(x=0, y=0, reach=10)]
        device = Device(x=100, y=100)
        station, power = device.get_best_link_station(link_stations)

        self.assertIsNone(station)
        self.assertEqual(power, 0)


if __name__ == '__main__':
    unittest.main()
