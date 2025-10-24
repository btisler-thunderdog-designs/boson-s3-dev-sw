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

result, curr_zoom = myCam.scalerGetZoom()

with HiddenPrints():
    myCam.Close()

roi_stats = {
    "x_location":curr_zoom.xCenter,
    "y_location":curr_zoom.yCenter,
    "zoom":curr_zoom.zoom,
}

print(json.dumps(roi_stats))
