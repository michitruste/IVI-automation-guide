import os, sys              # E401, F401 (both unused)
from ivi.radio import *     # F403 star import


class radio_helper:         # N801 use CapWords
    def SetFreq(self, f):   # N802 use lowercase
        if f == None: return    # E711, E701
        x = f * 2           # F841 never used
