import math
import numpy as np


def distance(a, b, x, y):
    return int(math.fabs(a - x) + math.fabs(b - y))


def time_to_start_ride(car_x, car_y, ride_x, ride_y, current_time, start_time):
    dist = distance(car_x, car_y, ride_x, ride_y)
    tmp = (start_time - current_time) - dist

    if tmp < 0:
        return dist
    else:
        return tmp


def calculate_wait_time(vehicle_position, ride_info, step):
    vehicle_x = vehicle_position[0]
    vehicle_y = vehicle_position[1]
    ride_x = ride_info[0]
    ride_y = ride_info[1]
    start = ride_info[4]
    calculated = time_to_start_ride(vehicle_x, vehicle_y, ride_x, ride_y, step, start)
    return calculated


def calculate_trip_time(ride_info):
    return distance(ride_info[0], ride_info[1], ride_info[2], ride_info[3])


if __name__ == '__main__':
    example = np.genfromtxt('a_example.in', dtype='int')
    should_be_easy = np.genfromtxt('b_should_be_easy.in')
    no_hurry = np.genfromtxt('c_no_hurry.in')

    general_data = no_hurry[0]
    rides_data = no_hurry[1:]
    vehicles = int(general_data[2])
    rides = int(general_data[3])
    steps = int(general_data[5])
    vehicle_info = np.zeros((vehicles, 3))
    output = []

    for i in range(vehicles):
        output.append([0])

    rides_with_flag = np.zeros((rides, 7))
    rides_with_flag[:, :-1] = rides_data
    rides_data = rides_with_flag

    for step in range(steps):
        for vehicle in range(vehicles):

            if vehicle_info[vehicle, 2] == step:
                min_ride = 1000000000000
                min_ride_index = -1

                for ride in range(0, rides):
                    if rides_data[ride, 6] == 0:
                        current_min_ride = calculate_wait_time(vehicle_info[vehicle], rides_data[ride], step)

                        if current_min_ride >= 0:
                            if current_min_ride < min_ride:
                                min_ride = current_min_ride
                                min_ride_index = ride

                if min_ride_index >= 0:
                    output[vehicle].append(min_ride_index)
                    # vehicle_row = np.append(output[vehicle], min_ride_index)
                    # output[vehicle] = vehicle_row
                    tmp = output[vehicle][0]
                    output[vehicle][0] = output[vehicle][0] + 1
                    vehicle_info[vehicle, 2] = min_ride + step + calculate_trip_time(rides_data[min_ride_index])
                    rides_data[min_ride_index, 6] = 1

    with open("test.txt", "w") as myfile:
        for line in output:
            for var in line:
                myfile.write(str(var) + ' ')
            myfile.write('\n')
