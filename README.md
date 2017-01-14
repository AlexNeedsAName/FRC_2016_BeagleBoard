# FRC_2016_BeagleBoard
The BeagleBoard side of the code for my FRC robot.

This repo includes a file for each openCV function our robot will use during autonomous. Documentation for the code for the 2017 FIRST STEAMWORKS challenge is shown below.

# Client.java
This file is used to communicate between the beagleboard and the roboRIO. It takes in values through stdin and then sends them through UDP to the roboRIO. It also can read messages received from the roboRIO. It is compiled with:
  javac Client.java
and run with:
  java Client
You can then type in values and they will be sent to the roboRIO. (If you are encountering any read errors on the roboRIO add a space after the text you write since that is how the roboRIO splits the incoming UDP string).

# BoilerLine.py
This python file is used to detect and figure out the angle of a line using openCV, and output that angle to stdout (or terminal). It is currently configured to track red lines, but you can change the threshold values to track different colors. At the moment I have it configured to update only once every few seconds (so that the roboRIO can update it's position before re-calculating the line position, since lag and motion blur can cause the roboRIO to constantly overshoot the line).

There are some performance changes I am currently working on for this code. One of these changes will figure out the perspective of the camera. For example if my camera is looking at the ground at a 45 degree angle, a part of the image farther away will be smaller then a part closer. So I am working on getting the image to warp so that openCV can correctly calculate the angle of the line as if it was looking down on the ground from a top-down view.

# Running the entire program
To run the entire program you can take the data coming from BoilerLine's stdout and pipe that into Client.java. This can be done by running:
  python BoilerLine.py | java Client
