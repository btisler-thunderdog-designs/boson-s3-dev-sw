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

x_position = form.getvalue('pos_x')
y_position = form.getvalue('pos_y')
width = form.getvalue('roi_width')
height = form.getvalue('roi_height')
show_region = form.getvalue('show_region')

column_start = int(x_position) - int(width)//2
if column_start <= 0:
    column_start = 0
column_stop = int(x_position) + int(width)//2
if column_stop >= 640:
    column_stop = 640
row_start = int(y_position) - int(height)//2
if row_start <= 0:
    row_start = 0
row_stop = int(y_position) + int(height)//2
if row_stop >= 512:
    row_stop = 512

print("column start:", column_start)
print("column stop:", column_stop)
print("row start:", row_start)
print("row stop:", row_stop)

with HiddenPrints():
    myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

roi = FLR_ROI_T()

roi.rowStart = int(row_start)
roi.rowStop = int(row_stop)
roi.colStart = int(column_start)
roi.colStop = int(column_stop)

print("column start:", roi.colStart)
print("column stop:", roi.colStop)
print("row start:", roi.rowStart)
print("row stop:", roi.rowStop)

myCam.spotMeterSetRoi(roi)
      
x_value = int(column_start)
y_value = int(row_start)

if show_region == "true":
    myCam.symbologySetEnable(FLR_ENABLE_E.FLR_ENABLE)
    myCam.symbologyDelete(1)
    myCam.symbologyUpdateAndShow(1, 1)
if show_region == "false":
    myCam.symbologySetEnable(FLR_ENABLE_E.FLR_DISABLE)

with HiddenPrints():
    myCam.Close()