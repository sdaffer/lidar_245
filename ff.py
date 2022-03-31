#import adafruit_blinka 
#import adafruit_platformdetect
#import adafruit_vl53l0x

# import board
#import busio

#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_vl53l0x.VL53L0X(i2c)

import board
import busio
import adafruit_vl53l0x
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)