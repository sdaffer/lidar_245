import serial
import re
import numpy as np
import pandas as pd

# arduino_port = "COM7"
# arduino_port = "/dev/ttyUSB0"
# arduino_port = "COM9"
# arduino_port = "/dev/ttyACM0"
baud = 115200 
# data = numpy.zero((1))
data = []
data = np.zeros((1))

ser = serial.Serial(arduino_port, baud, timeout=1)
print("Connected to Arduino port:" + arduino_port)

# while(True):
for i in range(950):
    string=str(ser.readline())
    match = re.search(r'[\w.-]+\d+', string)
    if match:
        print(match.group())
        data = np.append(data, match.group())
    else:
        print("-9999")
        data = np.append(data, -9999)

data = data[1:-1]
pd.DataFrame(data).to_csv('file.csv')