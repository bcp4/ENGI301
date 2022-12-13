
"""
--------------------------------------------------------------------------
Automatic Bottle Opener
--------------------------------------------------------------------------
License:   
Copyright 2022 <Brandon Peoples>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make an automatic bottle opener:  
  - 2 stepper motors 
  - 1 ultrasound sensor 
  - 12V power adapter
  - 1 button
  - 1 SPI display

Requirements:
  - Hardware:
    - When button is pushed, the servo motor will begin to rotate until the bottle reaches a predetermined position 
    - The ultrasound sensor will then sense the bottle, add it to the counter, and then initiate the second stepper motor to commence its motion to come down to the cap of the bottle
    - If the bottle is in the correct position, the bottle opener will be in contact with the cap, and remove the cap as it is lifted back up by the motor 
    - A standard LCD will display the amount of bottles that have been opened since the device has been powered

"""

import time 
import math 
import random
import bbpystepper
import displaynew
import sonarnew


SENSOR_LOOP_TIME = 0.5
OPENER_POS       = 1     # Distance where bottle needs to be so that it can be opened
INIT_POS         = 10    # Initial distance the bottle is from the sensor


class Opener()
    init_pos= None
    current_pos= None 
    bottle_count= None
    conveyor_motor= None
    opener_motor= None
    sensor= None
    button= None
    display = None
    reset_time = None
    
    def __init__(self, button = "P2_2", conveyor_motor = ["P2_04", "P2_6", "P2_8", "P2_10"], opener_motor = ["P2_1", "P2_3", "P2_5", "P2_7"], sensor = ["P1_2", "P1_4"],
                display = ["P1_26", "P1_28", "P1_30", "P1_10", "P1_12", "P1_08", "P1_14", "P1_16"]):
        self.button         = button 
        self.conveyor_motor = bbpystepper.Stepper(pins=conveyor_motor) #what goes in parenthesis 
        self.opener_motor   = bbpystepper.Stepper(pins=opener_motor)
        self.sensor         = sonarnew.Sensor(pins= sensor)
        self.display        = displaynew.Display() #would this be correct?
        self.bottle_count   = 0
        self.reset_time     = reset_time
        
    #end def
     
    
    def run(self):
    
        while(1):
            # Initial display
            display.clear()
            display.write("Total Bottles Open=" + bottle_count, 1)
            display.write("Place bottle; Press Button", 2)            
            
            button_press_time            = 0.0      # Time button was pressed (in seconds)
           
            # Wait for button press
            while(GPIO.input(self.button) == 1):
                time.sleep(0.05)

            # Record time
            button_press_time = time.time()

            # Wait for button release
            while(GPIO.input(self.button) == 0):
                time.sleep(0.05)

            # Compare time to increment or reset bottle_count
            if ((time.time() - button_press_time) > self.reset_time):
                bottle_count = 0
            else:
                bottle_count = bottle_count + 1

                # Open Bottle Loop        
                self.init_pos    = self.sensor.getvalue()  # What values does the sensor return?

                # Wait for bottle to be put into position                
                while(self.init_pos > INIT_POS) # inches? random value between 1-10 will be generated
                    display.write('Place Bottle Closer', 1)
                    time.sleep(1)
                    self.init_pos    = self.sensor.getvalue()
                
                # Set position to return to
                self.current_pos = self.init_pos
                
                # Move bottle into opening position
                while(self.init_pos > OPENER_POS):
                    self.conveyor_motor.rotate(90)
                    self.current_pos = self.sensor.getvalue
                    time.sleep(2) #repeat every 2 seconds

                # Open the bottle                    
                self.opener_motor(360)
                time.sleep(10)
                self.opener_motor(-360)

                # Move bottle back                
                while(self.current_pos < self.init_pos):
                    self.conveyor_motor(-360)
                    self.current_pos = self.sensor.getvalue()
                    time.sleep(1)
                    
                
                
            
            
    def cleanup(self):
        display.write("Goodbye!", 1)
        self.conveyor_motor.cleanup()
        self.opener_motor.cleanup()

# Main Function        
if __name__ == '__main__':
    print("Program Start")
    
    opener = Opener()

    try:
        opener.run()
    except KeyboardInterrupt:
        pass

    # Clean up hardware when exiting
    opener.cleanup()

    print("Program Complete")
