
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
  - button

Requirements:
  - Hardware:
    - When button is pushed, the servo motor will begin to rotate until the bottle reaches a predetermined position 
    - The ultrasound sensor will then sense the bottle, add it to the counter, and then initiate the second stepper motor to commence its motion to come down to the cap of the bottle
    - If the bottle is in the correct position, the bottle opener will be in contact with the cap, and remove the cap as it is lifted back up by the motor 
    - A standard LCD will display the amount of bottles that have been opened since the device has been powered

"""

import time 
import math 
import bbpystepper as motor
import sonarnew
import hd44780

display = hd44780.HD44780()
sensor_loop_time = 0.5
opener_pos = 1 #would I input a value?

class Opener()
    init_pos= None
    current_pos= None 
    bottle_count= None
    conveyor_motor= None
    opener_motor= None
    sensor= None
    button= None
    display = None
    
    def __init__(self, button = "P2_2", conveyor_motor = ["P2_04", "P2_6", "P2_8", "P2_10"], opener_motor = ["P2_1", "P2_3", "P2_5", "P2_7"], sensor = ["P1_2", "P1_4"],
                display = ["P1_2", "P1_4", "P1_6"]):
        self.button = button 
        self.conveyor_motor = Stepper(pins=conveyor_motor) #what goes in parenthesis 
        self.opener_motor = Stepper(pins=opener_motor)
        self.sensor = Sensor(pins= sensor)
        self.display = disp.image() #would this be correct?
        self.bottle_count = 0
        self.reset_time = 3
        
        self.setup
        
    #end def
     
    
    def_run(self):
        while(true):
        try:
            display.clear()
            display.write("Place Bottle",1)
            display.write("Press Button to Begin",2)
            
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
            self.display.update(bottle_count)
            
        #end
            self.init_pos = self.sensor.getvalue()
            self.current_pos = self.init_pos
                if self.init_pos > 5 #5 inches? random value between 1-10 will be generated
                    display.write('Place Bottle Closer')
                    time.sleep(10)
                    break 
            else:
                while(self.init_pos > opener_pos):
                    self.conveyor_motor.rotate(90)
                    self.current_pos = seld.sensor.getvalue
                    time.sleep(2) #repeat every 2 seconds
            self.opener_motor(360)
            while(self.current_pos < self.init_pos):
                self.conveyor_motor(-360)
                self.current_pos = self.sensor.getvalue()
                time.sleep(1)
                 display.write("Total Bottles Open=" + bottle_count,1)
                 display.write("Want Another?")
                 
    #input cleanup
    
   #insert if __name__ = "main " function
            
                
                
    
            
                
    

