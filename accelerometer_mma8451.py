#!/user/bin/env python

import time

import board
import busio


import adafruit_mma8451

# Initialise I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialise MMA8451 module
sensor = [adafruit_mma8451.MMA8451(i2c, address=Cx10), adafruit_mma8451.MMA8451(i2c, address=Dx10)]

#sensorA = adafruit_mma8451.MMA8451(i2c, address=Cx10)
#sensorB = adafruit_mma8451.MMA8451(i2c, address=Dx10)

# Main program loop
while True:

    for i in sensor:
        x, y, z = sensor[i].acceleration

        # Print the acceleration at each axis (x, y, z)
        print("Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2".format(x, y, z))

    #x, y, z = sensor.acceleration

    # Print the acceleration at each axis (x, y, z)
    #print("Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2".format(x, y, z))

    time.sleep(1.0)

    sys.exit()