import os
import sys
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

form = cgi.FieldStorage()

x_center = form.getvalue('zoom_x')
y_center = form.getvalue('zoom_y')
zoom = form.getvalue('zoom_level')

print("x_center", x_center)
print("y_center", y_center)
print("zoom", zoom)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

result, zzoom = myCam.scalerGetZoom()
zzoom.xCenter = int(x_center)
zzoom.yCenter = int(y_center)
zzoom.zoom = int(zoom)
myCam.scalerSetZoom(zzoom)

with HiddenPrints():
	myCam.Close()