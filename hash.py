#!/usr/bin/env python
import sys
def rshift(val, n):
	if(val >= 0):
		return val>>n
	else:
		return (val+0x100000000)>>n

def oneAtATime(msg):
	key = bytearray()
	key.extend(map(ord, msg))

	hash = 0
	for byte in key:
		hash += (byte)
		hash += (hash << 10)
		hash ^= (rshift(hash, 6))
		
	hash += (hash << 3)
	hash ^= (rshift(hash, 11))
	hash += (hash << 15)
	return hash
