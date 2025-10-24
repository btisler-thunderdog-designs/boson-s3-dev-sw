import os
import json
import sys
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

status, roi = myCam.spotMeterGetRoi()

cmd_status, mean_temp, deviation, min_temp, max_temp = myCam.spotMeterGetTempStats()
spot_stats = myCam.spotMeterGetSpotStats()
status, mean_val, deviation, min_spot, max_spot = spot_stats

with HiddenPrints():
    myCam.Close()

y_center = int((int(roi.rowStop) + int(roi.rowStart))//2)
x_center = int((int(roi.colStop) + int(roi.colStart))//2)
height = int(roi.rowStop) - int(roi.rowStart)
width = int(roi.colStop) - int(roi.colStart)

roi_stats = {
    "min_temp":min_temp.value,
    "max_temp":max_temp.value,
    "mean_temp":mean_temp,
    "mean_val":mean_val,
    "min_spot_row":min_spot.row,
    "min_spot_col":min_spot.column,
    "min_spot_value":min_spot.value,
    "max_spot_row":min_spot.row,
    "max_spot_col":min_spot.column,
    "max_spot_value":min_spot.value,
    "center_y":y_center,
    "center_x":x_center,
    "roi_w":width,
    "roi_h":height
}

print(json.dumps(roi_stats))