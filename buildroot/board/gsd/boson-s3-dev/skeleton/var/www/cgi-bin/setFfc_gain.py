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

ffc_gain = form.getvalue("ffc_gain")

print(ffc_gain)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)
     
if ffc_gain == "setFfcGain_high":
    myCam.bosonSetGainMode(FLR_BOSON_GAINMODE_E.FLR_BOSON_HIGH_GAIN)

elif ffc_gain == "setFfcGain_low":
    myCam.bosonSetGainMode(FLR_BOSON_GAINMODE_E.FLR_BOSON_LOW_GAIN)

elif ffc_gain == "setFfcGain_auto":
    myCam.bosonSetGainMode(FLR_BOSON_GAINMODE_E.FLR_BOSON_AUTO_GAIN)

elif ffc_gain == "setFfcGain_dual":
    myCam.bosonSetGainMode(FLR_BOSON_GAINMODE_E.FLR_BOSON_DUAL_GAIN)

elif ffc_gain == "setFfcGain_manual":
    myCam.bosonSetGainMode(FLR_BOSON_GAINMODE_E.FLR_BOSON_MANUAL_GAIN)

with HiddenPrints():
	myCam.Close()