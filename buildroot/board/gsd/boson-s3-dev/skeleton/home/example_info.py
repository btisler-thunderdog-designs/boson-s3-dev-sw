import os
from SDK_USER_PERMISSIONS import *

myCam = CamAPI.pyClient(manualport="/dev/ttyS1") # Boson COM port on Windows, check Device Manager

result1, cam_sernum = myCam.bosonGetCameraSN()
result2, sensor_sernum = myCam.bosonGetSensorSN()
result3, partnum_object = myCam.bosonGetCameraPN()


part_number = "".join(chr(char) for char in partnum_object.value)

print(" ")
print("--------------------------------------------------------------")

print("The serial number of this camera is",cam_sernum)
print("The serial number of this camera's sensor is",sensor_sernum)
print("The part number of this camera is", part_number)

print("--------------------------------------------------------------")
print(" ")

myCam.Close()