# CircuitPython library for the HD44780 with serial interface (PCF8574T)
#
# Sample code
#
# Website: https://github.com/bablokb/circuitpython-hd44780
#
# -----------------------------------------------------------------------------

import time
import hd44780

display = hd44780.HD44780()


class Display()
    dislay= None
   
     def __init__(self, pins= ["P1_2", "P1_4", "P1_6"]):
        self.display= hd44780.HD44780()
while True:
  try:
    display.clear()
    display.write("Place Bottle",1)
    display.write("Press Button to Begin",2)
    time.sleep(1)

    display.clear()
    display.write("backlight off!",1)
    time.sleep(0.5)
    display.backlight(False)
    time.sleep(2)

    display.clear()
    display.write("backlight on!",1)
    display.backlight(True)
    time.sleep(2)
  except:
    break

display.clear()
display.backlight(False)