from rflib import *
import signal
import sys

run = True
freq = 433000000
modulation = 4800

d = RfCat()
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmSyncMode(0)
d.setFreq(freq)
d.setMdmDRate(modulation)
d.setMaxPower();
d.lowball();

def signal_handler(sig, frame):
	print("Stopping...")
	global run
	run = False

signal.signal(signal.SIGINT, signal_handler)

print "Starting RFrecv() ..."
print "Frequency:", "{:,}".format(freq) + "Hz"
print "Modulation:", "{:,}".format(modulation) + "Bd"

while(run):
	try:
		y, packet = d.RFrecv()
		capture = packet.encode('hex')
		print capture
	except ChipconUsbTimeoutException:
		pass

d.setModeIDLE();
