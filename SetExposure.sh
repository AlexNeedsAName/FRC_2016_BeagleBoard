#!/bin/bash
#Find the video in /dev, then set exposure to zero

video=$(sudo find /dev -name "video*")

v4l2-ctl -d "$video" -c exposure_auto=1 -c exposure_absolute=$1
