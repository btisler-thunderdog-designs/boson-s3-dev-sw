import os
import sys
import json
import warnings
warnings.filterwarnings("ignore", "'cgi' is deprecated", DeprecationWarning)
warnings.filterwarnings("ignore", "'cgitb' is deprecated", DeprecationWarning)

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

result, ffc_mode = myCam.bosonGetFFCMode()
result, ffc_gain_mode = myCam.bosonGetGainMode()
result, ffc_int_frames = myCam.gaoGetNumFFCFrames()
result, ffc_frame_thrsh = myCam.bosonGetFFCFrameThreshold()
result, ffc_temp_k = myCam.bosonGetLastFFCTempDegKx10()
result, ffc_temp_thrsh = myCam.bosonGetFFCTempThreshold()
result, fpa_temp_k = myCam.bosonlookupFPATempDegKx10()

with HiddenPrints():
    myCam.Close()

ffc_temp_k10 = ffc_temp_k/100
fpa_temp_k10 = fpa_temp_k/100

settings_info = {
    "ffc_mode":ffc_mode,
    "ffc_gain":ffc_gain_mode,
    "ffc_frames":ffc_int_frames,
    "ffc_period":ffc_frame_thrsh,
    "ffc_ltemp":ffc_temp_k10,
    "fpa_temp":fpa_temp_k10,
    "ffc_delta":ffc_temp_thrsh,
}

print(json.dumps(settings_info))
