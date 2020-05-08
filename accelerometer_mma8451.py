##!/usr/bin/env python

#import smbus2 as smbus
#import time
#import datetime
#import os
#import sys
#import logging
#import threading
#import RPi.GPIO as GPIO
#from collections import deque


## I2C
#I2C_ADDRESS_1 = cx10
#I2C_ADDRESS_2 = dx10

## Bus
#BUS_NUMBER = 1

#CFG_INTERRUPT = 1

## Ranges
#RANGE_2G = 0b00 # Default
#RANGE_4G = 0b01
#RANGE_8G = 0b10

#RANGE_DEFAULT = RANGE_2G

## Register addresses
#REG_STATUS = 0x00
#REG_WHOAMI = 0x0d
#REG_DEVID = 0x1A
#REG_OUT_X_MSB = 0x01
#REG_OUT_X_LSB = 0x02
#REG_OUT_Y_MSB = 0x03
#REG_OUT_Y_LSB = 0x04
#REG_OUT_Z_MSB = 0x05
#REG_OUT_Z_LSB = 0x06
#REG_F_SETUP = 0x09
#REG_XYZ_DATA_CFG = 0X0e
#REG_PL_STATUS = 0x10
#REG_PL_CFG = 0x11
#REG_CTRL_REG1 = 0x2A
#REG_CTRL_REG2 = 0x2B
#REG_CTRL_REG3 = 0x2C
#REG_CTRL_REG4 = 0x2D
#REG_CTRL_REG5 = 0x2E

## Data rate values
#DATARATE_800_HZ = 0x00 # 800Hz
#DATARATE_400_HZ = 0x08 # 400Hz
#DATARATE_200_HZ = 0x10 # 200Hz
#DATARATE_100_HZ = 0x18 # 100Hz
#DATARATE_50_HZ = 0x20 # 50Hz
#DATARATE_12_5_HZ = 0x28 # 12.5Hz
#DATARATE_6_25_HZ = 0x30 # 6.25Hz
#DATARATE_1_56_HZ = 0x38 # 1.56Hz

## Orientation values
#PL_PUF = 0
#PL_PUB = 1
#PL_PDF = 2
#PL_PDB = 3
#PL_LRF = 4
#PL_LRB = 5
#PL_LLF = 6
#PL_LLB = 7



#def my_callback(channel):
#    bus = smbus2.SMBus(1)
#    axisData = bus.read_i2c_block_data(i2caddr, REG_OUT_X_MSB, 6)
#    pass

#import configparser
#class Accel():
#    intEnabled = 0
#    info = ""

#    def __init__(self):
#        self.b = smbus.SMBus(BUS_NUMBER)
#        self.a = i2caddr
#        self.info = GPIO.RPI_INFO


#    def whoAmI(self):
#        return self.b.read_byte_data(i2caddr, REG_WHOAMI)


#    def init(self):
#        # TODO: Setup registers

#        if CFG_INTERRUPT == 1:
#            GPIO.setmode(GPIO.BCM)
#            GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#            GPIO.add_event_detect(17, GPIO.FALLING, callback = my_callback)
#            self.intEnabled = 1;
#            my_callback(0)