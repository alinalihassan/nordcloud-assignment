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

def get_literal_input(prompt: str):
    # Retry until input is valid
    while (True):
        try:
            value = literal_eval(input(prompt))
            # Comma separated tuples
            if type(value) is list and type(value[0]) is tuple:
                return value
            # Single tuple
            elif type(value) is tuple:
                return [value]
            raise ValueError
        except Exception:
            print("Invalid input, please try again. Example: (1,2,3), (4,5,6)")

    return None

def catch_stdout_for_function(func: callable):
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    func()

    output = new_stdout.getvalue()
    return output


def main():
    link_stations: List[LinkStation] = []
    link_stations_params = get_literal_input("Link Stations (x, y, reach): ")
    for params in link_stations_params:
        link_stations.append(LinkStation(*params))

    devices: List[Device] = []
    devices_params = get_literal_input("Devices (x, y): ")
    for params in devices_params:
        devices.append(Device(*params))

    find_best_station_for_devices(link_stations, devices)

def cloud_function(request):
    # Get parameters
    params = request.get_json()

    if 'run-sample' in params and params.get('run-sample') == True:
        output = catch_stdout_for_function(sample_run)

        return {'statusCode': 200, 'body': output}

    elif 'link-stations' in params and 'devices' in params:
        link_stations: List[LinkStation] = []
        devices: List[Device] = []

        for station in params.get('link-stations'):
            link_stations.append(LinkStation(x=station['x'], y=station['y'], reach=station['reach']))

        for device in params.get('devices'):
            devices.append(Device(x=device['x'], y=device['y']))

        output = catch_stdout_for_function(lambda: find_best_station_for_devices(link_stations, devices))

        return {'statusCode': 200, 'body': output}

    return {'statusCode': 400, 'body': 'Bad request'}

if __name__ == '__main__':
    run_sample = input("Run sample? (y/n): ") == 'y'

    if run_sample:
        sample_run()
    else:
        main()