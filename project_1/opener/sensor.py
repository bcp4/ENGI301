import time
import board
from adafruit_hcsr04 import HCSR04
import Adafruit_BBIO.GPIO as GPIO
import display
import threading

button1 = "P2_02"

sensor = HCSR04(board.P1_2, board.P1_4)

#global variable 
sonar = 0 

#initial display values 
total_bottles = 0 

#counter 
def run(self):
        """Execute the main program."""
        bottle_count                 = 0        # Number of people to be displayed
        button_press_time            = 0.0      # Time button was pressed (in seconds)
        
        while(1):
            # Wait for button press
            while(GPIO.input(self.button) == 1):
                time.sleep(0.05)

            # Record time
            button_press_time = time.time()

            # Wait for button release
            while(GPIO.input(self.button) == 0):
                time.sleep(0.05)

            # Compare time to increment or reset people_count
            if ((time.time() - button_press_time) > self.reset_time):
                bottle_count = 0
            else:
                bottle_count = bottle_count + 1

            # Update the display
            self.display.update("Total Bottles Opened" + bottle_count)

    # End def

#reset value to 0 ASK HOW TO RESET VALUE 
def check_button():
    global sonar
    
    if GPIO.input(button1) == 3: #does this mean 3 seconds? 
        total_bottles = 0
        display.update("Total Bottles Opened" + total_bottles)
        return True 
    return False
    
  
        