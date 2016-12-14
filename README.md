# backlight_module

This repository contains the ROS nodes that control the backlight module 
of the BioBotus project. 

backlight_control.py is subscribing to Backlight_Color which is a string 
ROS topics. It can received 3 values :

- "white", sets the GPIO pin 10 to High
- "blue", sets the GPIO pin 25 to High
- "None", sets the GPIO pin 10 and 25 to Low

GPIO Pins 10 and 25 are outputs pins and are connected to the relay circuit 
in the backlight physical model to polarize the the diodes stripes.

Once the GPIO pins are setted, the ROS node publish a 
Done_Module("backlight_module")

Note : Everytime this ROS node receive a Backlight_Color topics, it sets the 
       GPIO pins 10 and 25 to Low. 
