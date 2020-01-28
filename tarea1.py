import time

actual_temp = 0
previous_temp = 1
gas_percentage = 0
fan = 0
limit = 230
learning = True
first = 0
second = 0
coeff = 0


def temperature(previous_temp, gas_percentage, fan):
    return (previous_temp + (5 * gas_percentage) - (10 * fan) - 1)


if __name__ == "__main__":
    while True:
        actual_temp = temperature(previous_temp, gas_percentage, fan)
        print(actual_temp)
        previous_temp = actual_temp
        if learning:
            difference = temperature(0, 2, 0) - temperature(0, 1, 0)
            punto_a = limit - temperature(0, 1, 0)
            n = punto_a
            punto_b = 1
            while n >= 0:
                punto_b += 1
                n -= difference
            learning = False
            coeff = (0 - punto_a) / (punto_b - 2)
        else:
            if actual_temp < limit:
                gas_percentage = (actual_temp - punto_a) / coeff + 1
                fan = 0
            else:
                gas_percentage = 0
                fan = 1
        time.sleep(1)
