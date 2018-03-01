import math
import numpy as np


def distance(a, b, x, y):
    return int(math.fabs(a - x) + math.fabs(b - y))


def time_to_start_ride(car_x, car_y, ride_x, ride_y, current_time, start_time):
    turns = 0

    if current_time > start_time:
        turns = start_time - current_time
    else:
        dist = distance(car_x, car_y, ride_x, ride_y)
        turns = current_time + dist - start_time

    return turns


def calculate_time(vehicle, ride, step):
    vehicle_x = current_vehicle_positions[vehicle, 0]
    vehicle_y = current_vehicle_positions[vehicle, 1]
    ride_x = rides_data[ride, 0]
    ride_y = rides_data[ride, 1]
    start = rides_data[ride, 4]
    return time_to_start_ride(vehicle_x, vehicle_y, ride_x, ride_y, step, start)


if __name__ == '__main__':
    example = np.genfromtxt('a_example.in', dtype='int')
    should_be_easy = np.genfromtxt('b_should_be_easy.in')
    no_hurry = np.genfromtxt('c_no_hurry.in')

    output = []
    general_data = example[0]
    rides_data = example[1:]
    vehicles = general_data[2]
    rides = general_data[3]
    steps = general_data[5]
    current_vehicle_positions = np.zeros((vehicles, 2))

    for step in range(steps):
        for vehicle in range(vehicles):
            min_ride = calculate_time(vehicle, 0, step)
            min_ride_index = 0

            for ride in range(1, rides):
                current_min_ride = calculate_time(vehicle, ride, step)

                if current_min_ride < min_ride:
                    min_ride = current_min_ride
                    min_ride_index = ride
