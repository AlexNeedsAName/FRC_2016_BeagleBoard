#!/bin/bash

echo "Booted" > /home/pi/log
source /home/pi/.profile
cd /home/pi/Desktop/vision2017
echo "Starting Vision Script" >> /home/pi/log
python VisionCore.py >> /home/pi/log
echo "Script Crashed" >> /home/pi/log
