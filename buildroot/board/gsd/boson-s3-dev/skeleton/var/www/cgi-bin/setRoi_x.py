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

#print(x_position)
#print(y_position)
#print(width)
#print(height)

column_start = int(x_position) - int(width)/2
column_stop = int(x_position) + int(width)/2
row_start = int(y_position) - int(height)/2
row_stop = int(y_position) + int(height)/2

with HiddenPrints():
    myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

result, roi = myCam.imageStatsGetROI()

roi.rowStart = int(row_start)
roi.rowStop = int(row_stop)
roi.colStart = int(column_start)
roi.colStop = int(column_stop)

myCam.imageStatsSetROI(roi)
      
x_value = int(column_start)
y_value = int(row_start)

myCam.symbologySetEnable(FLR_ENABLE_E.FLR_ENABLE)
myCam.symbologyDelete(1)
myCam.symbologyCreateOutlinedRectangle(1, x_value, y_value, int(width), int(height), 1)
myCam.symbologyUpdateAndShow(1, 1)

with HiddenPrints():
    myCam.Close()