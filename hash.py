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
		print byte
		hash += (byte)
		hash += (hash << 10)
		print hash
		hash ^= (rshift(hash, 6))
		print hash

	hash += (hash << 3)
	hash ^= (rshift(hash, 11))
	hash += (hash << 15)
	print hash
