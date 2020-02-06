import time
import numpy as np

actual_temp = 1
previous_temp = 2
gas_percentage = 0
fan = 0
limit = 230
learning = True
first = 0
second = 0
coeff = 0


def temperature(previous_temp, gas_percentage, fan):
    return (previous_temp + (20 * gas_percentage) - (10 * fan) - 1)


if __name__ == "__main__":
    while True:
        actual_temp = temperature(previous_temp, gas_percentage, fan)
        print("gas = {0:2.2f} fan = {1:2.2f} temp = {2:3.0f}".format(
            gas_percentage, fan, actual_temp))
        previous_temp = actual_temp
        if learning:
            difference = temperature(0, 2, 0) - temperature(0, 1, 0)
            point_a = limit - temperature(0, 1, 0)
            n = point_a
            point_b = 1
            while n >= 0: 
                point_b += 1
                n -= difference
            coeff = (0 - point_a) / (point_b - 2)
            reduce_factor = temperature(1000,0,10) - temperature(1000,0,9)
            learning = False
        else:
            if actual_temp < limit + 1:
                gas_percentage = (actual_temp - point_a) / coeff + 1
                if gas_percentage > 100:
                    gas_percentage = 100
                fan = 0
            else:
                gas_percentage = 0
                fan = (limit - actual_temp) / reduce_factor
                if fan > 10:
                    fan = 10
        time.sleep(1)
