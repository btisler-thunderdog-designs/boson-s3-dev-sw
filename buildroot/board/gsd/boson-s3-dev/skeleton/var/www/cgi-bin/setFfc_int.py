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

ffc_int = form.getvalue("ffc_int")

print(ffc_int)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)
     
if ffc_int == "setFfcInt_2":
    myCam.gaoSetNumFFCFrames(2)

elif ffc_int == "setFfcInt_4":
    myCam.gaoSetNumFFCFrames(4)

elif ffc_int == "setFfcInt_8":
    myCam.gaoSetNumFFCFrames(8)

elif ffc_int == "setFfcInt_16":
    myCam.gaoSetNumFFCFrames(16)

with HiddenPrints():
	myCam.Close()