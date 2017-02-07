#!/bin/bash
v4l2-ctl -d /dev/video0 -c auto_exposure=1 -c exposure=0
