#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Bool

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x400")

rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
pub2 = rospy.Publisher("chatter", String, queue_size=10)
pub_led = rospy.Publisher("led_control", Bool, queue_size=1)

def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = 0.0
    pub.publish(cmd)
    pub2.publish("forward")

def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z = 0.0
    pub.publish(cmd)
    pub2.publish("backward")

def lt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = AngularVel.get()
    pub.publish(cmd)
    pub2.publish("Turn Left")

def rt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = -AngularVel.get()
    pub.publish(cmd)
    pub2.publish("Turn Right")

def pen_on():
    pub2.publish("Pen On")
    pub_led.publish(data.data)  # Send a message to turn on the LED

def pen_off():
    pub2.publish("Pen Off")
    pub_led.publish(data.data)  # Send a message to turn off the LED

LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1)
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1)
AngularVel.pack()

B1 = Button(text="FW", command=fw)
B1.place(x=73, y=100)

B2 = Button(text="BW", command=bw)
B2.place(x=73, y=200)

B3 = Button(text="LT", command=lt)
B3.place(x=20, y=150)

B4 = Button(text="RT", command=rt)
B4.place(x=128, y=150)

B5 = Button(text="Pen On", command=pen_on)
B5.place(x=73, y=250)

B6 = Button(text="Pen Off", command=pen_off)
B6.place(x=73, y=300)

frame.mainloop()

