AUTO_OPENER PROJECT 

This automatic bottle opener software includes code for 2 stepper motors, 1 ultrasound sensor, 1 SPI display, 2 stepper motors, and 1 button.
Running opener.py will initiate the automatic bottles opener

-Once on, the device will show on the display that it is ready for a bottle to be placed and that once that is done, the button must be pressed to commence
-When the button is pressed, the sensor will begin reading distance
    -If the bottle is not detected, the display will tell the user to place the bottle closer to the sensor on the conveyor belt
    -If the bottle is detected, the conveyor motor stepper will initiate and rotate until the bottle is in the opener position 
    -When the button is pressed, the value 1 will be added to the bottles opened counter and will be displayed 
     (to clear the bottles opened counter the button must be pressed for more than 3 seconds)
- Once in the opening position, the opener motor will commence
- This motor will bring the bottle opener down to the bottle, and then return up to its initial position, removing the bottle cap in the process
- The conveyor motor will then return to its initial placement state and bring the bottle back to the user
- A message will display showing the number of bottles opened and a prompt for opening the next bottle
- Code repeats