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

ffc_temp = form.getvalue('ffc_temp')

print(ffc_temp)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)
with HiddenPrints():
	myCam.bosonSetFFCTempThreshold(ffc_temp)
with HiddenPrints():
	myCam.Close()