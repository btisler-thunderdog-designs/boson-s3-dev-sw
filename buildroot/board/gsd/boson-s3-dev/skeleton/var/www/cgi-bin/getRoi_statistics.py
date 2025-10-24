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

result, min_value = myCam.imageStatsGetFirstBinInROI()
result, max_value = myCam.imageStatsGetLastBinInROI()
result, avg_value = myCam.imageStatsGetMeanInROI()
result, roi = myCam.imageStatsGetROI()

with HiddenPrints():
    myCam.Close()

y_center = int((int(roi.rowStop) + int(roi.rowStart))/2) + 1
x_center = int((int(roi.colStop) + int(roi.colStart))/2) + 1
height = int(roi.rowStop) - int(roi.rowStart) + 1
width = int(roi.colStop) - int(roi.colStart) + 1

roi_stats = {
    "min_value":min_value,
    "max_value":max_value,
    "avg_value":avg_value,
    "center_y":y_center,
    "center_x":x_center,
    "roi_w":width,
    "roi_h":height
}

print(json.dumps(roi_stats))



