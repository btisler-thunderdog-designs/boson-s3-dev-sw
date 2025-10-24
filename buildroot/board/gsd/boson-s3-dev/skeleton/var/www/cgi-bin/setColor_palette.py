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

color_setting = form.getvalue("color_palette")

print(color_setting)

with HiddenPrints():
	myCam = CamAPI.pyClient(manualport="/dev/ttyACM0",useDll=False)

if color_setting == "colorWhiteHot":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_WHITEHOT)

elif color_setting == "colorArctic":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_ARCTIC)

elif color_setting == "colorGradedFire":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_GRADEDFIRE)      

elif color_setting == "colorBlackHot":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_BLACKHOT)

elif color_setting == "colorRainbow":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_RAINBOW)

elif color_setting == "colorRainbowhc":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_RAINBOW_HC)

elif color_setting == "colorIronbow":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_IRONBOW)

elif color_setting == "colorLava":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_LAVA)

elif color_setting == "colorGlobow":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_GLOBOW)

elif color_setting == "colorHottest":
    result = myCam.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_HOTTEST)

with HiddenPrints():
	myCam.Close()