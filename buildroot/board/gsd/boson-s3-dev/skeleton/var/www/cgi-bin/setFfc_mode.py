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

ffc_mode = form.getvalue("ffc_mode")

print(ffc_mode)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

if ffc_mode == "setFfcMode_auto":
    myCam.bosonSetFFCMode(FLR_BOSON_FFCMODE_E.FLR_BOSON_AUTO_FFC)

elif ffc_mode == "setFfcMode_manual":
    myCam.bosonSetFFCMode(FLR_BOSON_FFCMODE_E.FLR_BOSON_MANUAL_FFC)

elif ffc_mode == "setFfcMode_external":
    myCam.bosonSetFFCMode(FLR_BOSON_FFCMODE_E.FLR_BOSON_EXTERNAL_FFC)

elif ffc_mode == "setFfcMode_shutter":
    myCam.bosonSetFFCMode(FLR_BOSON_FFCMODE_E.FLR_BOSON_SHUTTER_TEST_FFC)

with HiddenPrints():
	myCam.Close()