from dataclasses import dataclass
from typing import List, Tuple, Optional
from ast import literal_eval
import io
import sys
import math


@dataclass
class Point:
    """
    Point class used to represent coordinates in a 2D space.

    :param x: x coordinate
    :param y: y coordinate
    """
    x: float
    y: float

    def get_distance_to(self, point: 'Point'):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


@dataclass
class LinkStation(Point):
    """
    LinkStation class used to represent a station in a 2D space.

    :param x: x coordinate
    :param y: y coordinate
    :param reach: maximum distance from the station to a device
    """
    reach: float

    def get_power(self, device: 'Device'):
        distance = self.get_distance_to(device)
        return (self.reach - distance) ** 2 if self.reach > distance else 0


@dataclass
class Device(Point):
    """
    Device class used to represent a device in a 2D space.

    :param x: x coordinate
    :param y: y coordinate
    """
    def get_best_link_station(self, link_stations: List[LinkStation]) -> Tuple[Optional[LinkStation], int]:
        best_station = None
        best_power = 0

        for station in link_stations:
            power = station.get_power(self)
            if power > best_power:
                best_station = station
                best_power = power

        return best_station, best_power


def find_best_station_for_devices(link_stations: List[LinkStation], devices: List[Device]):
    for device in devices:
        station, power = device.get_best_link_station(link_stations)
        if station is not None:
            print(f'Best link station for point {device.x},{device.y} is {station.x},{station.y} with power {power}')
        else:
            print(f'No link station within reach for point {device.x},{device.y}')


def sample_run():
    link_stations = [
        LinkStation(x=0, y=0, reach=10),
        LinkStation(x=20, y=20, reach=5),
        LinkStation(x=10, y=0, reach=12)
    ]

    devices = [
        Device(x=0, y=0),
        Device(x=100, y=100),
        Device(x=15, y=10),
        Device(x=18, y=18)
    ]

    find_best_station_for_devices(link_stations, devices)


def main():
    link_stations: List[LinkStation] = []
    link_stations_params = literal_eval(input("Link Stations (x, y, reach): "))
    for params in link_stations_params:
        link_stations.append(LinkStation(*params))

    devices: List[Device] = []
    devices_params = literal_eval(input("Devices (x, y): "))
    for params in devices_params:
        devices.append(Device(*params))

    find_best_station_for_devices(link_stations, devices)

def cloud_function(request):
    # Catch input to string to serve it back
    new_stdout = io.StringIO()  
    sys.stdout = new_stdout

    sample_run()

    output = new_stdout.getvalue()

    return output


if __name__ == '__main__':
    run_sample = input("Run sample? (y/n): ") == 'y'

    if run_sample:
        sample_run()
    else:
        main()