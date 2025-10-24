import os
import sys
import json
import warnings
warnings.filterwarnings("ignore", "'cgi' is deprecated", DeprecationWarning)
warnings.filterwarnings("ignore", "'cgitb' is deprecated", DeprecationWarning)
import cgi, cgitb

sys.path.append('/home/')

from SDK_USER_PERMISSIONS import *

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

result, cam_sernum = myCam.bosonGetCameraSN()
result, sensor_sernum = myCam.bosonGetSensorSN()
result, partnum_object = myCam.bosonGetCameraPN()
software_rev = myCam.bosonGetSoftwareRev()

with HiddenPrints():
    myCam.Close()

part_number = "".join(chr(char) for char in partnum_object.value)

camera_info = {
    "camera_sn":cam_sernum,
    "sensor_sn":sensor_sernum,
    "camera_pn":part_number.replace("\u0000",""),
    "software_rev":f"{software_rev[1]}.{software_rev[2]}.{software_rev[3]}" 
}

print(json.dumps(camera_info))
