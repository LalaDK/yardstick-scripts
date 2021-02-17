#!/usr/bin/env python2
from rflib import *
import signal
import sys

run = True
freq = 700000000
baudrate = 2000

d = RfCat()
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmSyncMode(0)
d.setFreq(freq)
d.setMdmDRate(baudrate)
d.setMaxPower();
d.lowball();

def signal_handler(sig, frame):
	print("Stopping...")
	global run
	run = False

signal.signal(signal.SIGINT, signal_handler)

print "Starting RFrecv() ..."
print "Frequency:{:,}Hz".format(freq)
print "Baud rate: {:,}Bd".format(baudrate)

while(run):
	try:
		y, packet = d.RFrecv()
		capture = packet.encode('hex')
		print capture
	except ChipconUsbTimeoutException:
		pass

d.setModeIDLE();
