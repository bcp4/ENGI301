#Code for Ultrasonic Sensor that is to be imported in opener.py
# Credit to Kattni Rembor
# Website: https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython
# Repurposed to suit opener.py
# -----------------------------------------------------------------------------
import time
import board
import adafruit_hcsr04
import random


class Sensor()
    sensor = None
    
    def __init__(self, pins= ["P1_02", "P1_04"]):
        self.sensor= adafruit_hcsr04.HCSR04(trigger_pin= pins[0], echo_pin=pins[1])

    def getvalue(self):
        #value= self.sensor.distance
        value= 10*random.random()
        
        print(value)
        time.sleep(0.1)
        return value
      
