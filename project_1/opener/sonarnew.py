import time
import board
import adafruit_hcsr04
import random


class Sensor()
    sensor = None
    
    def __init__(self, pins= ["P1_2", "P1_4"]):
        self.sensor= adafruit_hcsr04.HCSR04(trigger_pin= pins[0], echo_pin=pins[1])

    def getvalue(self):
        #value= self.sensor.distance
        value= 10*random.random()
        
        print(value)
        time.sleep(0.1)
        return value
      
