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

with HiddenPrints():
    myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

enable = form.getvalue('enable')
units = form.getvalue('units')

if enable == "true":
    myCam.spotMeterSetEnable(FLR_ENABLE_E.FLR_ENABLE)
    if units == "fahrenheit":
        myCam.spotMeterSetStatsMode(FLR_SPOTMETER_STATS_TEMP_MODE_E.FLR_SPOTMETER_FAHRENHEIT)
    if units == "celcius":        
        myCam.spotMeterSetStatsMode(FLR_SPOTMETER_STATS_TEMP_MODE_E.FLR_SPOTMETER_CELCIUS)
    print("Spotmeter Enabled")

if enable == "false":
    myCam.spotMeterSetEnable(FLR_ENABLE_E.FLR_DISABLE)
    print("Spotmeter Disabled")

with HiddenPrints():
    myCam.Close()