import RPi.GPIO as gp


class PhysicalManager:

	exchangePin = [17, False, False]  # BCM Pin, IsPressed, Status

	def __init__(self):
		gp.setmode(gp.BCM)

		gp.setwarnings(False)

		gp.setup(self.exchangePin[0], gp.IN)
		pass

	def readPins(self):
		print(self.exchangePin)
		if (gp.input(self.exchangePin[0]) == gp.HIGH):
			if self.exchangePin[1] == False: 
				self.exchangePin[1] = True
				self.exchangePin[2] = not self.exchangePin[2]
				return True
		else:
			self.exchangePin[1]=False
		pass


a = PhysicalManager()

try:
	while True:
		a.readPins()
		pass
except KeyboardInterrupt:
	pass
