#!/usr/bin/env python
import subprocess

def oneAtATime(msg):
	#I gave up on getting python to do the hash :P
	return (subprocess.check_output(['java', 'Hash', msg]))
