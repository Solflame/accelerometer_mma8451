#!/usr/bin/env python
import time
import board
import busio
import adafruit_mma8451


i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_mma8451.MMA8451(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)