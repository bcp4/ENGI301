#Code for LCD display that is to be imported in opener.py
# CircuitPython library for the HD44780 with serial interface (PCF8574T)
# Credit to user bablokb (github)
# Website: https://github.com/bablokb/circuitpython-hd44780
# Repurposed to suit opener.py
# -----------------------------------------------------------------------------

import time
import hd44780

display = hd44780.HD44780()


class Display()
    dislay= None
   
     def __init__(self, pins= ["P1_26", "P1_28", "P1_30", "P1_10", "P1_12", "P1_08", "P1_14", "P1_16"]):
        self.display= hd44780.HD44780()
    def clear():
        self.display.clear()
    
    def write(self,value, line):
        self.display.write(value, line)
