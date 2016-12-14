#!/usr/bin/python

# Imports
import pigpio
import rospy
from std_msgs.msg import String
import time

class BacklightControl:
    """This class is the ROS nodes used to control backlight module"""

    def __init__(self):
        # ROS init
        self.node_name = self.__class__.__name__
        rospy.init_node(self.node_name, anonymous=True)
        self.rate = rospy.Rate(10)  # 10Hz

        # ROS subscriptions
        self.subscriber = rospy.Subscriber('Backlight_Color', String, self.callback_set_color)

        # ROS publishments
        self.done_module = rospy.Publisher('Done_Module', String, queue_size=10)

        #TODO
        # GPIO 
        self.white_pin = 10
        self.blue_pin = 25

        """This function initializes GPIO pins for the node"""

        self.gpio = pigpio.pi()
        self.gpio.wave_tx_stop()
        self.gpio.wave_clear()

        self.gpio.set_mode(self.white_pin, pigpio.OUTPUT)
        self.gpio.write(self.white_pin, pigpio.LOW)

        self.gpio.set_mode(self.blue_pin, pigpio.OUTPUT)
        self.gpio.write(self.blue_pin, pigpio.LOW)


    def callback_set_color(self, data):

        self.gpio.write(self.white_pin,pigpio.LOW)
        self.gpio.write(self.blue_pin, pigpio.LOW)

        # white_pin HIGH     
        if data.data == "white":
            self.gpio.write(self.white_pin, pigpio.HIGH)

        # blue_pin HIGH
        elif data.data == "blue":
            self.gpio.write(self.blue_pin, pigpio.HIGH)

        # All gpio to 0
        else:
            pass

        self.done_module.publish("Backlight")

    # Listening function
    def listener(self):
        rospy.spin()


if __name__ == '__main__':
    try:
        bm = BacklightControl()
        bm.listener()

    except rospy.ROSInterruptException as e:
        print(e)

